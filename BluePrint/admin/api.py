from flask import Blueprint

Api = Blueprint('api', __name__)

@Api.route('/login')
def hoge():
    return 'Login'

