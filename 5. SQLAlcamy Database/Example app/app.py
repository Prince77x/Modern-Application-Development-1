from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

from models import Teacher , Student

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return "Hello prince"



if __name__ == '__main__':
    app.run(debug=True)
