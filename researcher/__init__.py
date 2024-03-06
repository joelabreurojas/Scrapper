from flask import Flask
from config import Config

from .routes import general_scope, api_scope, errors_scope

researcher = Flask(
        __name__,
        static_folder=Config.STATIC_FOLDER,
        template_folder=Config.TEMPLATE_FOLDER
    )

researcher.config.from_object(Config)

researcher.register_blueprint(general_scope, url_prefix="/")
researcher.register_blueprint(errors_scope, url_prefix="/")
researcher.register_blueprint(api_scope, url_prefix="/api")
