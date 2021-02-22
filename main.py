# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

app = Flask(__name__)

# https://alien-gadget-305416.ue.r.appspot.com/
@app.route('/')
def index():
    # Use a breakpoint in the code line below to debug your script.
    return render_template('beer.html')
        # f'<ul>Hello Greg, Bob says: Bushhhhhhhhhhhhhhh!<ul>'  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8080, debug=True)
    app.run(debug=True)
