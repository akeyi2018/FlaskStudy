from flask import Flask, escape, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return show_the_login_form()

@app.route('/res', methods=['GET', 'POST'])
def do_the_login():
    return """
    Result:
    <h1>{}</h1>
    """.format(str(request.form["num"]))

def show_the_login_form():
    return """
    TEST POST
    <form action= "/res" method="POST">
    <input name = "num"></input>
    </form>"""

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    #return 'user: %s' % escape(username)
    return '{}\'s profile'.format(escape(username))

if __name__ == "__main__":
    app.run(debug=True)
