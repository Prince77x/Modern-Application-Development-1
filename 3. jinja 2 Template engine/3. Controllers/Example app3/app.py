from flask import Flask , render_template

app = Flask(__name__)

@app.route('/info')
def info():
    return render_template("./info.html" , name= "Prince",college ="IITM",club= "aryavarta sangam")

@app.route('/ifelse')
def ifelse():
    return render_template('./ifelse.html',age= 17)

@app.route('/forloop')
def forloop():
    return render_template('./for_loop.html', friends = ["Prince", "Rahul", "Amit", "Neha", "Sneha"])

@app.route('/dict')
def dict():
    return render_template('./dictionary.html', profile = {"name": "Prince", "club": "Aryavarta Sangam", "region": "Mithila"})

@app.route('/main')
def main():
    return render_template('./main.html')

if __name__ == "__main__":
    app.run(debug=True) 