"""
Qiskit Examples for Quantum Gates: Pauli, Phase, and Hadamard
Demonstration of fundamental quantum gate operations using IBM Qiskit

These examples show how to implement and visualize quantum gates
including Pauli-X, Pauli-Y, Pauli-Z, Phase, T-gate, and Hadamard gates.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
from qiskit.visualization import plot_histogram, circuit_drawer
import numpy as np
import matplotlib.pyplot as plt


class QuantumGateExamples:
    """
    A comprehensive class demonstrating quantum gate operations using Qiskit.
    
    Includes:
    - Pauli gates (X, Y, Z)
    - Phase gates (S, T, Phase)
    - Hadamard gate
    - Gate combinations and circuits
    """
    
    def __init__(self):
        self.simulator = Aer.get_backend('qasm_simulator')
    
    def pauli_x_gate(self):
        """
        Pauli-X (NOT) Gate Example
        
        The Pauli-X gate flips the qubit state:
        |0⟩ → |1⟩
        |1⟩ → |0⟩
        
        Matrix representation:
        [[0, 1],
         [1, 0]]
        """
        qc = QuantumCircuit(1, 1, name='Pauli-X Example')
        
        # Apply X gate to |0⟩ state
        qc.x(0)
        qc.measure(0, 0)
        
        # Execute and get results
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Pauli-X Gate Example ===")
        print("Input: |0⟩")
        print(f"Output: {counts}")
        print("Expected: {'1': 1000} (all measurements give |1⟩)")
        
        return counts, qc
    
    def pauli_y_gate(self):
        """
        Pauli-Y Gate Example
        
        The Pauli-Y gate:
        |0⟩ → i|1⟩
        |1⟩ → -i|0⟩
        
        Matrix representation:
        [[0, -i],
         [i,  0]]
        """
        qc = QuantumCircuit(1, 1, name='Pauli-Y Example')
        
        # Apply Y gate to |0⟩ state
        qc.y(0)
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Pauli-Y Gate Example ===")
        print("Input: |0⟩")
        print(f"Output: {counts}")
        print("Expected: {'1': 1000} (all measurements give |1⟩)")
        
        return counts, qc
    
    def pauli_z_gate(self):
        """
        Pauli-Z Gate Example
        
        The Pauli-Z gate applies a phase flip:
        |0⟩ → |0⟩
        |1⟩ → -|1⟩
        
        Matrix representation:
        [[1,  0],
         [0, -1]]
        """
        qc = QuantumCircuit(2, 1, name='Pauli-Z Example')
        
        # Create superposition first
        qc.h(0)
        # Apply Z gate
        qc.z(0)
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Pauli-Z Gate Example ===")
        print("Input: (|0⟩ + |1⟩)/√2 (after Hadamard)")
        print(f"Output: {counts}")
        print("Expected: Roughly equal distribution between 0 and 1")
        
        return counts, qc
    
    def phase_gate(self):
        """
        Phase (S) Gate Example
        
        The Phase gate (S gate):
        |0⟩ → |0⟩
        |1⟩ → i|1⟩
        
        Matrix representation:
        [[1, 0],
         [0, i]]
        """
        qc = QuantumCircuit(1, 1, name='Phase Gate Example')
        
        # Create superposition
        qc.h(0)
        # Apply phase gate
        qc.s(0)
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Phase (S) Gate Example ===")
        print("Input: (|0⟩ + |1⟩)/√2")
        print(f"Output: {counts}")
        print("Expected: Roughly equal distribution (phase is not observable)")
        
        return counts, qc
    
    def t_gate(self):
        """
        T Gate Example
        
        The T gate (π/8 gate):
        |0⟩ → |0⟩
        |1⟩ → e^(iπ/4)|1⟩
        
        Matrix representation:
        [[1, 0],
         [0, e^(iπ/4)]]
        """
        qc = QuantumCircuit(1, 1, name='T Gate Example')
        
        # Create superposition
        qc.h(0)
        # Apply T gate
        qc.t(0)
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== T Gate Example ===")
        print("Input: (|0⟩ + |1⟩)/√2")
        print(f"Output: {counts}")
        print("Expected: Roughly equal distribution")
        
        return counts, qc
    
    def hadamard_gate(self):
        """
        Hadamard Gate Example
        
        The Hadamard gate creates superposition:
        |0⟩ → (|0⟩ + |1⟩)/√2
        |1⟩ → (|0⟩ - |1⟩)/√2
        
        Matrix representation:
        (1/√2) * [[1,  1],
                   [1, -1]]
        """
        qc = QuantumCircuit(1, 1, name='Hadamard Gate Example')
        
        # Apply Hadamard gate
        qc.h(0)
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Hadamard Gate Example ===")
        print("Input: |0⟩")
        print(f"Output: {counts}")
        print("Expected: Roughly equal distribution between 0 and 1")
        
        return counts, qc
    
    def hadamard_twice(self):
        """
        Double Hadamard Gate Example
        
        Two consecutive Hadamard gates return the qubit to its original state.
        H * H = I (Identity)
        
        |0⟩ → (|0⟩ + |1⟩)/√2 → |0⟩
        """
        qc = QuantumCircuit(1, 1, name='Double Hadamard Example')
        
        # Apply Hadamard twice
        qc.h(0)
        qc.h(0)
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Double Hadamard Gate Example ===")
        print("Input: |0⟩")
        print("Operations: H → H")
        print(f"Output: {counts}")
        print("Expected: {'0': 1000} (returns to |0⟩)")
        
        return counts, qc
    
    def gate_combination_circuit(self):
        """
        Complex Gate Combination Example
        
        Demonstrates a circuit combining multiple gates:
        |0⟩ → H → X → S → H → Measure
        """
        qc = QuantumCircuit(1, 1, name='Gate Combination')
        
        # Create complex circuit
        qc.h(0)      # Hadamard: superposition
        qc.x(0)      # Pauli-X: flip
        qc.s(0)      # Phase gate
        qc.h(0)      # Hadamard again
        qc.measure(0, 0)
        
        job = execute(qc, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        
        print("\n=== Gate Combination Circuit ===")
        print("Input: |0⟩")
        print("Circuit: |0⟩ → H → X → S → H → Measure")
        print(f"Output: {counts}")
        
        # Draw circuit
        print("\nCircuit Diagram:")
        print(qc)
        
        return counts, qc
    
    def run_all_examples(self):
        """
        Run all gate examples and display results.
        """
        print("\n" + "="*50)
        print("QUANTUM GATES WITH QISKIT - COMPREHENSIVE EXAMPLES")
        print("="*50)
        
        # Run individual gate examples
        self.pauli_x_gate()
        self.pauli_y_gate()
        self.pauli_z_gate()
        self.phase_gate()
        self.t_gate()
        self.hadamard_gate()
        self.hadamard_twice()
        self.gate_combination_circuit()
        
        print("\n" + "="*50)
        print("All examples completed successfully!")
        print("="*50 + "\n")


# Main execution
if __name__ == "__main__":
    """
    Execute all Qiskit examples for quantum gates.
    
    This demonstrates:
    1. Individual Pauli gates (X, Y, Z)
    2. Phase gates (S, T)
    3. Hadamard gate
    4. Gate combinations
    5. Measurement and result analysis
    """
    
    # Create example instance and run
    examples = QuantumGateExamples()
    examples.run_all_examples()
