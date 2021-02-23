__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# models.py was created on February 23 2021 @ 3:10 PM
# Project: PythonGoogleWeb
races = {
    1: 'Daytona 500',
    2: "Daytona Road Course",
    3: "Homestead",
    4: "Las Vagas"
}


class RaceFan:

    def __init__(self, fan_name):
        self.fan_name = fan_name

    def __repr__(self):
        return self.fan_name


class Race:
    def __init__(self, race_name):
        self.race_name = race_name

    def __repr__(self):
        return self.race_name


class Entry(Race, RaceFan):

    def __init__(self, fan_name, driver_name="None", race_name="None", finish=40):
        Race.__init__(self, race_name=race_name)
        RaceFan.__init__(self, fan_name)
        self.driver_name = driver_name
        self.finish = finish
        self.beer = False

    def __repr__(self):
        return f'Entry:{self.fan_name} {self.race_name} {self.driver_name} {self.finish} {self.beer}'


class BeerBet(Entry):
    bob: Entry
    greg: Entry

    def __init__(self, bob, greg):
        self.bob = bob
        self.greg = greg

    def the_winner(self):
        if self.greg.finish > self.bob.finish:
            self.bob.beer = True
        elif self.greg.finish < self.bob.finish:
            self.greg.beer = True

    def __repr__(self):
        return f'Bet: {self.bob.race_name}\n' \
               f'{self.bob.fan_name} {self.bob.driver_name} {self.bob.finish} {self.bob.beer}\n' \
               f'{self.greg.fan_name} {self.greg.driver_name} {self.greg.finish} {self.greg.beer}\n'


# picks = [BeerBet(greg=Entry(driver_name='Blaney', fan_name='Greg', race_name=races.get(1), finish=30),
#                  bob=Entry(driver_name='Keselowski', fan_name='Bob', race_name=races.get(1), finish=13)),
#          BeerBet(greg=Entry(driver_name='Blaney', fan_name='Greg', race_name=races.get(2), finish=15),
#                  bob=Entry(driver_name='Elliot', fan_name='Bob', race_name=races.get(2), finish=21)),
#          BeerBet(greg=Entry(fan_name='Greg', race_name=races.get(3)), bob=Entry(fan_name='Bob', race_name=races.get(3)))
#          ]
#
# sorted_races = {key: val for key, val in sorted(races.items(), key=lambda ele: [0])}
#
# # print(race1)
# for r in picks:
#     r.the_winner()
#     print(r)
