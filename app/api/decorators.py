from functools import wraps
from flask import g
from .errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return (
                f(*args, **kwargs)
                if g.current_user.can(permission)
                else forbidden('Insufficient permissions')
            )

        return decorated_function

    return decorator
