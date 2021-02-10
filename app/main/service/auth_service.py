from app.main.model.user import User


class Auth:

    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.public_id)
                if auth_token:
                    return auth_token
            else:
                return {'error': 'email or password does not match.'}

        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, dict):
                user = User.query.filter_by(public_id=resp).first()
                return user
            return {'error': resp['error']}
        else:
            return {'error': 'Provide a valid auth token.'}
