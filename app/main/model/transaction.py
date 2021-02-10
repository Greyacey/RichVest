import datetime

from app.main import db


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(60), unique=True, nullable=False, index=True)
    user_id = db.Column(db.String(60), db.ForeignKey('users.public_id'))
    amount = db.Column(db.Float, nullable=False, default=0.0)
    descrption = db.Column(db.String(150), nullable=False)
    reciever_id = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
