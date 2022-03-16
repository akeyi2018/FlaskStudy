from collections import defaultdict
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import DateField
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test secrect key'

class NameForm(FlaskForm):
    start_date = DateField('start date:', format='%Y-%m-%d',default=date(2000,4,1))
    end_date = DateField('end date:', format='%Y-%m-%d', default=date.today())
    submit = SubmitField('submit')

@app.route('/s', methods=['GET', 'POST'])
def index():
    start_d = None
    end_d = None
    form = NameForm()
    if form.is_submitted():
        start_d = form.start_date.data
        end_d = form.end_date.data
        # print(type(start_d))

    return render_template('index.html', form=form)
    # return render_template('index.html', form=form, start_date = start_d, end_date=end_d)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

