__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# models.py was created on February 23 2021 @ 3:10 PM
# Project: PythonGoogleWeb

bets_data = {
    "Daytona 500": {
        "Bob": {
            'driver': 'Keselowski', 'finish': 15
        },
        "Greg": {
            'driver': 'Blaney', 'finish': 30
        }
    },
    "Daytona Road Course": {
        "Bob": {
            'driver': 'Elliot', 'finish': 21
        },
        "Greg": {
            'driver': 'Blaney', 'finish': 15
        }
    },
    "Homestead": {
        "Bob": {
            'driver': 'Hamlin', 'finish': 11
        },
        "Greg": {
            'driver': 'Blaney', 'finish': 29
        }
    },
    "Las Vegas": {
        "Bob": {
            'driver': 'Truex', 'finish': 6
        },
        "Greg": {
            'driver': 'Blaney', 'finish': 5
        }
    },
    "Phoenix": {
        "Bob": {
            'driver': 'Elliot', 'finish': 5
        },
        "Greg": {
            'driver': 'Blaney', 'finish': 10
        }
    },
    "Atlanta": {
        "Bob": {
            'driver': 'Truex', 'finish': 9
        },
        "Greg": {
            'driver': 'Blaney', 'finish': 1
        }
    }
    # ,
    # "Bristol": {
    #     "Bob": {
    #         'driver': 'Rudd', 'finish': 0
    #     },
    #     "Greg": {
    #         'driver': 'Blaney', 'finish': 0
    #     }
    # }
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


class Summary(object):

    def __init__(self, list_of_bets):
        """

        :type list_of_bets: BeerBet
        """
        self.list_of_bets = list_of_bets
        self.total_beers_owed = {}

    def update_beers(self):
        pass


bets = []
for race_name, v in bets_data.items():
    # print(f'{race_name[0]}')
    # for name, b in bet.items():
    #     print(f'{name} {b["driver"]} {b["finish"]}')
    bets.append(BeerBet(race_name=race_name,
                        greg=Entry(driver_name=v["Greg"]["driver"],
                                   finish=v["Greg"]["finish"],
                                   fan_name="Greg"),
                        bob=Entry(driver_name=v["Bob"]["driver"],
                                  finish=v["Bob"]["finish"],
                                  fan_name="Bob")))
# calculate beers
bob = 0
greg = 0
# calculate beers
bob = 0
greg = 0
for b in bets:
    results = b.the_winner()
    if results['Bob']:
        # award two beers
        if b.bob.finish == 1:
            bob += 2
        else:
            bob += 1
    elif results['Greg']:
        if b.greg.finish == 1:
            greg += 2
        else:
            greg += 1
    pass
    print(f'race={b.race_name}  b={bob} g={greg}')

if bob > greg:
    bob = bob - greg
    greg = 0
elif greg > bob:
    greg = greg - bob
    bob = 0

betting_summary = Summary(bets)
betting_summary.total_beers_owed = {'Bob': bob, 'Greg': greg}
