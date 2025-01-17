from flask import Flask, render_template
from waitress import serve
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
# db = SQLAlchemy()
migrate = Migrate()

#def create_app():
app = Flask(__name__)
# app.config.from_object(config)
app.config.from_envvar('APP_CONFIG_FILE')

# ORM
db.init_app(app)
# migrate.init_app(app, db)
if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)
from . import models

# @app.route('/')
# def hello_myapp():
#     return 'Hello, First my App!'

# Blueprint
# from .views import main_views
# app.register_blueprint(main_views.bp)

from .views import main_views, question_views, answer_views, auth_views
app.register_blueprint(main_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)

#블루프린트가 없을경우
# 라우트 정의
# @app.route('/')
# def index():
#     return 'Hello, First my App!'

# @app.route('/questions')
# def questions():
#     return 'Questions Page'

# @app.route('/answers')
# def answers():
#     return 'Answers Page'

# 라우팅
# @app.route('/')

# 필터
from .filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime
    
    #return app
serve(app, listen="*:80")
# serve(app)