__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# models.py was created on February 23 2021 @ 3:10 PM
# Project: PythonGoogleWeb
from beerbet import BeerBet
from bets import bets_data
from entry import Entry
from summary import Summary

bets = []
bob = 0
greg = 1
for race_name, v in bets_data.items():
    # print(f'{race_name[0]}')
    # for name, b in bet.items():
    #     print(f'{name} {b["driver"]} {b["finish"]}')
    if 'Bob' in v[0]:
        bob = 0
        greg = 1
    else:
        bob = 1
        greg = 0
    bets.append(BeerBet(race_name=race_name,
                        greg=Entry(driver_name=v[greg]["Greg"]["driver"],
                                   finish=v[greg]["Greg"]["finish"],
                                   fan_name="Greg"),
                        bob=Entry(driver_name=v[bob]["Bob"]["driver"],
                                  finish=v[bob]["Bob"]["finish"],
                                  fan_name="Bob")))
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

betting_summary = Summary(bets)
betting_summary.total_beers_owed = {'Bob': bob, 'Greg': greg}
