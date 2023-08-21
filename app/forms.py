from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(FlaskForm):
    email =StringField('Email', validators=[DataRequired(), Email() ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[DataRequired() ])
    email = StringField('Email', validators=[DataRequired(), Email() ])
    password = PasswordField('Password', validators=[DataRequired() ])
    verify_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password') ])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    body = StringField('Make Post', validators=[DataRequired()])
    submit = SubmitField('Post')

class UserSearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired() ])
    submit = SubmitField('Search User')