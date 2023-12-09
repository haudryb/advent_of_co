def puzzle3():
    """
    https://adventofcode.com/2023/day/3
    """

    print("Résolution du puzzle 2023 3 de advent of code")

    print("Récupération des données")
    
    
    data = ['467..114..','...*......','..35..633.',
            '......#...','617*......','.....+.58.','..592.....',
            '......755.','...$.*....','.664.598..']
    data = parse_input('input.txt')


    sp = find_special_char(data)
    sp_value = [data[x][y] for x,y in sp]
    include_coord = define_inclusion_area(sp)

    #scan digits in input
    dg = find_digits(data)

    vd = get_valid_digits(data, dg, include_coord)
    #id = get_invalid_digits(data, dg, include_coord)
    #print(id)
    print(vd)
    print("Part 1 result = " + str(sum(vd)))

    gear_char = find_gear_char(data)

    gear_area = define_gear_area(gear_char)

    gear_sets = find_sets(data, gear_area, dg)

    part2 = sum([x*y for (x,y) in gear_sets])
    print("Part 2 result = " + str(part2))
    return 0

def find_special_char(data):
    spec_char_coords = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if not (data[i][j] == '.' or data[i][j].isdigit() ):
                spec_char_coords.append((i, j))
                
    return spec_char_coords

def find_gear_char(data):
    gear_char_coords = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if  (data[i][j] == '*'):
                gear_char_coords.append((i, j))
                
    return gear_char_coords

def define_gear_area(gear_char):
    incl_area_offset = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    gear_area = {}
    for x,y in gear_char:
        gear_area[(x,y)] = [(x+dx,y+dy) for dx,dy in incl_area_offset]

    return gear_area
 
def define_inclusion_area(spec_char_list):
    incl_area_offset = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    include_coord =[(x0 + dx, y0 + dy) for x0,y0 in spec_char_list for dx,dy in incl_area_offset]
    
    return include_coord
        
def find_digits(data):
    digits_coord = []
    for line in data:
        is_sequence = False
        
        for j in range (len(data[0])):
            if line[j].isdigit():
                if not is_sequence:
                    #create a new index
                    digit_seq = [(data.index(line),j)]
                    is_sequence = True
                else:
                    digit_seq.append((data.index(line),j))
                    if j==(len(data[0])-1):
                        digits_coord.append(digit_seq)
            else:
                if is_sequence:
                    #store previous result
                    digits_coord.append(digit_seq)
                    is_sequence = False
    return  digits_coord   
                    
def find_sets(data, gear_area, dg):
    gears_candidates = {}
    for k,v in gear_area.items():
        gears_candidates[k] = []
        for d in dg:
            for x,y in d:
                if (x,y) in v:
                    gears_candidates[k].append(d)
                    break

    gears_coord = [valeur for valeur in gears_candidates.values() if len(valeur)==2]

    gears_values = []
    
    for gc in gears_coord:
        gear_val = []
        for g in gc:
            dec_string=''
            for x,y in g:
                dec_string =  dec_string + data[x][y]
            gear_val.append(int(dec_string))
        gears_values.append(gear_val)

    return gears_values





def get_valid_digits(data, digits_coord, include_coord):
    valid_digits = []
    valid_digits_coord = []
    for dg_coord in digits_coord:
        for coord in dg_coord:
            if coord in include_coord:
                valid_digits_coord.append(dg_coord)
                break


    for v_coord in valid_digits_coord:
        dec_string=''
        for x,y in v_coord:
            dec_string =  dec_string + data[x][y]
        valid_digits.append(int(dec_string))
    return valid_digits

def get_invalid_digits(data, digits_coord, include_coord):
    invalid_digits = []
    invalid_digits_coord = []
    for dg_coord in digits_coord:
        digitisvalid = False
        for coord in dg_coord:
            if coord in include_coord:
                digitisvalid = True
                break
        if not digitisvalid:
            invalid_digits_coord.append(dg_coord)

    for v_coord in invalid_digits_coord:
        dec_string=''
        for x,y in v_coord:
            dec_string =  dec_string + data[x][y]
        invalid_digits.append(int(dec_string))
    return invalid_digits

                              



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
    puzzle3()