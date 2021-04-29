__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# entry.py was created on March 31 2021 @ 6:32 PM
# Project: PythonGoogleWeb
from racefan import RaceFan


class Entry(RaceFan):

    def __init__(self, player_name, finish=0, driver_name="", beers=0, car_number=99):
        RaceFan.__init__(self, player_name)
        self.driver_name = driver_name
        self.finish = finish
        self.beers = beers
        self.car_number = car_number

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'Entry:{self.fan_name} {self.race_name} {self.driver_name} {self.finish} {self.beer}'
