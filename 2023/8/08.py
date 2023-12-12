import time
from enum import Enum
from math import lcm

def p08():

    data = parse_input('input')
    #print(data)

    sequence_path = data[0]
    sequence_len = len(sequence_path)

    dico_path = get_dico_path(data)

    
    steps = find_path('AAA','ZZZ', sequence_path, dico_path)
    part1 = steps

    print('Part1 result = ' + str(part1))

    steps = find_ghost_path('A','Z', sequence_path, dico_path)
    part2=lcm(*steps)
    
    print('Part2 result = ' + str(part2))
    return 0

def  find_ghost_path(start,end, sequence_path, dico_path):
    start_nodes = [key for key in dico_path.keys() if key.endswith(start)]
    sequence_len = len(sequence_path)
    step = 0
        
    all_steps=[]
    for sn in start_nodes:
        step = 0
        current_node = sn
        while not current_node.endswith(end):
            direction = sequence_path[step % sequence_len]
            if direction == 'L':
                next_node = dico_path[current_node][0]
            elif direction == 'R':
                next_node = dico_path[current_node][1]
            current_node = next_node
            step+=1
        all_steps.append(step)

    return all_steps


def  find_path(start,end, sequence_path, dico_path):
    sequence_len = len(sequence_path)
    step = 0
    current_node = start

    while current_node!=end:
        direction = sequence_path[step % sequence_len]
        if direction == 'L':
            next_node = dico_path[current_node][0]
        elif direction == 'R':
            next_node = dico_path[current_node][1]
        current_node = next_node
        step+=1

    return step



def get_dico_path(data):
    dico_path = {}
    for line in data[2:]:
        key,valeur_raw = line.split("=")
        key = key.strip()
        valeurs = tuple(v.strip().lstrip('\(') for v in valeur_raw[1:-1].split(','))   
        dico_path[key] = valeurs
    return dico_path


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
    p08()
    print(f"Duration : {(time.time_ns() - start_time) / 10 ** 9} s")