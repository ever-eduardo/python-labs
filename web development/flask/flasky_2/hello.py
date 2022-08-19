from flask import Flask

# Create a Flask App instance
app = Flask(__name__)


# Add a route handler to the root path /
@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"


# Add a dynamic route handler to path /user/<name>
@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"
