from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length


class OpinionForm(FlaskForm):
    source = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    title = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16)]
    )
    submit = SubmitField('Создать')
