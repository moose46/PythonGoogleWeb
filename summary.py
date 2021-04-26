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
        bob_beers = len([x for x in self.list_of_bets if x.bob.beers == 1])
        bob_beers = bob_beers + len([x for x in self.list_of_bets if x.bob.beers == 2]) * 2
        greg_beers = len([x for x in self.list_of_bets if x.greg.beers == 1])
        greg_beers = greg_beers + len([x for x in self.list_of_bets if x.greg.beers == 2]) * 2

        if greg_beers > bob_beers:
            gregs_cooler = greg_beers - bob_beers
            bobs_cooler = 0
        else:
            bobs_cooler = bob_beers - greg_beers
            gregs_cooler = 0
        self.total_beers_owed = {'Bob': bobs_cooler, 'Greg': gregs_cooler}

    def beer_run(self):
        return self.total_beers_owed