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
    4: "Las Vegas",
    5: "Phoenix",
    6: "Atlanta",
    7: "Bristol"
}


class RaceFan:

    def __init__(self, fan_name):
        self.fan_name = fan_name
        self.total_beers = 0

    def __repr__(self):
        return self.fan_name


class Race:
    def __init__(self, race_name):
        self.race_name = race_name

    def __repr__(self):
        return self.race_name


class Entry(RaceFan):

    def __init__(self, fan_name, finish=0, driver_name=""):
        RaceFan.__init__(self, fan_name)
        self.driver_name = driver_name
        self.finish = finish
        self.beer = False

    def __repr__(self):
        return f'Entry:{self.fan_name} {self.race_name} {self.driver_name} {self.finish} {self.beer}'


class BeerBet(Race, Entry):
    bob: Entry
    greg: Entry

    def __init__(self, bob, greg, race_name):
        super().__init__(race_name=race_name)
        self.bob = bob
        self.greg = greg
        self.race_name = race_name

    def the_winner(self):
        if self.greg.finish > self.bob.finish:
            self.bob.beer = True
        elif self.greg.finish < self.bob.finish:
            self.greg.beer = True

        return {"Bob": self.bob.beer, "Greg": self.greg.beer}

    def __repr__(self):
        return f'Bet: {self.race_name}\n' \
               f'{self.bob.fan_name} {self.bob.driver_name} {self.bob.finish} {self.bob.beer}\n' \
               f'{self.greg.fan_name} {self.greg.driver_name} {self.greg.finish} {self.greg.beer}\n'


class Summary(object):

    def __init__(self, list_of_bets):
        """

        :type list_of_bets: BeerBet
        """
        self.list_of_bets = list_of_bets
        self.total_beers_owed = {}

    def update_beers(self):
        pass


bets = [BeerBet(race_name=races.get(1),
                greg=Entry(driver_name='Blaney', fan_name='Greg', finish=30),
                bob=Entry(driver_name='Keselowski', fan_name='Bob', finish=13)),
        BeerBet(race_name=races.get(2),
                greg=Entry(driver_name='Blaney', fan_name='Greg', finish=15),
                bob=Entry(driver_name='Elliot', fan_name='Bob', finish=21)),
        BeerBet(race_name=races.get(3),
                greg=Entry(fan_name='Greg'),
                bob=Entry(fan_name='Bob')),
        BeerBet(race_name=races.get(4),
                greg=Entry(fan_name='Greg'),
                bob=Entry(fan_name='Bob')),
        BeerBet(race_name=races.get(5),
                greg=Entry(fan_name='Greg'),
                bob=Entry(fan_name='Bob')),
        BeerBet(race_name=races.get(6),
                greg=Entry(fan_name='Greg'),
                bob=Entry(fan_name='Bob'))
        ]

# calculate beers
bob = 0
greg = 0
for b in bets:
    results = b.the_winner()
    if results['Bob']:
        bob += 1
    if results['Greg']:
        greg += 1
    pass

if greg > bob:
    greg = greg - bob
    bob -= 1
elif bob > greg:
    bob = bob - greg
    greg -= 1
else:
    bob = 0
    greg = 0

betting_summary = Summary(bets)
betting_summary.total_beers_owed = {'Bob': bob, 'Greg': greg}
