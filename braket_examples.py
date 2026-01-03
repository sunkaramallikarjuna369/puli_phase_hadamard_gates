"""
Amazon Braket Examples for Quantum Gates: Pauli, Phase, and Hadamard
Demonstration of quantum gate operations using AWS Amazon Braket

These examples show how to implement and visualize quantum gates
including Pauli-X, Pauli-Y, Pauli-Z, Phase, T-gate, and Hadamard gates.
Compatible with local simulator and cloud-based quantum hardware.
"""

from braket.circuits import Circuit, gates
from braket.devices import LocalSimulator, AwsDevice
from braket.aws import AwsSession
import numpy as np
from collections import Counter


class BraketQuantumGateExamples:
    """
    A comprehensive class demonstrating quantum gate operations using Amazon Braket.
    
    Includes:
    - Pauli gates (X, Y, Z)
    - Phase gates (S, T, Phase)
    - Hadamard gate
    - Gate combinations and circuits
    - Local simulator and AWS device support
    """
    
    def __init__(self, use_aws=False, device_arn=None):
        """
        Initialize the Braket quantum examples.
        
        Args:
            use_aws (bool): Whether to use AWS device or local simulator
            device_arn (str): AWS device ARN if using cloud hardware
        """
        if use_aws and device_arn:
            self.device = AwsDevice(device_arn)
        else:
            self.device = LocalSimulator()
        
        self.use_aws = use_aws
        self.device_arn = device_arn
    
    def pauli_x_gate_example(self):
        """
        Pauli-X (NOT) Gate Example
        
        The Pauli-X gate flips the qubit state:
        |0⟩ → |1⟩
        |1⟩ → |0⟩
        
        Matrix representation:
        [[0, 1],
         [1, 0]]
        """
        # Create circuit with X gate
        circuit = Circuit()
        circuit.x(0)  # Apply X gate to qubit 0
        circuit.result_type.sample(observable=gates.Operator.Z())  # Measure Z basis
        
        # Run on device
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Pauli-X Gate (Amazon Braket) ===")
        print(f"Input: |0⟩")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: All measurements should give |1⟩")
        
        return counts, circuit
    
    def pauli_y_gate_example(self):
        """
        Pauli-Y Gate Example
        
        The Pauli-Y gate:
        |0⟩ → i|1⟩
        |1⟩ → -i|0⟩
        
        Matrix representation:
        [[0, -i],
         [i,  0]]
        """
        circuit = Circuit()
        circuit.y(0)  # Apply Y gate
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Pauli-Y Gate (Amazon Braket) ===")
        print(f"Input: |0⟩")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: All measurements should give |1⟩")
        
        return counts, circuit
    
    def pauli_z_gate_example(self):
        """
        Pauli-Z Gate Example
        
        The Pauli-Z gate applies a phase flip:
        |0⟩ → |0⟩
        |1⟩ → -|1⟩
        
        Matrix representation:
        [[1,  0],
         [0, -1]]
        """
        circuit = Circuit()
        circuit.h(0)      # Create superposition with Hadamard
        circuit.z(0)      # Apply Z gate
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Pauli-Z Gate (Amazon Braket) ===")
        print(f"Input: (|0⟩ + |1⟩)/√2 (after Hadamard)")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: Roughly equal distribution")
        
        return counts, circuit
    
    def phase_gate_example(self):
        """
        Phase (S) Gate Example
        
        The Phase gate (S gate):
        |0⟩ → |0⟩
        |1⟩ → i|1⟩
        
        Matrix representation:
        [[1, 0],
         [0, i]]
        """
        circuit = Circuit()
        circuit.h(0)      # Superposition
        circuit.s(0)      # Apply S (Phase) gate
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Phase (S) Gate (Amazon Braket) ===")
        print(f"Input: (|0⟩ + |1⟩)/√2")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: Roughly equal distribution (phase not observable in Z basis)")
        
        return counts, circuit
    
    def t_gate_example(self):
        """
        T Gate Example
        
        The T gate (π/8 gate):
        |0⟩ → |0⟩
        |1⟩ → e^(iπ/4)|1⟩
        
        Matrix representation:
        [[1, 0],
         [0, e^(iπ/4)]]
        """
        circuit = Circuit()
        circuit.h(0)      # Superposition
        circuit.t(0)      # Apply T gate
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== T Gate (π/8) (Amazon Braket) ===")
        print(f"Input: (|0⟩ + |1⟩)/√2")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: Roughly equal distribution")
        
        return counts, circuit
    
    def hadamard_gate_example(self):
        """
        Hadamard Gate Example
        
        The Hadamard gate creates superposition:
        |0⟩ → (|0⟩ + |1⟩)/√2
        |1⟩ → (|0⟩ - |1⟩)/√2
        
        Matrix representation:
        (1/√2) * [[1,  1],
                   [1, -1]]
        """
        circuit = Circuit()
        circuit.h(0)  # Apply Hadamard gate
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Hadamard Gate (Amazon Braket) ===")
        print(f"Input: |0⟩")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: Roughly equal distribution (50% 0, 50% 1)")
        
        return counts, circuit
    
    def hadamard_twice_example(self):
        """
        Double Hadamard Gate Example
        
        Two consecutive Hadamard gates return the qubit to its original state:
        H * H = I (Identity)
        
        |0⟩ → (|0⟩ + |1⟩)/√2 → |0⟩
        """
        circuit = Circuit()
        circuit.h(0)  # First Hadamard
        circuit.h(0)  # Second Hadamard
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Double Hadamard Gate (Amazon Braket) ===")
        print(f"Input: |0⟩")
        print(f"Operations: H → H")
        print(f"Measurement counts: {dict(counts)}")
        print(f"Expected: All measurements should give |0⟩")
        
        return counts, circuit
    
    def complex_circuit_example(self):
        """
        Complex Multi-Gate Circuit Example
        
        Demonstrates a circuit combining multiple gates:
        |0⟩ → H → X → S → H → Measure
        """
        circuit = Circuit()
        circuit.h(0)      # Hadamard: superposition
        circuit.x(0)      # Pauli-X: flip
        circuit.s(0)      # Phase gate
        circuit.h(0)      # Hadamard again
        circuit.result_type.sample(observable=gates.Operator.Z())
        
        task_result = self.device.run(circuit, shots=1000).result()
        measurements = task_result.measurements
        counts = Counter(tuple(measurement) for measurement in measurements)
        
        print("\n=== Complex Multi-Gate Circuit (Amazon Braket) ===")
        print(f"Input: |0⟩")
        print(f"Circuit: H → X → S → H")
        print(f"Measurement counts: {dict(counts)}")
        print(f"\nCircuit structure:")
        print(circuit)
        
        return counts, circuit
    
    def run_all_examples(self):
        """
        Run all gate examples and display results.
        """
        device_info = "AWS Cloud" if self.use_aws else "Local Simulator"
        
        print("\n" + "="*60)
        print(f"QUANTUM GATES WITH AMAZON BRAKET - {device_info.upper()}")
        print("="*60)
        
        # Run individual gate examples
        self.pauli_x_gate_example()
        self.pauli_y_gate_example()
        self.pauli_z_gate_example()
        self.phase_gate_example()
        self.t_gate_example()
        self.hadamard_gate_example()
        self.hadamard_twice_example()
        self.complex_circuit_example()
        
        print("\n" + "="*60)
        print("All examples completed successfully!")
        print("="*60 + "\n")


# Main execution
if __name__ == "__main__":
    """
    Execute all Amazon Braket examples for quantum gates.
    
    This demonstrates:
    1. Individual Pauli gates (X, Y, Z) with Braket
    2. Phase gates (S, T) implementation
    3. Hadamard gate and superposition
    4. Complex multi-gate circuits
    5. Measurement using local simulator
    
    To use AWS cloud hardware, set use_aws=True and provide device_arn.
    Device ARN example: "arn:aws:braket:::device/qpu/ionq/ionQdevice"
    """
    
    # Using local simulator (no AWS credentials needed)
    print("Initializing Amazon Braket examples with Local Simulator...")
    examples = BraketQuantumGateExamples(use_aws=False)
    examples.run_all_examples()
    
    # To use AWS cloud hardware, uncomment below:
    # examples_aws = BraketQuantumGateExamples(
    #     use_aws=True,
    #     device_arn="arn:aws:braket:::device/qpu/ionq/ionQdevice"
    # )
    # examples_aws.run_all_examples()
