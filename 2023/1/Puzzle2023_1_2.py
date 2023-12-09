dec_txt_list = ["zero", 
                "one", 
                "two", 
                "three", 
                "four", 
                "five", 
                "six", 
                "seven",
                "eight", 
                "nine"]

def Puzzle2023_1_2():
    """Fonction qui affiche 'Hello, World!'."""
    print("Advent of code 2023 : puzzle 1")
    print("==============================")

    print("Starting resolution")
    print("Parsing file input.txt")
    input = parse_file("input.txt")
    print("Replace textual digit")
    filtered_input  = filter_input(input)

    print("Extract digits for each line")
    digits = findDigits(filtered_input)
    print("Concatenate first and last digits for each line")
    dec_list = concat_first_and_last_digits(digits)

    print("Resultat pour Puzzle 1 : ", sum(dec_list))



def parse_file(filename):
    """Fonction qui parse un fichier et renvoie une liste de lignes en tant que chaînes de caractères."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        return []
    
def findDigits(input):
    digits = []
    for l in input:
        digits.append([char for char in list(l) if char.isdecimal()])
    return digits

def concat_first_and_last_digits(digits):
    dec_list = []
    for d in digits:
        dec_list.append(int(d[0] + d[-1]))

    return dec_list

def filter_input(input):
    converted_input = []
    for l in input:
        conv_line = l[:]    
        for nb in dec_txt_list:           
            conv_line = conv_line.replace(nb, nb[0] + str(dec_txt_list.index(nb)) + nb[-1])
        converted_input.append(conv_line)
    return converted_input

if __name__ == "__main__":
    # Point d'entrée principal (main)
    Puzzle2023_1_2()