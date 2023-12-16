'''
Contains all functions I create to solve the problems on Advent of Code 2023.
'''

# Used in Day 1
def first_or_last_digit(string_with_num, first: bool = True):
    if not first:
        string_with_num = string_with_num[::-1]
    for char in string_with_num:
        if char.isdigit():
            num = char
            break
    return num
    

# Used in Day 1
def first_and_last_digit(string_with_num: str):
    first = first_or_last_digit(string_with_num, first = True)
    last = first_or_last_digit(string_with_num, first = False)
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


# Used in Day 2
def find_first_num(string_with_num):
    num = int(re.findall(r'\d+', string_with_num)[0])
    return num


# Used in Day 2
def get_game_num_and_sets(game_string):
    game_num = find_first_num(game_string.split(": ")[0])
    game_sets_ = game_string.split(": ")[1].split("; ")
    game_sets = []
    for game_set_ in game_sets_:
        game_set = game_set_.split(", ")
        game_sets.append(game_set)
    return game_num, game_sets


# Used in Day 2
def update_max_in_colour_dict(colour_dict: dict = None, colour: str = "", a_string: str = ""):
    if colour in a_string:
        num = find_first_num(a_string)
        if num > colour_dict[colour]:
            colour_dict[colour] = num
            
