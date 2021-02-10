import datetime
import uuid

from app.main import db
from app.main.model.transaction import Transaction
from app.main.model.wallet import Wallet


def save_new_transaction(data):
    public_id = str(uuid.uuid4())

    transfer = Wallet.query.filter_by(user_id=user_id).first()
    reciever = Wallet.query.filter_by(user_id=reciever_id).first()

    amount = data.get('amount', None)
    
    if transfer:
        balance = transfer.balance
        new_balance = balance - amount
        transfer.balance = new_balance
        transfer.updated_at = datetime.datetime.utcnow()

    if reciever:
        balance_two = reciever.balance
        new_balance_two = balance_two + amount
        reciever.balance = new_balance_two
        reciever.updated_at = datetime.datetime.utcnow()

    new_transaction = Transaction(
        public_id=public_id,
        user_id=data.get('userId', None),
        amount=data.get('amount', None),
        description=data.get('txnDesc', None),
        reciever_id=data.get('recieverId', None),
    )
    try:
        save_changes(reciever)
        save_changes(transfer)
        save_changes(new_transaction)
        data['publicId'] = public_id 
        return data
    except Exception as e:
        return {'error': str(e)}


def get_all_transactions():
    return Transaction.query.all()


def get_a_transaction(public_id):
    return Transaction.query.filter_by(public_id=public_id)


def delete_a_transaction(public_id):
    txn = get_a_transaction(public_id)
    if not txn:
        return {'error': 'Transaction not found'}
    try:
        delete(txn)
        return True
    except Exception as e:
        return {'error': str(e)}


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete(data):
    db.session.delete(data)
    db.session.commit()
