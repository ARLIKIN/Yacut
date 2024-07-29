from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import UrlForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        short_url = form.short_url.data
        if short_url == '':
            short_url = '38Adkv'
        if URLMap.query.filter_by(short_url=short_url).first() is not None:
            flash('Такое сокращение уже было оставлено ранее!')
            return render_template('general.html', form=form)
        opinion = URLMap(
            full_url=form.full_url.data,
            short_url=short_url
        )
        db.session.add(opinion)
        db.session.commit()
        return render_template('general.html', sort_link=opinion.short_url)
    return render_template('general.html', form=form)
