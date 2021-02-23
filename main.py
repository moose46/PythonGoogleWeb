# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template
from models import BeerBet, Race, RaceFan, Entry, races

app = Flask(__name__)


# https://alien-gadget-305416.ue.r.appspot.com/
@app.route('/')
def index():
    bets \
        = [BeerBet(greg=Entry(driver_name='Blaney', fan_name='Greg', race_name=races.get(1), finish=30),
                   bob=Entry(driver_name='Keselowski', fan_name='Bob', race_name=races.get(1), finish=13)),
           BeerBet(greg=Entry(driver_name='Blaney', fan_name='Greg', race_name=races.get(2), finish=15),
                   bob=Entry(driver_name='Elliot', fan_name='Bob', race_name=races.get(2), finish=21)),
           BeerBet(greg=Entry(fan_name='Greg', race_name=races.get(3)),
                   bob=Entry(fan_name='Bob', race_name=races.get(3)))
           ]
    # pick the winners
    for r in bets:
        r.the_winner()
    # Use a breakpoint in the code line below to debug your script.
    return render_template('beer.html', bets=bets)


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8080, debug=True)
    app.run(debug=True)
