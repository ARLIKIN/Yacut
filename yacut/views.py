import random
import string

from flask import flash, redirect, render_template, url_for, request

from . import app, db
from .forms import UrlForm
from .models import URLMap


def generate_random_link(length=6):
    characters = string.ascii_letters + string.digits
    random_link = ''.join(random.choice(characters) for _ in range(length))
    if check_short_url(random_link):
        random_link = generate_random_link()
    return random_link


def check_short_url(short_url):
    return URLMap.query.filter_by(short_url=short_url).first() is not None


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        if form.short_url.data != '':
            short_url = form.short_url.data
            if check_short_url(short_url):
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('general.html', form=form)
        else:
            short_url = generate_random_link()
        url_map = URLMap(
            full_url=form.full_url.data,
            short_url=short_url
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template(
            'general.html',
            form=form,
            short_link=f'{request.url_root}{url_map.short_url}'
        )
    return render_template('general.html', form=form)


@app.route('/<short_url>')
def short_url_view(short_url):
    url_map = URLMap.query.filter_by(short_url=short_url).first()
    if url_map is None:
        return redirect(url_for('index_view'))
    return redirect(url_map.full_url)
