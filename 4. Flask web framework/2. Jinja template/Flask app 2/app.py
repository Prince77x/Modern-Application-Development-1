from flask import Flask, render_template
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return "welcome to the landing page"

@app.route('/subjects')
def subjects():
    subject = ['math','hindi','cs', 'ME'] 
    return render_template('./subject looping.html' , subjects = subject)
 



if __name__ =="__main__":
    app.run(debug=True)