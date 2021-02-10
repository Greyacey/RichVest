from functools import wraps

from flask import request

from app.main.model.user import User
from app.main.service.auth_service import Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        feedback = Auth.get_logged_in_user(request)
        if not isinstance(feedback, User):
            return {
                       'status': 'fail',
                       'message': feedback.get('error', None)
                   }, 401

        return f(*args, **kwargs)

    return decorated


def verified_user_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        feedback = Auth.get_logged_in_user(request)

        if feedback.get('error', None):
            return {
                       'status': 'fail',
                       'message': feedback.get('error', None)
                   }, 401

        verified = feedback.get('if_verified')
        if not verified:
            response_object = {
                'status': 'fail',
                'message': 'user not verified'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
