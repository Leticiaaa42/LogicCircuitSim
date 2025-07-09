# LogicCircuitSim
Simple optional activity I did for my first year of my computer science major. It's a python program that takes the text description of a logic gate circuit in a text file titled "entrada.txt" and outputs its truth table in a "saida.txt" file, both in the same folder as the .py file. The entries for the circuit should be labeled "entradas", the exits "saidas" and the list of gates "gates", with every gate being named as you please and following this format:

"NAME":["TYPE", "OUTPUT", "INPUT1", "INPUT2", etc]. 

The program suports NOT, AND, OR, NAND, NOR and XOR gates.

Example input:
C1 = {"entradas": ["A", "B", "C"], "saidas": ["Y"], "gates": ["g1", "g2", "g3"], "g1": ["nand", "y1", "A",
"B"], "g3": ["and", "Y", "B", "y1", "y2"], "g2": ["not", "y2", "C"]}
Example output:
[IN], [OUT]
['0', '0', '0'], [False]
['0', '0', '1'], [False]
['0', '1', '0'], [True]
['0', '1', '1'], [False]
['1', '0', '0'], [False]
['1', '0', '1'], [False]
['1', '1', '0'], [False]
['1', '1', '1'], [False]
