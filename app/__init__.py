from flask import Flask
from flask_sqlalchemy import flask_SQLAlchemy

db=SQLAlchemy()
def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    from .routes import main
    from .api import api
    
    app.register_blueprint(main)
    app.register_blueprint(api,url_prefix='/api')

    return app