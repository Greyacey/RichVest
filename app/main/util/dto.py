from flask_restplus import Namespace, fields

class AuthDTO:
    api = Namespace('Log in', description='user authentication for login')

    s_user_auth = api.model('login_auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class UserDTO:
    api = Namespace('Users', description='user related operations')
    user = api.model('users', {
        'publicId': fields.String(description='Identifier', attribute='public_id'),
        'email': fields.String(description='user email', attribute='email'),
    })
    register = api.model('register', {
        'email': fields.String(description='user email', attribute='email'),
        'password': fields.String(description='user password', attribute='password'),
    })

    change_password = api.model('change_password', {
        'oldPassword': fields.String(description='user first name', attribute='old_password'),
        'password': fields.String(description='user last name', attribute='password'),
    })

class WalletDTO:
    api = Namespace('Wallets', description='wallet related operations')
    wallet = api.model('wallets', {
        'amount': fields.Float(description='Funding amount'),
        'paymentId': fields.String(required=True, description='payment id'),
        'balance': fields.Float(required=True, description='wallet balance'),
        'userId': fields.String(required=True, description='wallet user id', attribute='user_id'),
        'publicId': fields.String(description='Identifier', attribute='public_id')
    })

class TransactionDTO:
    api = Namespace('Transactions', description='transaction related operations')
    transaction = api.model('transactions', {
        'amount': fields.Float(description='transaction amount'),
        'recieverId': fields.String(required=True, description='reciever wallet ID', attribute='txn_type'),
        'txnDesc': fields.String(required=True, description='Transaction description', attribute='description'),
        'userId': fields.String(required=True, description='transaction user id', attribute='user_id'),
        'publicId': fields.String(description='Identifier', attribute='public_id')
    })