__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'


# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# summary.py was created on March 31 2021 @ 6:39 PM
# Project: PythonGoogleWeb
class Summary(object):

    def __init__(self, list_of_bets):
        """

        :type list_of_bets: BeerBet
        """
        self.list_of_bets = list_of_bets
        self.total_beers_owed = {}

    def update_beers(self):
        pass
