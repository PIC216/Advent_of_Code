"""
Contains all classes I create to solve the problems on Advent of Code 2023.
"""

import itertools
import collections


# Used in Day 7
class CamelCards:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

        cards_split = []
        for char in self.cards:
            if char.isdigit():
                cards_split.append(int(char))
            elif char == "T":
                cards_split.append(10)
            elif char == "J":
                cards_split.append(11)
            elif char == "Q":
                cards_split.append(12)
            elif char == "K":
                cards_split.append(13)
            elif char == "A":
                cards_split.append(14)
        self.cards_split = cards_split

        if len(set(self.cards_split)) == 1:
            self.type = 1
        elif len(set(self.cards_split)) == 2:
            max_num = max(collections.Counter(self.cards_split).values())
            if max_num == 4:
                self.type = 2
            else:
                self.type = 3
            pass
        elif len(set(self.cards_split)) == 3:
            max_num = max(collections.Counter(self.cards_split).values())
            if max_num == 3:
                self.type = 4
            else:
                self.type = 5
            pass
        elif len(set(self.cards_split)) == 4:
            self.type = 6
        elif len(set(self.cards_split)) == 5:
            self.type = 7

        self.part_rank = 1
        self.rank = 0
        self.win = 0


# Used in Day 7
class CamelCardsJoker:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

        cards_split = []
        for char in self.cards:
            if char.isdigit():
                cards_split.append(int(char))
            elif char == "T":
                cards_split.append(10)
            elif char == "J":
                cards_split.append(1)
            elif char == "Q":
                cards_split.append(12)
            elif char == "K":
                cards_split.append(13)
            elif char == "A":
                cards_split.append(14)
        self.cards_split = cards_split

        pre_joker_count = collections.Counter(self.cards_split)  # .values()
        joker_count = pre_joker_count[1]
        if len(pre_joker_count) == 1:
            self.post_joker_count = {x: pre_joker_count[x] for x in pre_joker_count}
        elif 1 in pre_joker_count:
            self.post_joker_count = {x: pre_joker_count[x] for x in pre_joker_count if x != 1}
            max_key = max(self.post_joker_count, key=self.post_joker_count.get)
            self.post_joker_count[max_key] += joker_count
        else:
            self.post_joker_count = {x: pre_joker_count[x] for x in pre_joker_count}

        if len(self.post_joker_count) == 1:
            self.type = 1
        elif len(self.post_joker_count) == 2:
            max_num = max(self.post_joker_count.values())
            if max_num == 4:
                self.type = 2
            else:
                self.type = 3
            pass
        elif len(self.post_joker_count) == 3:
            max_num = max(self.post_joker_count.values())
            if max_num == 3:
                self.type = 4
            else:
                self.type = 5
            pass
        elif len(self.post_joker_count) == 4:
            self.type = 6
        elif len(self.post_joker_count) == 5:
            self.type = 7

        self.part_rank = 1
        self.rank = 0
        self.win = 0


# Used in Day 7
class CamelCardsStorer:
    def __init__(self):
        self.store = {}
        self.type1 = {}
        self.type2 = {}
        self.type3 = {}
        self.type4 = {}
        self.type5 = {}
        self.type6 = {}
        self.type7 = {}
        self.all_types = [self.type1,
                          self.type2,
                          self.type3,
                          self.type4,
                          self.type5,
                          self.type6,
                          self.type7]
        self.type_total = {1: 0,
                           2: 0,
                           3: 0,
                           4: 0,
                           5: 0,
                           6: 0,
                           7: 0}

    def add_cards(self, cards, bid, normal_rules=True):
        if normal_rules:
            self.store[cards] = CamelCards(cards, bid)
        else:
            self.store[cards] = CamelCardsJoker(cards, bid)

    def sort_into_types(self):
        for card in self.store:
            if self.store[card].type == 1:
                self.type1[card] = self.store[card]
                self.type_total[1] += 1
            elif self.store[card].type == 2:
                self.type2[card] = self.store[card]
                self.type_total[2] += 1
            elif self.store[card].type == 3:
                self.type3[card] = self.store[card]
                self.type_total[3] += 1
            elif self.store[card].type == 4:
                self.type4[card] = self.store[card]
                self.type_total[4] += 1
            elif self.store[card].type == 5:
                self.type5[card] = self.store[card]
                self.type_total[5] += 1
            elif self.store[card].type == 6:
                self.type6[card] = self.store[card]
                self.type_total[6] += 1
            elif self.store[card].type == 7:
                self.type7[card] = self.store[card]
                self.type_total[7] += 1

    def get_part_rank(self):
        for card_type in self.all_types:
            for card_1, card_2 in itertools.combinations(card_type, 2):
                if card_type[card_1].cards_split[0] < card_type[card_2].cards_split[0]:
                    card_type[card_2].part_rank += 1
                elif card_type[card_1].cards_split[0] > card_type[card_2].cards_split[0]:
                    card_type[card_1].part_rank += 1
                else:
                    if card_type[card_1].cards_split[1] < card_type[card_2].cards_split[1]:
                        card_type[card_2].part_rank += 1
                    elif card_type[card_1].cards_split[1] > card_type[card_2].cards_split[1]:
                        card_type[card_1].part_rank += 1
                    else:
                        if card_type[card_1].cards_split[2] < card_type[card_2].cards_split[2]:
                            card_type[card_2].part_rank += 1
                        elif card_type[card_1].cards_split[2] > card_type[card_2].cards_split[2]:
                            card_type[card_1].part_rank += 1
                        else:
                            if card_type[card_1].cards_split[3] < card_type[card_2].cards_split[3]:
                                card_type[card_2].part_rank += 1
                            elif card_type[card_1].cards_split[3] > card_type[card_2].cards_split[3]:
                                card_type[card_1].part_rank += 1
                            else:
                                if card_type[card_1].cards_split[4] < card_type[card_2].cards_split[4]:
                                    card_type[card_2].part_rank += 1
                                elif card_type[card_1].cards_split[4] > card_type[card_2].cards_split[4]:
                                    card_type[card_1].part_rank += 1

    def get_rank(self):
        for card in self.store:
            if self.store[card].type == 7:
                self.store[card].rank = self.store[card].part_rank
            elif self.store[card].type == 6:
                self.store[card].rank = (self.store[card].part_rank +
                                         self.type_total[7])
            elif self.store[card].type == 5:
                self.store[card].rank = (self.store[card].part_rank +
                                         self.type_total[7] +
                                         self.type_total[6])
            elif self.store[card].type == 4:
                self.store[card].rank = (self.store[card].part_rank +
                                         self.type_total[7] +
                                         self.type_total[6] +
                                         self.type_total[5])
            elif self.store[card].type == 3:
                self.store[card].rank = (self.store[card].part_rank +
                                         self.type_total[7] +
                                         self.type_total[6] +
                                         self.type_total[5] +
                                         self.type_total[4])
            elif self.store[card].type == 2:
                self.store[card].rank = (self.store[card].part_rank +
                                         self.type_total[7] +
                                         self.type_total[6] +
                                         self.type_total[5] +
                                         self.type_total[4] +
                                         self.type_total[3])
            elif self.store[card].type == 1:
                self.store[card].rank = (self.store[card].part_rank +
                                         self.type_total[7] +
                                         self.type_total[6] +
                                         self.type_total[5] +
                                         self.type_total[4] +
                                         self.type_total[3] +
                                         self.type_total[2])

    def get_win(self):
        for card in self.store:
            self.store[card].win = self.store[card].bid * self.store[card].rank

    def get_total_winnings(self):
        total = 0
        for card in self.store:
            total += self.store[card].win
        return total

    def print_store(self):
        for card in self.store:
            print([self.store[card].cards,
                   self.store[card].cards_split,
                   self.store[card].bid,
                   self.store[card].type,
                   self.store[card].part_rank,
                   self.store[card].rank,
                   self.store[card].win])

    def print_joker(self, normal_rules=True):
        if normal_rules:
            print("Not applicable")
        else:
            for card in self.store:
                print([self.store[card].cards,
                       self.store[card].post_joker_count,
                       self.store[card].type])
              
