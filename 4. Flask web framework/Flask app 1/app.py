from flask import Flask 
app = Flask(__name__) # initializing the flask app

# routes 
@app.route('/')
def home():
    return "welcome to your first flask app"









# execution of flask app
if __name__ == "__main__":
    app.run(debub=True)