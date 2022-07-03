from flask import Flask, jsonify
from flask_restx import Api, Resource, fields, model
from marshmallow import post_load, Schema, fields as ma_fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

db = SQLAlchemy(app)

authorizations = {
    'apikey':{
        'type' : 'apiKey',
        'in': 'header',
        'name':'X-API-KEY'
    }
}

api = Api(app, authorizations=authorizations)

class TheLanguage(object):
    def __init__(self, language, framework) -> None:
        self.language = language
        self.framework = framework
    
    def __repr__(self) -> str:
        return f'{self.language} is the language. {self.framework} is the framwork.'

class LanguageSchema(Schema):
    language = ma_fields.String()
    framework = ma_fields.String()

    @post_load
    def create_language(self, data, **kwargs):
        return TheLanguage(**data)

languages = []
# python = {'language': 'Python', 'id': 1}
python = TheLanguage(language='Python', framework='Flask')
languages.append(python)

a_language = api.model('Language', {'language' : fields.String('Thelanguage.'), 'framework' : fields.String('FR')})

@api.route('/language')
class Language(Resource):

    # @api.marshal_with(a_language, envelope='test')
    @api.doc(security='apikey')
    def get(self):
        schema = LanguageSchema(many=True)
        return schema.dump(languages)
    
    @api.expect(a_language)
    @api.doc(security='apikey')
    def post(self):
        schema = LanguageSchema()
        new_language = schema.load(api.payload)
        # new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result' : 'Language added'}, 201

if __name__ == '__main__':
    app.run(debug=True)