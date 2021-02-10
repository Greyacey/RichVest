from flask import request
from flask_restplus import Resource

from ..service.wallet_service import save_new_wallet, delete_a_wallet 
from ..util.dto import WalletDTO

api = WalletDTO.api
_wallet = WalletDTO.wallet


@api.route('/')
class WalletList(Resource):
    @api.doc('create a new wallet')
    @api.expect(_wallet, validate=True)
    def post(self):
        """Creates a new Wallet """
        data = request.json
        feedback = save_new_wallet(data=data)
        if not feedback.get('error', None):
            response_object = {
                'status': 'success',
                'message': 'Wallet Successfully Created',
                'body': feedback,
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None)
            }
            return response_object, 400

    @api.doc('delete a wallet')
    def delete(self, public_id):
        """deletes Wallet """
        feedback = delete_a_wallet(public_id)
        if isinstance(feedback, bool):
            response_object = {
                'status': 'success',
                'message': 'Wallet Deleted'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None)
            }
            return response_object, 404

@api.route('/<user_id>/user')
@api.param('user_id', 'The Wallet User identifier')
class WalletUser(Resource):
    @api.doc('update user wallet')
    @api.expect(_wallet, validate=True)
    def put(self, user_id):
        """Fund Wallet """
        data = request.json
        feedback = fund_a_wallet(user_id, data=data)
        if not feedback.get('error', None):
            response_object = {
                'status': 'success',
                'message': 'Wallet Successfully Funded',
                'body': feedback,
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None)
            }
            return response_object, 400

