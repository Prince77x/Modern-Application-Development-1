from flask import Flask, request, render_template,redirect, url_for
from database import db, Student

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        student = Student(name=name, email=email, course=course)
        db.session.add(student)
        db.session.commit()
        return "student added successfully"
    
    return render_template("add.html")

@app.route("/students")
def students():
    all_students = Student.query.all()
    return render_template("students.html", students=all_students)


# DELETE Student
@app.route("/delete/<int:id>")
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("students"))



if __name__ == "__main__":
    app.run(debug=True)