__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# models.py was created on February 23 2021 @ 3:10 PM
# Project: PythonGoogleWeb
from beerbet import BeerBet
from bets import list_of_individual_bets
from entry import Entry
from summary import Summary

from bets import final_team
cnt = len(final_team)
team_summary = final_team
