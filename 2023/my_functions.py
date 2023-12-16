'''
Contains all functions I create to solve the problems on Advent of Code 2023.
'''

# Used in Day 1
def first_and_last_number(a_string: str):
    for char in a_string:
        if char.isdigit():
            first = char
            break
    for char in a_string[::-1]:
        if char.isdigit():
            last = char
            break
    first_and_last = f"{first}{last}"
    return int(first_and_last)

# Used in Day 1
def fix_string(a_string: str):
    extra_chars = {
        "oneight": "oneeight",
        "twone": "twoone",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight"
    }
    for original, fixed in extra_chars.items():
        a_string = a_string.replace(original, fixed)
    return a_string

# Used in Day 1
def find_word_num_and_replace(a_string: str):
    digits = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    for word, num in digits.items():
        a_string = a_string.replace(word, num)
    return a_string
  
