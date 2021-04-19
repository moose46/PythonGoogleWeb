__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# entry.py was created on March 31 2021 @ 6:32 PM
# Project: PythonGoogleWeb
from racefan import RaceFan


class Entry(RaceFan):

    def __init__(self, fan_name, finish=0, driver_name="", beers=0):
        RaceFan.__init__(self, fan_name)
        self.driver_name = driver_name
        self.finish = finish
        self.beers = 0

    def __repr__(self):
        return f'Entry:{self.fan_name} {self.race_name} {self.driver_name} {self.finish} {self.beer}'

