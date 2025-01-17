from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_myapp():
    return 'Hello, my App!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# @bp.route('/')
# def index():
#     # username='관리자'
#     # user_info = {
#     #     "username": "사용자",
#     #     "age": 25
#     # }
#     user_list = ['Bob', 'Alice','Charlie' ]
#     return render_template('test2.html',users=user_list )

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get(question_id)
#     return render_template('question/question_detail.html', question=question)

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id): 
#     question = Question.query.get_or_404(question_id)   
#     return render_template('question/question_detail.html', question=question)


