# Quantum Gates: Pauli, Phase & Hadamard

A comprehensive learning repository featuring interactive visualizations and practical examples of fundamental quantum gates using **IBM Qiskit** and **AWS Amazon Braket**.

## Features

### Premium HTML Visualization (`index.html`)
An interactive web-based visualization tool with:
- **Tab-based interface** for easy gate switching
- **Mathematical notation** with proper quantum mechanics symbols
- **Quantum circuit diagrams** for each gate
- **Code examples** for both Qiskit and Amazon Braket
- **Comparison table** showing gate properties
- **Beautiful CSS styling** with gradients and responsive design
- **JavaScript interactivity** for smooth tab switching

### Qiskit Examples (`qiskit_examples.py`)
Comprehensive Python examples using IBM Qiskit:
- **Pauli-X Gate**: Bit flip operation
- **Pauli-Y Gate**: Complex state transformation
- **Pauli-Z Gate**: Phase flip with superposition
- **Phase (S) Gate**: S-gate manipulation
- **T Gate**: pi/8 rotation gate
- **Hadamard Gate**: Superposition creation
- **Double Hadamard**: H x H = I property
- **Complex Circuits**: Multi-gate combinations

### Amazon Braket Examples (`braket_examples.py`)
Practical examples using AWS Amazon Braket:
- Same gate examples as Qiskit
- **Local Simulator**: Test without AWS
- **AWS Device Support**: Real quantum hardware
- Counter-based measurement analysis

## Quick Start

### Option 1: Interactive Web Visualization
1. Open `index.html` in your browser
2. Click tabs to explore gates
3. View circuit diagrams and code

### Option 2: Qiskit
```bash
pip install qiskit qiskit-aer matplotlib numpy
python qiskit_examples.py
```

### Option 3: Amazon Braket
```bash
pip install amazon-braket-sdk
python braket_examples.py
```

## Quantum Gates Overview

### Pauli-X (NOT Gate)
Flips qubit state: |0> -> |1>, |1> -> |0>

### Pauli-Y
Complex flip: |0> -> i|1>, |1> -> -i|0>

### Pauli-Z
Phase flip: |0> -> |0>, |1> -> -|1>

### Phase (S) Gate
|0> -> |0>, |1> -> i|1> (90 degree rotation)

### T Gate
|0> -> |0>, |1> -> e^(i*pi/4)|1> (45 degree rotation)

### Hadamard Gate
Creates superposition: |0> -> (|0>+|1>)/sqrt(2)

## File Structure

```
puli_phase_hadamard_gates/
├── README.md (This file)
├── index.html (Interactive visualization)
├── qiskit_examples.py (IBM Qiskit implementation)
└── braket_examples.py (AWS Amazon Braket implementation)
```

## Requirements

### Web Visualization
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No installation needed!

### Qiskit
- Python 3.7+
- Qiskit, Qiskit AER, NumPy, Matplotlib

### Amazon Braket
- Python 3.7+
- Amazon Braket SDK

## Learning Outcomes

After using this repository, you will understand:

1. How quantum gates manipulate quantum states
2. Mathematical representation of quantum gates
3. How to implement quantum circuits
4. Different types of quantum gates
5. Practical quantum computing
6. Measurement and state collapse

## Key Concepts

- |0>: Quantum state 0
- |1>: Quantum state 1
- sqrt(2): Square root of 2
- i: Imaginary unit
- ->: State transformation
- x: Gate combination

## Getting Started for Beginners

1. **Start with**: Open `index.html` - no installation!
2. **Explore**: Click gate tabs and read explanations
3. **Learn code**: View code examples
4. **Practice**: Run Python examples
5. **Experiment**: Modify code

## Technologies Used

- **IBM Qiskit**: Open-source quantum framework
- **AWS Amazon Braket**: Cloud quantum computing
- **HTML5/CSS3**: Web visualization
- **JavaScript**: Interactivity
- **Python**: Examples

## References

- IBM Qiskit: https://qiskit.org/documentation/
- AWS Amazon Braket: https://aws.amazon.com/braket/
- Quantum Computing: https://en.wikipedia.org/wiki/Quantum_computing
- Quantum Gates: https://en.wikipedia.org/wiki/Quantum_gate

## Contributing

Feel free to:
- Report issues
- Suggest improvements
- Add more examples
- Improve documentation

## License

Educational repository for learning purposes.

---

**Created for Quantum Computing Enthusiasts and Students**

Happy quantum computing!
