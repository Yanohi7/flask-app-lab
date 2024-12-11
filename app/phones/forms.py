from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.phones.models import Category

class PhoneForm(FlaskForm):
    name = StringField('Назва телефону', validators=[DataRequired()])
    description = TextAreaField('Опис', validators=[DataRequired()])
    price = FloatField('Ціна', validators=[DataRequired()])
    category = SelectField('Категорія', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Зберегти')

    # Метод для завантаження категорій з БД
    def load_categories(self):
        self.category.choices = [(c.id, c.category_name) for c in Category.query.all()]
