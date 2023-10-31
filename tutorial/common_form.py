from save_message import Messager
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
# Formクラス及び使用するフィールドをインポート
from wtforms import SubmitField, SelectMultipleField, widgets

def get_comment_data():
	module = Messager().read_data()
	return module

class MemberMonthlyForm(FlaskForm):
    # 月別ラベル取得
    start_month = SelectField('Start', choices=['2023-04','2023-05','2023-06'])
    multi = SelectMultipleField("test", choices=['abc','def','ghi'])
    submit = SubmitField('Submit')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class StoreForm(FlaskForm):
    # オプション
    list_of_store = ['A店','B店','C店']
    # create a list of value/description tuples
    # li = [(x, x) for x in list_of_store]
    # print(li)
    stores = MultiCheckboxField('Label', choices=list_of_store)

    start_month = SelectField('Start', choices=['2023-04','2023-05','2023-06'])
    multi = SelectMultipleField("test", choices=['abc','def','ghi'])
    submit = SubmitField('Submit')

class SelectMultiStore(FlaskForm):
    list_of_store = ['A店 B','B店 C','C店 d','D店 /sa','E店/sad']
    stores = SelectMultipleField("店舗選択：", choices=list_of_store)
    category_li = ['区分１','区分２','区分３']
    
    category = SelectMultipleField("区分：", choices=category_li)
    submit = SubmitField('Submit')
