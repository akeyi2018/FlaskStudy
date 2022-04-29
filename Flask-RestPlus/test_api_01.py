from flask_restx import Resource, fields
from flask import jsonify, request


class api_001(Resource):
    def get(self):
        return jsonify({'test':'OK'})

    def post(self):
        r = request.json
        return r,201

