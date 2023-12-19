import time

class self:
    def __init__(self, coords, value):
        self.coords = coords
        self.value = value
        self.get_neibhours()

    def get_neibhours(self):
        if self.value == '|':
            self.neigbhours = ((self.coords[0]-1, self.coords[1]),(self.coords[0]+1, self.coords[1]))
        elif self.value == '-':
            self.neigbhours = ((self.coords[0], self.coords[1]-1),(self.coords[0], self.coords[1] + 1))
        elif self.value == 'L':
            self.neigbhours = ((self.coords[0] - 1, self.coords[1]),(self.coords[0], self.coords[1] + 1))
        elif self.value == 'J':
            self.neigbhours = ((self.coords[0] - 1, self.coords[1]),(self.coords[0], self.coords[1] - 1 ))
        elif self.value == '7':
            self.neigbhours = ((self.coords[0] + 1, self.coords[1]),(self.coords[0], self.coords[1] - 1 ))        
        elif self.value == 'F':
            self.neigbhours = ((self.coords[0] + 1, self.coords[1]),(self.coords[0], self.coords[1] + 1 ))
        elif self.value == '.':
            self.neigbhours = (-1,-1)
        elif self.value == 'S':
            self.neigbhours = ((self.coords[0] - 1, self.coords[1]),(self.coords[0] + 1, self.coords[1]),(self.coords[0], self.coords[1] - 1), (self.coords[0], self.coords[1] + 1) )     


def p10():
    #example
    
    #input
    data = parse_input('input')
    
    nodes = acquire_selfs_map(data) 
    graph = generate_dic_graph(nodes)
    start_node = [n.coords for n in nodes if n.value == 'S'][0]

    #get next node
    next_node = [n for n in graph[start_node] if start_node in graph[n]][0]

    current_node = next_node
    explored = [start_node]
   
    chain_len = 1

    while not(current_node == start_node and chain_len >= 2):
        if (start_node in graph[current_node] and chain_len >=2):
            chain_len+=1
            current_node = start_node
            break
        else:
            explored.append(current_node)
            for n in graph[current_node]:
                if n not in explored:
                    current_node = n
                    chain_len +=1
                    
            
            

    part1 = chain_len // 2

    print('Part 1 result = ' + str(part1))
    ctr = 0
    for n in nodes:
        if(n.coords not in explored and tile_is_enclosed(n.coords,explored)):
           ctr += 1 

    part2 = ctr

    print('Part 2 result = ' + str(part2))

    return 0


def generate_dic_graph(nodes):
    dico_graph = {}
    for n in nodes:
        dico_graph[n.coords] = n.neigbhours
    return dico_graph

def acquire_selfs_map(data):
    nodes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            nodes.append(self((i,j),data[i][j]))
    return nodes

def tile_is_enclosed(tile_coords, loop):
    x, y = tile_coords
    inter = 0
    #find line
    line = [(x0,y0) for (x0,y0) in loop if x0 == x]
    for c in line:
        if c[1] > y:
            inter+=1

    return (inter != 0 and (inter % 2) == 1)
    



    
       

       

    # Si le nombre d'intersections est impair, le point est à l'intérieur
    return (intersections % 2 == 1)      


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
    p10()
    print(f"Duration : {(time.time_ns() - start_time) / 10 ** 9} s")