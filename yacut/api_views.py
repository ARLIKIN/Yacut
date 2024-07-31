from flask import jsonify, request, url_for

from settings import Config
from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import check_duplicate, generate_random_link, check_chars


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' in data and data['custom_id'] != '':
        short = data['custom_id']
        if len(short) > Config.MAX_SHORT_LEN or check_chars(short):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if check_duplicate(short):
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
    else:
        data['custom_id'] = generate_random_link()

    url_map = URLMap(
        original=data['url'],
        short=data['custom_id'],
    )
    db.session.add(url_map)
    db.session.commit()

    return jsonify({
        'url': data['url'],
        'short_link': url_for(
            'short_view',
            short=url_map.short,
            _external=True
        )
    }), 201


@app.route('/api/id/<short>/', methods=['GET'])
def get_url(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        raise InvalidAPIUsage(
            'Указанный id не найден',
            status_code=404
        )
    return jsonify({'url': url_map.original}), 200
