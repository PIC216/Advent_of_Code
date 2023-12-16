from my_functions import get_game_num_and_sets
from my_functions import update_max_in_colour_dict


# Part 1
total = 0
with open("advent_2_input.txt") as advent_2_input:
    for game in advent_2_input:
        max_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game_num, game_sets = get_game_num_and_sets(game)
        for game_set in game_sets:
            for cube_colour in game_set:
                for colour in max_cubes:
                    update_max_in_colour_dict(max_cubes, colour, cube_colour)
        if max_cubes["red"] <= 12 and max_cubes["green"] <= 13 and max_cubes["blue"] <= 14:
            total += game_num

print(total)


# Part 2
total_power = 0
with open("advent_2_input.txt") as advent_2_input:
    for game in advent_2_input:
        max_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game_num, game_sets = get_game_num_and_sets(game)
        for game_set in game_sets:
            for cube_colour in game_set:
                for colour in max_cubes:
                    update_max_in_colour_dict(max_cubes, colour, cube_colour)
        power = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]
        total_power += power

print(total_power)
