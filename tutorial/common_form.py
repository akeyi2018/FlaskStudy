from save_message import Messager
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField

def get_comment_data():
	module = Messager().read_data()
	return module

class MemberMonthlyForm(FlaskForm):
    # 月別ラベル取得
    start_month = SelectField('Start', choices=['2023-04','2023-05','2023-06'])
    submit = SubmitField('Submit')
