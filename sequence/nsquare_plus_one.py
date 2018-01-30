"""Generate the sequence
2 5 10 17 26 .....
"""

def find_sequence(no_of_element):
    """This function takes no_of_element to print in the sequence
    
    Arg: no_of_element as integer
    
    returns: list with sequence n^2 + 1 where n is natural no 1,2,3, ... n 
    """

    sequence = []
    for n in range(1, no_of_element+1):
        sequence.append(n**2+1)
    return sequence


