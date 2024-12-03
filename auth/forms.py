from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from ..models import Employee


class RegistrationForm(FlaskForm):
    email = StringField(
        'Email Address',
        validators=[
            Email(message="Enter a valid email address."),
            DataRequired(message="Email is required."),
        ]
    )
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Username is required."),
            Length(min=3, max=20, message="Username must be between 3 and 20 characters.")
        ]
    )
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(message="First name is required."),
            Length(max=50, message="First name cannot exceed 50 characters.")
        ]
    )
    last_name = StringField(
        'Last Name',
        validators=[
            DataRequired(message="Last name is required."),
            Length(max=50, message="Last name cannot exceed 50 characters.")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, message="Password must be at least 8 characters long."),
            EqualTo('confirm_password', message="Passwords must match."),
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(message="Please confirm your password.")]
    )
    submit = SubmitField('Register')

    def validate_email(self, field):
        """Check if the email is already registered."""
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        """Check if the username is already taken."""
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Enter a valid email address."),
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Password is required.")]
    )
    submit = SubmitField('Log In')
