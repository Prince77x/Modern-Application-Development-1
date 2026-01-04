from flask import Flask, render_template, request, url_for 
app = Flask(__name__)

# routes
@app.route('/')
def index():
    return "Welcome to your flask app"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "data submited successfully"
    
    return render_template('./login.html')



# -- main execution of flask app --
if __name__ == "__main__":
    app.run(debug=True)