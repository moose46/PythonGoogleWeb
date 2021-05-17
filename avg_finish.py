__author__ = 'Robert W. Curtiss'
__project__ = 'flask-by-example'

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# avg_finish.py was created on May 12 2021 @ 9:44 AM
# Project: PythonGoogleWeb
import logging
import re
from pathlib import Path
DATE_FORMAT = '%m-%d-%Y'

data_files = Path.home() / "beerme" / "data"

if not data_files.exists():
    data_files = Path.home() / "PycharmProjects" / "Python-Google-Web" / "data"
else:
    data_files = Path.home() / "PycharmProjects" / "Python-Google-Web" / "data"

logging.basicConfig(filename='avg_log.txt', level=logging.DEBUG,filemode='w')
def clean_data(text, track):
    """Remove all tabs file the .txt file and create a list for each line"""
    txt = text.split('\n')
    clean_list = []
    keys = []

    # race_date = datetime.today().date().strftime("%m-%d-%Y")
    cnt = 0
    for d in txt:
        driver_results = d.split('\t')
        if cnt == 0:
            pos, driver, car, manufactures, laps, start, *_ = driver_results
            keys.append(pos)
            if pos == '':
                pass
            keys.append(driver)
            # keys.append('DATE')
            # keys.append('TRACK')
            # keys.append('CAR_NUMBER')
            cnt += 1
        else:
            # driver_results.append(strptime(race_date, '%m-%d-%Y'))
            driver_results.append(track)
            # clean_list.append(driver_results)

            clean_list.append(dict(zip(keys, driver_results)))
            logging.info(keys)
    return clean_list


def get_files(race_name):
    race = f'results_{race_name}*.txt'
    for f in data_files.glob(race):
        with f.open('r', encoding="utf-8") as file:
            race_date = re.findall(r'\d+-\d+-\d+', f.name)[0]  # returns a list
            logging.info(f.stem)
            text = file.read()
            data = clean_data(text, race_name)
            pass
        print(race_date)
        for d in data:
            try:
                if int(d['POS']) < 11:
                    print(d)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    race_name = input("Enter Race Name: ")
    while race_name in '':
        race_name = input("Enter Race Name: ")

    get_files(race_name)
