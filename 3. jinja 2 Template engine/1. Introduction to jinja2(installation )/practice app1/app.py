from flask import Flask , render_template

app = Flask(__name__)

@app.route('/info')
def info():
    return render_template("./info.html" , name= "Prince",college ="IITM",club= "aryavarta sangam")

@app.route('/header')
def header():
    return render_template("./header.html" , name="Prince")

if __name__ == "__main__":
    app.run(debug=True) 