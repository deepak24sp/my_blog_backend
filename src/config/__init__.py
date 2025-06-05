from .flask import FlaskAppConfig
def init_config(app):
    app.config.update(
        SQLALCHEMY_DATABASE_URI = FlaskAppConfig.SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS = FlaskAppConfig.SQLALCHEMY_TRACK_MODIFICATIONS,
        SECRET_KEY = FlaskAppConfig.SECRET_KEY
    )