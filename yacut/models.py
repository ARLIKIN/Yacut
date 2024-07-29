from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String(16), nullable=False, unique=True)

    def to_dict(self):
        return dict(
            id=self.id,
            full_url=self.full_url,
            short_url=self.short_url,
        )

    def from_dict(self, data):
        for field in ['full_url', 'short_url']:
            if field in data:
                setattr(self, field, data[field])
