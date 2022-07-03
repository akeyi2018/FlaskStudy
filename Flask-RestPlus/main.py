from flask import Flask, jsonify
from flask_restx import Api

from test_api_01 import api_001

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'

app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post"]
app.config.SWAGGER_UI_REQUEST_DURATION = True
app.config.SWAGGER_UI_JSONEDITOR = True
api = Api(app, version='0.9', title='hello API', description='サンプルAPI')

person = api.schema_model()

api.add_resource(api_001, '/hello')
# api.add_namespace(api_001, '/hello')


if __name__ == '__main__':
    app.run(debug=True)