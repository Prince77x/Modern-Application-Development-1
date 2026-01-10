from flask import Flask, render_template,flash
from models import db, User
from forms import Registerform
from werkzeug.security import generate_password_hash

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
        password_hash = generate_password_hash(form.password.data)
        username = form.username.data
        email = form.email.data

        existed_email = User.query.filter_by(email=email).first()
        if existed_email:
            return flash("Accout already existed")
        
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return "You have successfull registered"
    return render_template("./register.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)