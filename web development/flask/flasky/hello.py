""" The very first application developed with Flask.
"""

from flask import Flask

# Creation af a Flask App instance
# It requires as argument the name of the module or package
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"
