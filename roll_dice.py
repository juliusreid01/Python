from random import randint
# keep track of each roll
from collections import Counter

# * dice is variable for sides of dice
def roll_dice(*dice, num_trials=1_000_000):
    # initialize the counter
    counts = Counter()
    # roll num_trials each time and increment each roll
    for roll in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1

    # print the results
    print('Outcome\tProbability')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))

# alternate using a dictionary to count (collections is nice tho)
def roll_dice2(*dice, num=1000000):
    d = dict()
    
    for roll in range(num):
        r = sum((randint(1,sides) for sides in dice))
        if not r in d.keys(): d[r] = 0
        d[r] += 1

    # print the results
    print('Outcome\tProbability')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, d[outcome]*100/num))
        
roll_dice2(6)
