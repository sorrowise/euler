# time cost = 45.4 ms ± 93.5 µs

class Card:
    def __init__(self,vs):
        d = {'T':10,'J':11,'Q':12,'K':13,'A':14}
        self.s = vs[1]        
        if vs[0] not in set('TJQKA'):
            self.v = int(vs[0])
        else:
            self.v = d[vs[0]]
        
class Hand:
    def __init__(self,cards):
        self.values = [x.v for x in cards]
        self.suits = [x.s for x in cards]
        self.value_counter = Counter(self.values).most_common()
        self.suit_kind = len(set(self.suits))
        self.ranks = sorted([x.v for x in cards],reverse=True)
        self.diff = [self.ranks[:-1][i]-self.ranks[1:][i] for i in range(4)]
    
    def categories(self):
        if self.suit_kind == 1 and set(self.diff) == {1}:
            return ('Straight Flush',9)
        elif self.suit_kind == 1:
            return ('Flush',6)
        elif set(self.diff) == {1}:
            return ('Straight',5)
        elif self.value_counter[0][1] == 4:
            return ('Four of a Kind',8)
        elif self.value_counter[0][1] == 3 and self.value_counter[1][1] == 2:
            return ('Full House',7)
        elif self.value_counter[0][1] == 3 and self.value_counter[1][1] == 1:
            return ('Three of a Kind',4)
        elif self.value_counter[0][1] == 2 and self.value_counter[1][1] == 2:
            return ('Two Pairs',3)
        elif len(self.value_counter) == 4 and self.value_counter[0][1] == 2:
            return ('One Pair',2)
        else:
            return ('High Card',1)
    
    def is_winner(self,hand):
        if self.categories()[1] > hand.categories()[1]:
            return True
        elif self.categories()[1] < hand.categories()[1]:
            return False
        elif self.categories()[1] in [8,7,4,3,2]:
            return self.value_counter > hand.value_counter
        else:
            return self.ranks > hand.ranks

def main():
    count = 0
    with open('data/ep54.txt') as f:
        hands = [line.split() for line in f]
    for hand in hands:
        p1_cards = [Card(x) for x in hand[:5]]
        p2_cards = [Card(x) for x in hand[5:]]
        p1_hand,p2_hand = Hand(p1_cards),Hand(p2_cards)
        if p1_hand.is_winner(p2_hand):
            count += 1
    return count
