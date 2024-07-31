import random
import string

from flask import flash, redirect, render_template, url_for

from settings import Config
from . import app, db
from .forms import UrlForm
from .models import URLMap


def generate_random_link(length=6):
    characters = string.ascii_letters + string.digits
    random_link = ''.join(random.choice(characters) for _ in range(length))
    if check_duplicate(random_link):
        random_link = generate_random_link()
    return random_link


def check_duplicate(short):
    return URLMap.query.filter_by(short=short).first() is not None


def check_chars(short):
    for char in short:
        if char not in string.ascii_letters + string.digits:
            return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        if form.custom_id.data != '' and form.custom_id.data is not None:
            short = form.custom_id.data
            if len(short) > Config.MAX_SHORT_LEN or check_chars(short):
                flash('Указано недопустимое имя для короткой ссылки')
                return render_template('general.html', form=form)
            if check_duplicate(short):
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('general.html', form=form)
        else:
            short = generate_random_link()
        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template(
            'general.html',
            form=form,
            link=url_for(
                'short_view',
                short=url_map.short,
                _external=True
            )
        )
    return render_template('general.html', form=form)


@app.route('/<short>')
def short_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
