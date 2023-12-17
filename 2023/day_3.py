"""
My solution to Day 1 problem on Advent of Code 2023
"""

from my_functions import get_numbers_and_symbols
from my_functions import find_all_diagonals
from my_functions import get_part_num_indices
from my_functions import find_number
from my_functions import find_all_gear_diagonals
from my_functions import get_definite_gear_nums
from my_functions import get_gear_product


# Part 1
with open("advent_3_input.txt") as advent_3_input:
    advent_3_input_list = advent_3_input.read().split('\n')
    max_row = len(advent_3_input_list)-1
    max_col = len(advent_3_input_list)-1
    number_indices, symbol_indices = get_numbers_and_symbols(advent_3_input_list)[:2]
    symbol_diagonals = find_all_diagonals(symbol_indices, max_row, max_col)
    part_num_indices = get_part_num_indices(number_indices, symbol_diagonals)
    total = 0
    for number_as_indices in part_num_indices:
        number = find_number(advent_3_input_list, number_as_indices)
        total += number
    print(total)


# Part 2
with open("advent_3_input.txt") as advent_3_input:
    advent_3_input_list = advent_3_input.read().split('\n')
    number_indices, gear_indices = get_numbers_and_symbols(advent_3_input_list)[::2]
    gear_diagonals = find_all_gear_diagonals(gear_indices, max_row, max_col)
    all_gear_nums = []
    for gear_diagonal in gear_diagonals:
        definite_gear_nums = get_definite_gear_nums(number_indices, gear_diagonal)
        all_gear_nums += definite_gear_nums
    gear_product_sum = 0
    for gear_nums_index in all_gear_nums:
        if gear_nums_index:
            gear_number_product = get_gear_product(advent_3_input_list, gear_nums_index)
        gear_product_sum += gear_number_product
    print(gear_product_sum)
