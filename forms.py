from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

# Форма регистрации
class RegistrationForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    birthdate = DateField("Дата рождения", validators=[DataRequired()])
    hobbies = TextAreaField("Увлечения")
    photo = FileField("Загрузить аватар")
    submit = SubmitField("Зарегистрироваться")
