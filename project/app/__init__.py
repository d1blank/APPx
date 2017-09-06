# -*- coding:utf-8 -*-
from flask import Flask, request
from os import path
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_pagedown import PageDown
from flask_gravatar import Gravatar
from flask_babel import Babel, gettext as _
from config import config

#from flask_nav import Nav
#from flask_nav.elements import *
#from werkzeug.routing import BaseConverter




basedir = path.abspath(path.dirname(__file__))

db = SQLAlchemy()
babel = Babel()
bootstrap = Bootstrap()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    babel.init_app(app)
    Gravatar(app, size=64)


    from auth import auth as auth_blueprint
    from main import main as main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, static_folder='static')

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path

    return app


#def create_app():
#	app = Flask(__name__)
#	app.config.from_pyfile('config')
#	app.config['SQLALCHEMY_DATABASE_URI'] = \
#		'sqlite:///' + path.join(basedir, 'data.sqlite')
#	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#	db.init_app(app)
#	bootstrap.init_app(app)
#	login_manager.init_app(app)
#	#nav.init_app(app)
#	#init_views(app)
#	from auth import auth as auth_blueprint
#	from main import main as main_blueprint
#
#	app.register_blueprint(auth_blueprint,url_prefix='/auth')
#	app.register_blueprint(main_blueprint,static_folder='static')
#
#	@app.template_test('current_link')
#	def is_current_link(link):
#		return link == request.path
#
#	return app





