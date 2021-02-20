# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, Bob says hot potatoes!')  # Press Ctrl+F8 to toggle the breakpoint.
