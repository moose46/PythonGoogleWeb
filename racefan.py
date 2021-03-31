__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'


# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# racefan.py was created on March 31 2021 @ 6:27 PM
# Project: PythonGoogleWeb
class RaceFan:

    def __init__(self, fan_name):
        self.fan_name = fan_name
        self.total_beers = 0

    def __repr__(self):
        return self.fan_name
