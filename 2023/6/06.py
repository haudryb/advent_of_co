import time


def p06():

    #inputs data
    races = [(49,298), (78,1185), (79,1066), (80,1181)]

    res = 1
    for race in races:
        win = len(get_winning_distances(race[1], get_travel_distances(race)))
        res *=win

    part1 = res

    print('part1 result = ' + str(part1))
    ##
    race = (49787980,298118510661181)
    win = len(get_winning_distances(race[1], get_travel_distances(race)))

    part2 = win
    print('part2 result = ' + str(part2))
    
    return 0

def get_travel_distances(race):
    total_time = race[0]
    acceleration = 1

    distances = []
    for time_push in range(total_time):
        remaining_time = total_time - time_push
        speed = time_push * acceleration
        distance = speed * remaining_time
        distances.append(distance)

    return distances

def get_winning_distances(win_distance_threshold, distances):
    return [d for d in distances if d > win_distance_threshold]


if __name__ == "__main__":
    start_time = time.time_ns()
    p06()
    print(f"Duration for brute force: {(time.time_ns() - start_time) / 10 ** 9} s")