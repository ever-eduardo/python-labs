""" The very first application developed with Flask.
"""

from flask import Flask

# Creation af a Flask App instance
# It requires as argument the name of the module or package
app = Flask(__name__)


# This way is created a route or view
# A route maps a URL to a function handler in this case
# it maps the root route to the function index.
# The index function handles the request done to /
# and give some html as a response.
@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"
