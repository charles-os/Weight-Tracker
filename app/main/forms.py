from  flask import FlaskForm
from .forms import  TextAreaField,SubmitField,validators

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')