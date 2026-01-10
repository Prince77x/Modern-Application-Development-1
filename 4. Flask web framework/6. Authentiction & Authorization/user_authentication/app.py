from flask import Flask, render_template 
from models import db, User
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "Apple123"
db.init_app(app)
with app.app_context():
    db.create_all()


# routes
@app.route("/")
def home():
    return render_template("./home.html")


if __name__ == "__main__":
    app.run(debug=True)