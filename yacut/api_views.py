from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import check_short_url, generate_random_link


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'custom_id' in data and data['custom_id'] != '':
        custom_id = data['custom_id']
        if check_short_url(custom_id):
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
    else:
        data['custom_id'] = generate_random_link()

    url_map = URLMap(
        full_url=data['url'],
        short_url=data['custom_id'],
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify({
        'url': data['url'],
        'short_link': f'{request.url_root}{url_map.short_url}'
    }), 201


@app.route('/api/id/<short_url>', methods=['GET'])
def get_url(short_url):
    url_map = URLMap.query.filter_by(short_url=short_url).first()
    if url_map is None:
        raise InvalidAPIUsage(
            'Указанный id не найден'
        )
    return jsonify({'url': url_map.full_url}), 200
