__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# models.py was created on February 23 2021 @ 3:10 PM
# Project: PythonGoogleWeb
from beerbet import BeerBet
from bets import bets
from entry import Entry
from summary import Summary

from bets import final_team
# calculate beers
bob = 0
greg = 0
for b in bets:
    results = b.the_winner()
    if results['Bob']:
        # award two beers
        if b.bob.finish == 1:
            bob += 2
        else:
            bob += 1
    elif results['Greg']:
        if b.greg.finish == 1:
            greg += 2
        else:
            greg += 1
    pass
    print(f'race={b.race_name}  b={bob} g={greg}')

if bob > greg:
    bob = bob - greg
    greg = 0
elif greg > bob:
    greg = greg - bob
    bob = 0
else:
    bob = 0
    greg = 0

betting_summary = Summary(bets)
betting_summary.total_beers_owed = {'Bob': bob, 'Greg': greg}
cnt = len(final_team)
team_summary = final_team
pass