from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, BooleanField, DateTimeField
from wtforms.validators import DataRequired

from database import get_classes


class AnimalForm(FlaskForm):
    id = IntegerField(label="ID(int)", validators=[DataRequired()])
    address = StringField(label="Address the zoo", validators=[DataRequired()])
    personal = StringField(label="Name personal", validators=[DataRequired()])
    box = IntegerField(label="Number the box", validators=[DataRequired()])
    animal = SelectField(label="Type the animal",
                         choices=[(i[0], i[0]) for i in get_classes()],
                         validators=[DataRequired()])
    nickname = StringField(label="Nickname the animal",
                           validators=[DataRequired()])
    eating = DateTimeField(label="Last time eat. format='%Y-%m-%d %H:%M:%S'",
                           validators=[DataRequired()])
    certificat = StringField(label="Certificat", validators=[DataRequired()])
    chip = BooleanField(label="is chip")
    submit = SubmitField('Submit')
