import time
from enum import Enum

class HandType(Enum):
    ONE = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE = 4
    FULL = 5
    FOUR = 6
    FIVE = 7



def p07():

    data = parse_input('input')
    print(data)

    hands = [(line.split(' ')[0], ) ]

    return 0

def parse_input(filename):
    """Parse file and return lines as alist of str"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        return []

if __name__ == "__main__":
    start_time = time.time_ns()
    p07()
    print(f"Duration : {(time.time_ns() - start_time) / 10 ** 9} s")