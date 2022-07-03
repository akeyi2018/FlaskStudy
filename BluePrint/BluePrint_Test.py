from flask import Flask

from admin.api import Api

app = Flask(__name__)

app.register_blueprint(Api,url_prefix='/admin')

if __name__ == '__main__':
    app.run()

