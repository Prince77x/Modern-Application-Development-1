from re import L
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField,EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired(),Length(min=3, max=80)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm_password",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])