"""
My solution to Day 7 problem on Advent of Code 2023
"""

from my_classes import CamelCardsStorer


# Part 1
with open("advent_7_input.txt") as advent_7_input:
    camel_card_part_1 = CamelCardsStorer()

    for hands in advent_7_input:
        cards, bid = hands.split(" ")
        camel_card_part_1.add_cards(cards, int(bid))

    camel_card_part_1.sort_into_types()
    camel_card_part_1.get_part_rank()
    camel_card_part_1.get_rank()
    camel_card_part_1.get_win()
    winnings_part_1 = camel_card_part_1.get_total_winnings()
    print(winnings_part_1)


# Part 2
with open("advent_7_input.txt") as advent_7_input:
    camel_card_part_2 = CamelCardsStorer()

    for hands in advent_7_input:
        cards, bid = hands.split(" ")
        camel_card_part_2.add_cards(cards, int(bid), False)

    camel_card_part_2.sort_into_types()
    camel_card_part_2.get_part_rank()
    camel_card_part_2.get_rank()
    camel_card_part_2.get_win()
    winnings_part_2 = camel_card_part_2.get_total_winnings()
    print(winnings_part_2)
  
