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

class Hand:
    def __init__(self, raw_str):
        self.cards = raw_str.split(' ')[0]
        self.bid = raw_str.split(' ')[1]
        self.hand_type = self.get_hand_type()

    def get_hand_type(self):
        store_count=[]
        card_checked=[]
        for card in self.cards:
            count = self.cards.count(card)
            if count == 5:
                return HandType.FIVE
            elif count == 4:
                return HandType.FOUR
            else:
                if card not in card_checked:
                    card_checked.append(card)
                    store_count.append(count)
        if 3 in store_count:
            if 2 in store_count:
                return HandType.FULL
            else:
                return HandType.THREE
        if 2 in store_count:
            if store_count.count(2) == 2:
                return HandType.TWO_PAIR
            else:
                return HandType.PAIR
            
        return HandType.ONE

def p07():

    data = parse_input('input')
    print(data)

    hands = [Hand(line) for line in data]
    


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