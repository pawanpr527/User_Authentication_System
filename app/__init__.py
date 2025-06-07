from flask import Flask
from app.extensions import db, login_manager
from app.models import User
import os
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myData.db')

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
