from flask import request
from flask_restplus import Resource

from app.main.service.transaction_service import delete_a_transaction
from ..service.transaction_service import save_new_transaction, get_all_transactions, get_a_transaction
from ..util.dto import TransactionDTO

api = TransactionDTO.api
_transaction = TransactionDTO.transaction


@api.route('/')
class TransactionList(Resource):
    @api.doc('list_of_all_transactions')
    @api.marshal_list_with(_transaction)
    def get(self):
        """get all transaction history"""
        transactions = get_all_transactions()
        if not transactions:
            api.abort(417)
        else:
            return transactions, 200

    @api.doc('create a new transaction')
    @api.expect(_transaction, validate=True)
    def post(self):
        """transfer funds from one wallet to another"""
        data = request.json
        feedback = save_new_transaction(data=data)
        if not feedback.get('error', None):
            response_object = {
                'status': 'success',
                'message': 'Transaction Successfully',
                'body': feedback,
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None)
            }
            return response_object, 400


@api.route('/<user_id>')
@api.param('user_id', 'The Transaction identifier')
class Transaction(Resource):
    @api.doc('get a transaction')
    @api.marshal_with(_transaction)
    def get(self, user_id):
        """get transaction history of a user"""
        transaction = get_a_transaction(user_id)
        if not transaction:
            api.abort(417)
        else:
            return transaction, 200
