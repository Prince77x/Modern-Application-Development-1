import email
from flask import Flask, render_template, flash, redirect, url_for
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
app = Flask(__name__)
# flask login setup


# app configuration 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "Apple123"
db.init_app(app)
with app.app_context():
    db.create_all()


# flask login setup 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#user loader 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("user verified")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credential !  try again")
            return redirect(url_for('login'))
        
    return render_template("login.html" , form=form )

# logout route 
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(" you have logout successfully ")
    return redirect(url_for('login'))


#dashboard 
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", username= current_user.username)



if __name__ == "__main__":
    app.run(debug=True)