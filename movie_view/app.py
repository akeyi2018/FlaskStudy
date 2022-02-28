from flask import Flask, send_from_directory
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class Show_Movie(Resource):
    def get(self):
        return 200
    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

api.add_resource(Show_Movie,'/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
