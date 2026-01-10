from flask import Flask, render_template, flash, redirect
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
app = Flask(__name__)

# app configuration 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "Apple123"
db.init_app(app)
with app.app_context():
    db.create_all()

# routes
@app.route("/")
def home():
    return render_template("./home.html")

# registration route 
@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # talking information from forms register
        user = form.username.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)
        # checking already have account or not 
        existed_user = User.query.filter_by(email=email).first()
        if existed_user:
            flash("Account Already existed")
            return redirect("./login.html")
        
        # updating new user 
        new_users = User(username=user, email=email, password_hash=password_hash)
        db.session.add(new_users)
        db.session.commit()

        return "user added successfully"
    
    return render_template("./register.html", form=form)

# login route 



if __name__ == "__main__":
    app.run(debug=True)