__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# bets.py was created on April 15 2021 @ 3:01 PM
# Project: nascar
import operator
from itertools import groupby
from operator import itemgetter

from beerbet import BeerBet
from entry import Entry
from files import ProcessDataFiles
from summary import Summary
from wager import MyWager

p = ProcessDataFiles()
# read all results*.txt files for 2021 and the drivers finish position
# for bets that greg and bob placed
race_results = p.read_data_files()
individual_race_results = list(filter(lambda results: not results['team_bet'], race_results))
team_race_results = list(filter(lambda results: results['team_bet'], race_results))
list_of_individual_bets = []
team_bets = []
wager = MyWager()
# go through the raw results list and sort out team from individual bets
for date, items in groupby(individual_race_results, key=itemgetter('race_date')):
    print(date)
    wager.reset()  # zero out one bet
    for player in items:
        # create either bob or gregs bet in the wager
        operator.methodcaller(player["player_name"].lower(), player)(wager)
        # if both bets have been placed create a beer bet
        if wager.enabled():
            wager.brew_some_beer()
            # list_of_individual_bets.append(wager)
            list_of_individual_bets.append(BeerBet(race_name=wager.bobs_bet['race_track'],
                                                   greg=Entry(driver_name=wager.gregs_bet['driver_name'],
                                                              finish=wager.gregs_bet['finish'],
                                                              player_name=wager.gregs_bet['player_name'],
                                                              beers=wager.gregs_bet["beers"],
                                                              car_number=wager.gregs_bet['car_number']),
                                                   bob=Entry(driver_name=wager.bobs_bet['driver_name'],
                                                             finish=wager.bobs_bet['finish'],
                                                             player_name=wager.bobs_bet['player_name'],
                                                             beers=wager.bobs_bet["beers"],
                                                             car_number=wager.bobs_bet['car_number'])))

# beers count has already been scored
betting_summary = Summary(list_of_individual_bets)
final_team = []
total_bob = 0
total_greg = 0

list_of_team_bets = []
for date, items in groupby(team_race_results, key=itemgetter('race_date')):
    # print(date)
    bobs_total_team_points = 0
    gregs_total_team_points = 0
    penske = 0
    gibbs = 0
    for i in items:
        # print('     ', i)
        if i['player_name'] == 'Bob':
            bobs_total_team_points += i['finish']  # add the finish positions up
            gibbs = bobs_total_team_points
        else:
            gregs_total_team_points += i['finish']
            penske = gregs_total_team_points
    if bobs_total_team_points > gregs_total_team_points:
        winner_name = 'Greg'
    else:
        winner_name = 'Bob'
    # list of results of all team bets one for each race and the total points for each better
    list_of_team_bets.append({'race_track': i['race_track'],
                              'bob': bobs_total_team_points,
                              'greg': gregs_total_team_points,
                              'winner': winner_name})
    # team total points for penske and gibbs
    final_team.append({'race_name': i['race_track'],
                       'Greg': gregs_total_team_points < bobs_total_team_points,
                       'Bob': gregs_total_team_points < bobs_total_team_points,
                       'Penske': penske,
                       'Gibbs': gibbs})

# count the number of times bob or greg has won
total_bob = len([t for t in list_of_team_bets if t['winner'] == 'Bob'])
total_greg = len([t for t in list_of_team_bets if t['winner'] == 'Greg'])
if total_bob > total_greg:
    total_bob = total_bob - total_greg
    total_greg = 0
else:
    total_greg = total_greg - total_bob
    total_bob = 0
team_cooler = {'Bob': total_bob, 'Greg': total_greg}
