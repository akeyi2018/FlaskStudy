from flask import Flask, escape, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/response', methods=['GET', 'POST'])
def show_post_result():
    return """
    POST実行結果:
    <h1>{}</h1>
    """.format(str(request.form["name"]))

@app.route('/showpostpage')
def show_the_post_form():
    return """
    文字列を入力し、Enterキーを押してください。
    <form action= "/response" method="POST">
    <input name = "name"></input>
    </form>"""

@app.route('/hello')
def hello():
    return 'Hello, World! 1234434343'

@app.route('/user/<username>')
def show_user_profile(username):
    #return 'user: %s' % escape(username)
    return '{}\'s profile'.format(escape(username))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
