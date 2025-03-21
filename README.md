# Magi Decision Network

![Magi Network Diagram](.github/magi_network.jpg)

## Overview
The Magi Decision Network is a recursive trinary decision tree system inspired by the MAGI supercomputers from Evangelion. It implements a hierarchical decision-making process where decisions are made through majority voting at each level.

## Features
- Recursive trinary decision tree structure
- Configurable network depth using levels
- Three distinct decision makers (Balthazar, Casper, Melchior)
- Majority-based decision making
- ASCII tree visualization of the decision process

## Installation
```bash
git clone <repository-url>
cd magi-network
pip install -r requirements.txt
```

## Usage
Run the program using the following command:
```bash
python src/main.py "Your query text" -l <level>
```

Arguments:
- `"Your query text"`: The input query to process
- `-l, --level`: The depth of the decision tree (default: 1)

Example:
```bash
python src/main.py "Should I deploy to production?" -l 2
```

## Architecture

### Components
1. **MagiNetwork**: The main recursive decision tree structure
   - Creates a network of depth `level`
   - Manages decision propagation through the tree
   - Implements majority voting at each node

2. **Magi**: A leaf node containing three Machina
   - Contains Balthazar, Casper, and Melchior
   - Implements majority voting among the three machines

3. **Machina**: Base decision-making units
   - **Balthazar**: First decision maker
   - **Casper**: Second decision maker
   - **Melchior**: Third decision maker

### Decision Flow
1. Query is propagated down the tree to all nodes
2. Leaf nodes (Magi) collect decisions from their three Machina
3. Non-leaf nodes collect decisions from their three child nodes
4. Decisions are aggregated upward using majority voting
5. Final decision is made at the root node

## Tree Visualization
The program generates an ASCII tree visualization showing:
- Network structure and hierarchy
- Object IDs for each component
- Decision results at each node
- Individual machine decisions

Example output:
