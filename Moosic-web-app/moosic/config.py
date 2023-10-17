from pathlib import Path
import logging
from flask_appbuilder.security.manager import AUTH_DB

logger = logging.getLogger(__name__)

ROLES = {
    #"Viewer": [
        #("PersonView", "can_list"),
        #("PersonView", "can_show"),
        #("People", "menu_access"),
    #]
}


class FlaskConfig:
    ENV = "development"
    DEBUG = True
    TESTING = True
    APP_NAME = "Moosic"
    # APP_ICON = "/static/img/whistle.png"
    SECRET_KEY = "willtheylayoffme"
    APP_DIR = Path(__file__).parent
    STATIC_DIR = APP_DIR / "static"
    IMG_DIR = STATIC_DIR / "images"
    TEMPLATES_DIR = APP_DIR / "templates"
    # FAB_BASE_TEMPLATE = "base.html"
    APP_DB = APP_DIR.parent / "app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    AUTH_ROLE_PUBLIC = "Public"
    AUTH_ROLE_ADMIN = "Admin"
    FAB_ROLES = ROLES
    AUTH_USER_REGISTRATION = True
    AUTH_TYPE = AUTH_DB
    BABEL_DEFAULT_LOCALE = "en"
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = "translations"
    # The allowed translation for you app
    LANGUAGES: dict[str, dict[str, str]] = {}
    RECAPTCHA_ENABLED = False
    RECAPTCHA_PUBLIC_KEY =''


    # APP_THEME = "united.css"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"sqlite:///{self.APP_DB.absolute()}"

    def __init__(self) -> None:
        logger.info(self.SQLALCHEMY_DATABASE_URI)

