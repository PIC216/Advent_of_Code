"""
My solution to Day 1 problem on Advent of Code 2023
"""

from my_functions import first_and_last_number
from my_functions import find_word_num_and_replace
from my_functions import fix_string


# Part 1
total = 0
with open("advent_1_input.txt") as advent_1_input:
    for line in advent_1_input:
        num = first_and_last_number(line)
        total += num

print(total)


# Part 2
total = 0
with open("advent_1_input.txt") as advent_1_input:
    for line in advent_1_input:
        fixed_line = fix_string(line)
        new_line = find_word_num_and_replace(fixed_line)
        num = first_and_last_number(new_line)
        total += num

print(total)
