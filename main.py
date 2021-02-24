# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template
from models import BeerBet, Race, RaceFan, Entry, races, betting_summary

app = Flask(__name__)


# https://alien-gadget-305416.ue.r.appspot.com/
@app.route('/')
def index():
    # pick the winners
    for r in betting_summary.list_of_bets:
        r.the_winner()


    # Use a breakpoint in the code line below to debug your script.

    return render_template('beer.html', betting_summary=betting_summary)


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8080, debug=True)
    app.run(debug=True)
