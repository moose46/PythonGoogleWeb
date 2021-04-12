__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'


# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# team.py was created on March 31 2021 @ 6:43 PM
# Project: PythonGoogleWeb

class Team:

    def __init__(self, name):
        self.name = name


class Penske(Team):
    def __init__(self, name='Penske'):
        self.name = name


class Gibbs(Team):

    def __init__(self, name='Gibbs'):
        self.name = name
