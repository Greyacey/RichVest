import datetime

from app.main import db


class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(60), unique=True, nullable=False, index=True)
    user_id = db.Column(db.String(60), db.ForeignKey('users.public_id'))
    balance = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)