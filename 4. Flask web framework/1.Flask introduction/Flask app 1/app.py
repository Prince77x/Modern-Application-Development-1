from flask import Flask,render_template, request
app = Flask(__name__) # initializing the flask app

# routes 
@app.route('/')
def home():
    return "welcome to your first flask app"

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":            # request.args is used to read data from url if the method is GET
        username = request.form["username"] # request.form is used to read data from url if the method is POST 
        pswd = request.form["pswd"]
        print(f"{username} , {pswd}")
        print(request.method) # request.method will print the method name what we are using 
        return f'Your name is :{username} and password is : {pswd}' 
        #return render_template('./home.html')
        

    return render_template('./register.html')









# execution of flask app
if __name__ == "__main__":
    app.run(debug=True)