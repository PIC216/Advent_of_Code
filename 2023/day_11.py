"""
My solution to Day 11 problem on Advent of Code 2023
"""

import itertools
from my_functions import add_space_row
from my_functions import add_space_col
from my_functions import get_galaxy_coords
from my_functions import distance_between_galaxies
from my_functions import get_extra_rows
from my_functions import get_extra_cols
from my_functions import distance_between_bigger_galaxies


# Part 1
with open("advent_11_input.txt") as advent_11_input:
    space_map = [[val for val in row if val != "\n"] for row in advent_11_input]
    space_map = add_space_row(space_map)
    space_map = add_space_col(space_map)
    galaxy_coords = get_galaxy_coords(space_map)
    sum_of_shortest_paths = 0
    for galaxy_1, galaxy_2 in itertools.combinations(galaxy_coords, 2):
        distance = distance_between_galaxies(galaxy_1, galaxy_2)
        sum_of_shortest_paths += distance
    print(sum_of_shortest_paths)


# Part 2
with open("advent_11_input.txt") as advent_11_input:
    space_map = [[val for val in row if val != "\n"] for row in advent_11_input]
    extra_rows = get_extra_rows(space_map)
    extra_cols = get_extra_cols(space_map)
    galaxy_coords = get_galaxy_coords(space_map)
    sum_of_shortest_paths = 0
    x_times_larger = 1_000_000
    for galaxy_1, galaxy_2 in itertools.combinations(galaxy_coords, 2):
        distance = distance_between_bigger_galaxies(galaxy_1, galaxy_2, extra_rows, extra_cols, x_times_larger)
        sum_of_shortest_paths += distance
    print(sum_of_shortest_paths)
