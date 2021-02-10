import datetime
import uuid

from app.main import db
from app.main.model.wallet import Wallet


def save_new_wallet(data):
    public_id = str(uuid.uuid4())

    new_wallet = Wallet(
        public_id=public_id,
        user_id=data.get('userId', None),
        balance=data.get('balance', None),
    )
    try:
        save_changes(new_wallet)
        data['publicId'] = public_id
        return data
    except Exception as e:
        return {'error': str(e)}

def get_a_wallet(public_id):
    return Wallet.query.filter_by(public_id=public_id).first()

def fund_a_wallet(user_id, data):
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    balance = wallet.balance
    amount = data.get('amount', None)

    if wallet:
        if data.get('paymentId', None):
            new_balance = balance + amount
            wallet.balance = new_balance
        wallet.updated_at = datetime.datetime.utcnow()

        try:
            save_changes(wallet)
            return data
        except Exception as e:
            return {'error': str(e)}
    return {'error': 'Wallet Not found or Payment ID invalid'}


def delete_a_wallet(public_id):
    wallet = get_a_wallet(public_id)
    if not wallet:
        return {'error': 'Wallet not found'}

    try:
        delete(wallet)
        return True
    except Exception as e:
        return {'error': str(e)}


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete(data):
    db.session.delete(data)
    db.session.commit()
