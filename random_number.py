from projectq.ops import  H, Measure
from projectq import MainEngine

"""
This Function creates a new qubit,
applies a Hadamard gate to put it in superposition,
and then measures the qubit to get a random
1 or 0. 
 
"""
def get_random_number(quantum_engine):
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    random_number = int(qubit)
    return random_number


def main():
    # This list is used to store our random numbers
    random_numbers_list = []
    # for loop to generate 10 random numbers
    for i in range(10):
        # initialises a new quantum backend
        quantum_engine = MainEngine()
        # calling the ranom number function and append the return to the list
        random_numbers_list.append(get_random_number(quantum_engine))
    # Flushes the quantum engine from memory
    quantuapt m_engine.flush()
    print('Random numbers', random_numbers_list)

if __name__ == '__main__':
    main()