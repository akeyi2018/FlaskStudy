from flask import Flask, jsonify
from flask_restx import Api, Resource, fields, model

app = Flask(__name__)
api = Api(app, doc=False)

a_language = api.model('Language', {'language' : fields.String('The language.'), 'id' : fields.Integer('ID')})

languages = []
python = {'language': 'Python', 'id': 1}
languages.append(python)

@api.route('/language')
class Language(Resource):

    @api.marshal_with(a_language, envelope='test')
    def get(self):
        return languages
    
    @api.expect(a_language)
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(api.payload)
        return {'result' : 'Language added'}, 201

if __name__ == '__main__':
    app.run(debug=True)