from flask import Blueprint, render_template
from common_form import MemberMonthlyForm, get_comment_data
# Formクラス及び使用するフィールドをインポート

# 自分自身をBlueprintに登録する
bp_view = Blueprint('view_graph', __name__, static_folder='../static', template_folder='../templates')

@bp_view.route('/cm2')
def comment2():
	form = MemberMonthlyForm()

	ld = get_comment_data()
	d_x = [80, 50, 90]
	d_y = [30, 40, 50]
	
	t_x = ["日本語", 50, 90]
	t_y = ["テスト", 50, 90]
	t_z = ["応答", 50, 90]
	t_k = ["解凍", 50, 90]

	return render_template('register5.html', form=form, d=ld, d_x=d_x, d_y=d_y, dd = zip(d_x,d_y),
			table_dd=zip(t_x,t_y,t_z,t_k))
