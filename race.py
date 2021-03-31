__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'


# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# race.py was created on March 31 2021 @ 6:30 PM
# Project: PythonGoogleWeb
class Race:
    def __init__(self, race_name):
        self.race_name = race_name

    def __repr__(self):
        return self.race_name
