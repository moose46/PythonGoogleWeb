# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

from summary import Summary
from bets import team_cooler, betting_summary
from models import team_summary

app = Flask(__name__)


# https://alien-gadget-305416.ue.r.appspot.com/
@app.route('/')
def index():
    # pick the winners
    for r in betting_summary.list_of_individual_bets:
        r.the_winner()

    # Use a breakpoint in the code line below to debug your script.

    return render_template("beer.html", betting_summary=betting_summary, team_summary=team_summary,
                           team_cooler=team_cooler, coolers=betting_summary.total_beers_owed)


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8089, debug=True)
    app.run(host="127.0.0.1",port=8089, debug=True)
    # app.run(debug=True)
