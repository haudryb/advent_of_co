
class Game:

    def __init__(self,raw_game_str_def):
        self.game_id = self.get_game_id(raw_game_str_def)
        self.tirages = self.get_tirages(raw_game_str_def)

    def get_game_id(self, raw_str):
        return int(raw_str.removeprefix("Game ").split(":")[0])
    
    def get_tirages(self, raw_str):
        tirages = []
        tmp_str = raw_str.split(":")[1].split(";")
        for tir in tmp_str:
            tirage = {}
            for t in tir.split(","):
                tirage[t.split(" ")[2]] = int(t.split(" ")[1])
            tirages.append(tirage)
        return tirages
    
    def check_validity(self, sac):
        self.isValid = True
        for t in self.tirages:
            for k in t.keys():
                if (t[k] > sac[k] ):
                    self.isValid = False
                    break
            if (not self.isValid):
                break
        
        return self.isValid
    
    def compute_min(self):
        self.min_nb_of_cube = {}
        for color in['red','green','blue']:
            values = []
            for t in self.tirages:
                if color in t.keys():
                    values.append(t[color])
            self.min_nb_of_cube[color] = max(values)

    def compute_power(self):
        self.compute_min()
        power = 1
        for value in self.min_nb_of_cube.values():
            power*=value
        return power

        


def Puzzle2023_2_1():
    """Fonction qui calcule la réponse pour l'advent of code 2023 puzzle 2 partie 1 '."""
    print("Advent of code 2023 : puzzle 2")
    input = parsefile("input.txt")

    games = []
    for l in input:
        game = Game(l)
        games.append(game)

    sac = {'red': 12,'green': 13, 'blue':14}

    ctr = 0
    for g in games:
        if (g.check_validity(sac)):
            ctr+=g.game_id

    pow = sum([g.compute_power() for g in games])

    print("Résultat pour le puzzle 1: ", ctr)
    print("Résultat pour le puzzle 2: ", pow)


def parsefile(filename):
    """Fonction qui parse un fichier et renvoie une liste de lignes en tant que chaînes de caractères."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
        return []


if __name__ == "__main__":
    # Point d'entrée principal (main)
    Puzzle2023_2_1()