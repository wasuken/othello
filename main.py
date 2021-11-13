from game import Othello
import random
import time

o = Othello(8)
hand = 1

o.put_default_stone()
o.print()

while not (o.is_finished()):
    r_hand = o.opponent_stone(hand)
    candis = o.put_ptr_candidates(hand)
    print(candis)
    if len(candis) > 0:
        cho = random.choice(candis)
        x, y = cho
        o.put_judge(x, y, hand)
    else:
        print("pass")
    o.print()
    hand = r_hand

win, wc, lc = o.who_winner()
o.count_print()
print('winner: {}, {}/{}'.format(win, wc, lc))



