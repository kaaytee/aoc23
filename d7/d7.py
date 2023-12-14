from enum import Enum
from functools import cmp_to_key

hand_type = Enum('handT', ["Five", "Four", "Full", "Three", "TwoP", "OneP", "High"])

val = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
val2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def sol(file) -> int:
    stuff = []
    with open(file, 'r') as f:
        for l in f:
            hand, bet = l.split()
            hand_t = get_hand(hand)
            stuff.append((hand_t, hand, bet))
    total = sorted(stuff, key=cmp_to_key(comp))
    total.reverse()
    ans = 0
    for i in range(0, len(total)):
        hand = list(total[i])
        ans += (i + 1) * int(hand[2])
    print(f"part 1 {ans}")

def comp(h1, h2):
    h1_t, h1_h, h1_b = h1
    h2_t, h2_h, h2_b = h2
    
    if h1_t.value < h2_t.value:
        return -1
    elif h1_t.value > h2_t.value:
        return 1
    elif h1_t.value == h2_t.value:
        for i in range(0, len(h1_h)):
            if val.index(h1_h[i]) < val.index(h2_h[i]):
                return -1
            elif val.index(h1_h[i]) > val.index(h2_h[i]):
                return 1

def get_hand(card):
    d = {}
    for i, j in enumerate(card):
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1

    pairs = 0
    trips = 0
    for i in d:
        if d[i] == 2:
            pairs += 1
        elif d[i] == 3:
            trips += 1
        elif d[i] == 5:
            return hand_type.Five
        elif d[i] == 4:
            return hand_type.Four
        
    if trips == 1:
        if pairs == 1:
            return hand_type.Full
        return hand_type.Three
    elif pairs == 2:
        return hand_type.TwoP
    elif pairs == 1:
        return hand_type.OneP
    else: 
        return hand_type.High
       
def sol2(file:str) -> int:
    stuff = []
    with open(file, 'r') as f:
        for l in f:
            hand, bet = l.split()
            hand_t = get_hand2(hand)
            stuff.append((hand_t, hand, bet))
    total = sorted(stuff, key=cmp_to_key(comp2))
    total.reverse()
    
    ans = 0
    for i in range(0, len(total)):
        hand = list(total[i])
        ans += (i + 1) * int(hand[2])
    print(f"part 2 {ans}")

def comp2(h1, h2):
    h1_t, h1_h, h1_b = h1
    h2_t, h2_h, h2_b = h2
    
    if h1_t.value < h2_t.value:
        return -1
    elif h1_t.value > h2_t.value:
        return 1
    elif h1_t.value == h2_t.value:
        for i in range(0, len(h1_h)):
            if val2.index(h1_h[i]) < val2.index(h2_h[i]):
                return -1
            elif val2.index(h1_h[i]) > val2.index(h2_h[i]):
                return 1




def get_hand2(card):
    d = {}    
    jnums = card.count('J')
    if jnums == 5:
        return hand_type.Five
    
    for i, j in enumerate(card):
        if j == 'J':
            continue
        elif j not in d:
            d[j] = 1 
        else:
            d[j] += 1

    pairs = 0
    trips = 0
    for i in d:
        if i == 'J':
            continue
        
        if d[i] == 2:
            pairs += 1
        elif d[i] == 3:
            trips += 1
            
    cmax = max(d, key=d.get)
    
    if d[cmax] + jnums == 5:
        return hand_type.Five
    elif d[cmax] + jnums == 4:
        return hand_type.Four
    elif d[cmax] + jnums == 3:
        if d[min(d, key=d.get)] == 2:
            return hand_type.Full
        else: 
            return hand_type.Three
    elif pairs == 1 and jnums > 0 or pairs == 2:
        return hand_type.TwoP
    elif pairs == 1 and jnums == 0 or d[cmax] + jnums == 2:
        return hand_type.OneP
    else: 
        return hand_type.High

sol('input2.txt')
sol2('input2.txt')