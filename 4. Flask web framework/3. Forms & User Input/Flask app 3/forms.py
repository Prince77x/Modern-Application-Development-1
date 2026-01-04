from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, equal_to

class registerform(FlaskForm):
    username= StringField("Name", validators=[DataRequired(), Length(min=3, max=30)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password= PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), equal_to('password')])
    submit = SubmitField("Register")

