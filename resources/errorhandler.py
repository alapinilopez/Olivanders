from app import *

def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response_error = jsonify(message)
    response_error.status_code = 404
    return response_error