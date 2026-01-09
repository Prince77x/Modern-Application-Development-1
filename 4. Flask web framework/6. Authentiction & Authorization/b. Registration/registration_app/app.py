from flask import Flask, render_template
from models import db, User
from forms import Registerform

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"]= "helloprince1"
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/register", methods=["GET","POST"])
def register():
    form = Registerform()
    if form.validate_on_submit():
        return "validation succesful"
    
    return render_template("./register.html", form=form)





if __name__ == "__main__":
    app.run(debug=True)