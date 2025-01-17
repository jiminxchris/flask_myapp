from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from myapp import db
from myapp.models import Question, Answer, User
from ..forms import AnswerForm

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']

        # 글쓴이 데이터 확인 (g.user가 없으면 Anonymous로 설정)
        anonymous_user = User.query.filter_by(username='Anonymous').first()
        user = g.user if g.user else anonymous_user

        answer = Answer(content=content, create_date=datetime.now(), user=user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)

# def create(question_id):
#     question = Question.query.get_or_404(question_id)
#     content = request.form['content']
#     answer = Answer(content=content, create_date=datetime.now())
#     question.answer_set.append(answer)
#     db.session.commit()
#     return redirect(url_for('question.detail', question_id=question_id))

@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id=answer.question.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)

@bp.route('/delete/<int:answer_id>')
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))