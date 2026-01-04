from flask import Flask, render_template, request, url_for 
from forms import registerform
app = Flask(__name__)

# app configuration
app.config["SECRET_KEY"] = "secret123"

# routes
@app.route('/')
def index():
    return "Welcome to your flask app"

@app.route('/register',methods=['GET','POST'])
def register():
    form = registerform()

    if form.validate_on_submit():
        name = request.form.get('username')
        print(name)
        return "registration successful"
    
    return render_template('./register.html', form = form)


#Write a Flask route that handles both GET and POST for a login form.
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('pswd')
        return f'you are {user} with password {password}'
    
    return render_template('./login.html')



# -- main execution of flask app --
if __name__ == "__main__":
    app.run(debug=True)