from flask import request
from flask_restplus import Resource

from app.main.service.user_service import save_new_user, delete_a_user, generate_token
from ..model.user import User
from ..util.dto import UserDTO

api = UserDTO.api
_user = UserDTO.user
_register = UserDTO.register

@api.route('/')
class Register(Resource):
    @api.doc('create a new user')
    @api.expect(_register, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        if data.get('email', None):
            the_user = get_a_user_by_email(data.get('email', None))
            if isinstance(the_user, User):
                response_object = {
                    'status': 'fail',
                    'message': 'Email already registered',
                }
                return response_object, 400
        feedback = save_new_user(data=data)
        # todo verify user
        if not feedback.get('error', None):
            the_user = get_a_user_by_id(feedback['publicId'])
            token = generate_token(the_user)

            if not isinstance(token, dict):
                response_object = {
                    'status': 'success',
                    'message': 'User Successfully registered',
                    'body': feedback,
                    'Authorization': token.decode()
                }
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': token.get('error', None),
                }
            return response_object, 400
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None),
            }
            return response_object, 400

    @api.doc('delete a user')
    def delete(self, public_id):
        """deletes User """
        feedback = delete_a_user(public_id)
        if isinstance(feedback, bool):
            response_object = {
                'status': 'success',
                'message': 'User Deleted'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None),
            }
            return response_object, 404