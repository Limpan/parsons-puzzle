from config import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    """Application factory, see docs."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
