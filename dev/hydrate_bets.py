from collections import defaultdict

individual_bets = defaultdict(list)

individual_bets['02-20-2022'] = {'Greg': 'Denny Hamlin', 'Bob': 'Brad Keselowski'}
individual_bets['02-27-2022'] = {'Greg': 'Chase Elliott', 'Bob': 'Ryan Blaney'}
individual_bets['03-06-2022'] = {'Greg': 'Ryan Blaney', 'Bob': 'Joey Logano'}
individual_bets['03-13-2022'] = {'Greg': 'Martin Truex Jr.', 'Bob': 'Christopher Bell'}
individual_bets['03-20-2022'] = {'Greg': 'Chase Elliott', 'Bob': 'Ryan Blaney'}
individual_bets['03-27-2022'] = {'Greg': 'Chase Elliott', 'Bob': 'Alex Bowman'}
individual_bets['04-04-2022'] = {'Greg': 'William Byron', 'Bob': 'Alex Bowman'}
individual_bets['04-09-2022'] = {'Greg': 'Chase Elliott', 'Bob': 'William Byron'}
individual_bets['04-17-2022'] = {'Greg': 'Ryan Blaney', 'Bob': 'Christopher Bell'}
individual_bets['04-24-2022'] = {'Greg': 'Ryan Blaney', 'Bob': 'Daniel Suarez'}
individual_bets['05-02-2022'] = {'Greg': 'Chase Elliott', 'Bob': 'Denny Hamlin'}
individual_bets['05-08-2022'] = {'Greg': 'Martin Truex Jr.', 'Bob': 'Joey Logano'}
individual_bets['05-15-2022'] = {'Greg': 'Chase Elliott', 'Bob': 'Kyle Busch'}
individual_bets['05-22-2022'] = {'Greg': 'Kyle Busch', 'Bob': 'William Byron'}
individual_bets['05-29-2022'] = {'Greg': 'Kyle Busch', 'Bob': 'Denny Hamlin'}
individual_bets['06-05-2022'] = {'Greg': 'Kyle Busch', 'Bob': 'Ryan Blaney'}
individual_bets['06-10-2022'] = {'Greg': 'Ross Chastain', 'Bob': 'Chase Elliott'}

for b in individual_bets:
    print(f'{b},Greg,{individual_bets[b]["Greg"]}')
    print(f'{b},Bob,{individual_bets[b]["Bob"]}')
