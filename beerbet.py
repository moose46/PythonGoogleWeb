__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# beerbet.py was created on March 31 2021 @ 6:34 PM
# Project: PythonGoogleWeb
from entry import Entry
from race import Race


class BeerBet(Race, Entry):
    bob: Entry
    greg: Entry

    def __init__(self, bob, greg, race_name):
        super().__init__(race_name=race_name)
        self.bob = bob
        self.greg = greg
        self.race_name = race_name

    def the_winner(self):
        self.bob.beer = False
        self.greg.beer = False
        if self.greg.finish > self.bob.finish:
            self.bob.beer = True
        elif self.greg.finish < self.bob.finish:
            self.greg.beer = True

        return {"Bob": self.bob.beer, "Greg": self.greg.beer}

    def __repr__(self):
        return f'Bet: {self.race_name}\n' \
               f'{self.bob.fan_name} {self.bob.driver_name} {self.bob.finish} {self.bob.beer}\n' \
               f'{self.greg.fan_name} {self.greg.driver_name} {self.greg.finish} {self.greg.beer}\n'
