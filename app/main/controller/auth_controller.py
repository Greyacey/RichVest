from flask import request
from flask_restplus import Resource

from app.main.service.auth_service import Auth
from app.main.service.user_service import get_a_user_by_email
from ..util.dto import AuthDTO

api = AuthDTO.api
s_user_auth = AuthDTO.s_user_auth


@api.route('/login')
class AuthLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('smart phone user login')
    @api.expect(s_user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        try:
            feedback = Auth.login_user(data=post_data)
        except Exception as e:
            return 'an error occurred', 500

        if not isinstance(feedback, dict):
            user_data = get_a_user_by_email(post_data.get('email', None))
            response_data = {
                'email': user_data.email,
            }
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'body': response_data,
                'Authorization': feedback.decode()
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': feedback.get('error', None),
            }
            return response_object, 401
