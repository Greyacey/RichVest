from flask import Blueprint
from flask_restplus import Api

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.wallet_controller import api as wallet_ns
from .main.controller.transaction_controller import api as transaction_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Richvest 360 WALLETS ENDPOINTS',
          version='1.0',
          description='a simple Wallet API based on Flask'
          )

api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(wallet_ns, path='/wallets')
api.add_namespace(transaction_ns, path='/transactions')
