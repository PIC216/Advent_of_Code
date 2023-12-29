"""
My solution to Day 5 problem on Advent of Code 2023
Note: The code for Part 2 is not optimised but does produce the correct answer.
"""

from my_functions import get_numbers_from_string
from my_functions import get_all_maps
from my_functions import map_new_num
from my_functions import get_seed_pairs_from_seed_ranges


# Part 1
with open("advent_5_input.txt") as advent_5_input:
    advent_5_input_list = advent_5_input.read().split('\n')
    seed_numbers = get_numbers_from_string(advent_5_input_list[0].split(": ")[1])
    combined_maps = get_all_maps(advent_5_input_list)

    seed_to_soil = combined_maps[0]
    soil_to_fertiliser = combined_maps[1]
    fertilizer_to_water = combined_maps[2]
    water_to_light = combined_maps[3]
    light_to_temperature = combined_maps[4]
    temperature_to_humidity = combined_maps[5]
    humidity_to_location = combined_maps[6]

    min_location_number = None
    for seed_number in seed_numbers:
        soil_num = map_new_num(seed_number, seed_to_soil)
        fertiliser_num = map_new_num(soil_num, soil_to_fertiliser)
        water_num = map_new_num(fertiliser_num, fertilizer_to_water)
        light_num = map_new_num(water_num, water_to_light)
        temperature_num = map_new_num(light_num, light_to_temperature)
        humidity_num = map_new_num(temperature_num, temperature_to_humidity)
        location_num = map_new_num(humidity_num, humidity_to_location)
        if not min_location_number:
            min_location_number = location_num
        elif location_num < min_location_number:
            min_location_number = location_num

    print(min_location_number)


# Part 2
with open("advent_5_input.txt") as advent_5_input:
    advent_5_input_list = advent_5_input.read().split('\n')
    seed_ranges = get_numbers_from_string(advent_5_input_list[0].split(": ")[1])

    combined_maps = get_all_maps(advent_5_input_list)
    seed_to_soil = combined_maps[0]
    soil_to_fertiliser = combined_maps[1]
    fertilizer_to_water = combined_maps[2]
    water_to_light = combined_maps[3]
    light_to_temperature = combined_maps[4]
    temperature_to_humidity = combined_maps[5]
    humidity_to_location = combined_maps[6]

    seed_pairs = get_seed_pairs_from_seed_ranges(seed_ranges)
    min_location_number = None
    for pair in seed_pairs:
        pair_start = pair[0]
        pair_range = pair[1]
        for i in range(pair_range):
            seed_number = pair_start + i
            soil_num = map_new_num(seed_number, seed_to_soil)
            fertiliser_num = map_new_num(soil_num, soil_to_fertiliser)
            water_num = map_new_num(fertiliser_num, fertilizer_to_water)
            light_num = map_new_num(water_num, water_to_light)
            temperature_num = map_new_num(light_num, light_to_temperature)
            humidity_num = map_new_num(temperature_num, temperature_to_humidity)
            location_num = map_new_num(humidity_num, humidity_to_location)
            if not min_location_number:
                min_location_number = location_num
            elif location_num < min_location_number:
                min_location_number = location_num
                
    print(min_location_number)
