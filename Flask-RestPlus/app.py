from flask import Flask, jsonify
from flask_restx import Api, Resource, fields, model

app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language' : fields.String('The language.')})

languages = []
python = {'language': 'Python'}
languages.append(python)

@app.route('/language')
class Language(Resource):
    def get(self):
        return 'OK',200
    
    @api.expect(a_language)
    def post(self):
        languages.append(api.payload)
        return {'result' : 'Language added'}, 201

if __name__ == '__main__':
    app.run(debug=True)

