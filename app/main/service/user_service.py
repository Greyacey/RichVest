import datetime
import uuid

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    public_id = str(uuid.uuid4())

    new_user = User(
        public_id=public_id,
        email=data.get('email', None),
    )
    if data.get('password', None):
        new_user.password = data.get('password', None)
    try:
        save_changes(new_user)
        data['publicId'] = public_id
        return data
    except Exception as e:
        return {'error': str(e)}

def get_a_user_by_id(public_id):
    return User.query.filter_by(public_id=public_id).first()

def get_a_user_by_email(email):
    return User.query.filter_by(email=email).first()

    
def get_a_user_wallet(public_id):
    user = get_a_user_by_id(public_id)
    if user:
        return user.wallet
    else:
        return {'error': 'User Not found'}


def get_a_user_transactions(public_id):
    user = get_a_user_by_id(public_id)
    if user:
        return user.transactions.all()
    else:
        return {'error': 'User Not found'}


def delete_a_user(public_id):
    user = get_a_user_by_id(public_id)
    if not user:
        return {'error': 'User not found'}
    try:
        delete(user)
        return True
    except Exception as e:
        return {'error': str(e)}

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.public_id)
        return auth_token
    except Exception as e:
        return {'error': str(e)}


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete(data):
    db.session.delete(data)
    db.session.commit()
