from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


# creating a login in form.
class BELIF(FlaskForm):
    name = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("Sign In")