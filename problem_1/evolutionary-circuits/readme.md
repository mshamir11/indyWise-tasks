## Problem 1

To run the code.



## Approach towards the problem

1. Create a virtual environment using conda for python 2.7
   ```bash
  conda create --name py2 python=2.7
  conda activate py2
   ```
2. Install ngspice
   ```bash
     sudo apt install ngspice
   ```
3. Install pypy
   ```bash
    sudo snap install pypy --classic
   ```
4. Run the examples
   ```bash
      pypy evolutionary/cgp.py ./examples/lowpass.py
      pypy evolutionary/cgp.py ./examples/inverter.py
      pypy evolutionary/cgp.py ./examples/nand.py
   ```
5. Results
   The simulation results can be found in the folders named lowpass,inverter and nand.