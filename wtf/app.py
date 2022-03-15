from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import DateField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test secrect key'

class NameForm(FlaskForm):
    name = StringField('name:', validators=[DataRequired()])
    inputdate = DateField('日時:', format='%Y-%m-%d')
    submit = SubmitField('Go')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.inputdate.data
    if form.is_submitted():
        input_date = form.inputdate.data
    return render_template('index.html', form=form, name=input_date)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

