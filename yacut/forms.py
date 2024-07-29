from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length


class UrlForm(FlaskForm):
    full_url = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    short_url = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(0, 16)]
    )
    submit = SubmitField('Создать')
