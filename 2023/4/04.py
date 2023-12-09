import re
def p04():
    """
    https://adventofcode.com/2023/day/4
    """

    print("Résolution du puzzle 2023 4 de advent of code")

    print("Récupération des données")
    data = parse_input('input.txt')
    result = 0
    for line in data:
        card = int(re.findall('(\d+)(?=:)',line)[0])
        winning_numbers = [int(res) for res in re.findall('\d+',str(re.findall('(?<=:)\s*([^|]+)',line)))] 
        own_numbers = [int(res) for res in re.findall('\d+',str(re.findall('\|\s*([\d\s]+)',line)))]
        ctr = 0
        for on in own_numbers:
            if on in winning_numbers:
                ctr += 1
        if (ctr != 0):
            result += (2 ** (ctr-1))
        #print(card)
        #print(winning_numbers)
        #print(own_numbers)
    part1 = result
    print("Part 1 result = " + str(part1))
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
     p04()