import time
def p05():
    data = parseInput('input')
    #print(data)

    seeds = [int(s) for s in data[0].split(' ')[1:-1]]
    #print(seeds)

    seeds_to_soil = map_data(data,'seed-to-soil map:')
    soil_to_fertilizer = map_data(data,'soil-to-fertilizer map:')
    fertilizer_to_water = map_data(data,'fertilizer-to-water map:')
    water_to_light = map_data(data,'water-to-light map:')
    light_to_temperature = map_data(data,'light-to-temperature map:')
    temperature_to_humidity = map_data(data,'temperature-to-humidity map:')
    humidity_to_location = map_data(data,'humidity-to-location map:')

    path = [seeds_to_soil,soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location]

    locations = get_locations(seeds,path )

    part1 = min(locations)
    print("Part 1 result: " + str(part1))

    #part 2 
    
    locations = get_locations(seeds,path,part2=True)

    part2 = min([s for s,l in locations])
    print("Part 2 result: " + str(part2))
    return 0


def get_locations(seeds, path, part2 = False):
    if not part2:
        locations = []
        for seed in seeds:
            start_pos = seed
            for p in path:
                new_pos = get_position(p,start_pos)
                start_pos = new_pos
            locations.append(new_pos)
        return locations
    else:
         #for part 2 we will get only the min location for 1 set of range
         #to minimize memory consumption

        starts_seed = [sd for sd in seeds if seeds.index(sd) % 2 == 0]
        seeds_len =  [sd for sd in seeds if seeds.index(sd) % 2 == 1]
       
        seeds_coord = list(zip(starts_seed, seeds_len))

        locations = []
        for interval in seeds_coord:
            intervals_to_check = [interval]
            
            for p in path:
                result=[]
                for elt in p:
                    loc_res =  get_intervals_loc(elt,intervals_to_check)
                    result+=loc_res[1]
                    intervals_to_check = loc_res[0]
                    if intervals_to_check == []:
                        break
                intervals_to_check = result + intervals_to_check #if remainings
            locations += intervals_to_check   
        return locations
        
         

def map_data(data, start):
        return [{"dest": int(l.split(' ')[0]), 
                "source": int(l.split(' ')[1]), 
                "len": int(l.split(' ')[2])} 
                for l in data[data.index(start)+1: data.index('',data.index(start))]]

def get_position(data_map, start_position):
    
        dest_pos = -1
        for dm in data_map:
            if start_position in range(dm["source"],dm["source"] + dm["len"]):
                dest_pos = dm["dest"] + (start_position - dm["source"])
                return dest_pos
        if  dest_pos == -1 :
            return start_position
        
def get_intervals_loc(range_map, intervals):
    not_match_intervals = []
    matched_intervals = []
    source_start = range_map["source"]
    length = range_map["len"]
    source_end = source_start + length -1
    dest_start = range_map["dest"]
    dest_end = dest_start + length -1

    for s,l in intervals:
        e = s + l - 1

        if (s < source_start):
            if((e) < source_start):
                not_match_intervals.append((s,l))
            elif((e) >= source_start):
                not_match_intervals.append((s,source_start-s))
                if((e) <= (source_end)): 
                    matched_intervals.append((dest_start,e - source_start + 1))
                else:
                    matched_intervals.append((dest_start,length))
                    not_match_intervals.append((source_end + 1,e-source_end))
        else:
            if(s<=source_end):
                if(e <= source_end):
                    matched_intervals.append((dest_start + s - source_start,l))
                else:
                    not_match_intervals.append((source_end + 1, e-source_end))
                    matched_intervals.append((dest_start+s-source_start,source_end - s +1))
            else:
                not_match_intervals.append((s,l))
    return((not_match_intervals, matched_intervals))                    
                         
               



def parseInput(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

if __name__ == "__main__":
    start_time = time.time_ns()
    p05()
    print(f"Duration: {(time.time_ns() - start_time) / 10 ** 9} s")
