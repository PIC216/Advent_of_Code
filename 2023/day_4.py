"""
My solution to Day 1 problem on Advent of Code 2023
"""

import re
from my_functions import get_numbers_from_string
from my_functions import get_num_of_wins
from my_functions import get_game_num


# Part 1
with open("advent_4_input.txt") as advent_4_input:
    total = 0
    for scratch_card in advent_4_input:
        scratch_card_details = re.split(": +", scratch_card.strip())[1]
        winning_nums = get_numbers_from_string(scratch_card_details, "w")
        chosen_nums = get_numbers_from_string(scratch_card_details, "c")
        num_of_wins = get_num_of_wins(chosen_nums, winning_nums)
        if num_of_wins == 0:
            points = 0
        else:
            points = 2 ** (num_of_wins - 1)
        total += points
    print(total)


# Part 2
with open("advent_4_input.txt") as advent_4_input:
    scratch_card_list = []
    for scratch_card in advent_4_input:
        game_num = get_game_num(scratch_card.strip())
        scratch_card_list.append(game_num)
        scratch_card_details = re.split(": +", scratch_card.strip())[1]
        winning_nums = get_numbers_from_string(scratch_card_details, "w")
        chosen_nums = get_numbers_from_string(scratch_card_details, "c")
        num_of_wins = get_num_of_wins(chosen_nums, winning_nums)
        if num_of_wins > 0:
            num_copies = scratch_card_list.count(game_num)
            scratch_card_copies = [game_num + win_num + 1 for win_num in range(num_of_wins)] * num_copies
            scratch_card_list += scratch_card_copies
    print(len(scratch_card_list))
