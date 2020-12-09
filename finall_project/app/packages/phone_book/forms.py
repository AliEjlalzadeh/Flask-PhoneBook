from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, StringField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(), ])
    family = StringField("family", validators=[DataRequired(), ])
    phone_number = StringField("phone number", validators=[DataRequired(), ])
    submit = SubmitField("save")