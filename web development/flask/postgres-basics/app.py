from flask import Flask, render_template, request, flash
from sqlalchemy import create_engine
from model.person import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:haskell@localhost/flasksql';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_string'

db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-person', methods=['POST'])
def create_person():
    name = request.form['name']
    color = request.form['color']
    db.session(Person(name, color))
    db.session.commit()
    return 'done'


if __name__ == '__main__':
    print(db)
    db.create_all()
    app.run()