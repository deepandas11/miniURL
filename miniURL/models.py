from datetime import datetime
import string
from random import choices

from .extensions import db


SHORT_URL_LEN = 5

# Database model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(SHORT_URL_LEN), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_shortlink()

    
    def generate_shortlink(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=SHORT_URL_LEN))

        link = self.query.filter_by(short_url=short_url).first()
        if link:
            return self.generate_shortlink()
        return short_url

        
