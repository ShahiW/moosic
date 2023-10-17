from __future__ import annotations

import logging
from base64 import b64encode
from flask import Flask, g  # g is global variable that will be initialized for every request (user endpoint access)
from flask_appbuilder import AppBuilder
from flask_appbuilder.security.sqla.models import User, Role
from moosic.db import db, tune_sqlite
from moosic.config import FlaskConfig
from moosic.views import MoosicViews, MoosicIndexViews


def is_admin() -> bool:

    try:
        for role in g.user.roles:
            if role.name == "Admin":
                return True
    except AttributeError:
        pass
    return False


appbuilder = AppBuilder(indexview=MoosicIndexViews)


def create_app() -> Flask:
    
    log_format = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(format=log_format)
    logging.getLogger().setLevel(logging.INFO)

    app = Flask("moosic")
    app.config.from_object(FlaskConfig())

    jinja_env = {
        "get_current_user": lambda: g.user,
        "is_admin": is_admin,
    }
    app.context_processor(lambda: jinja_env)

    @app.template_filter("base64")
    def base64_filter(text: str) -> str:
        return b64encode(text.encode()).decode()

    # Open pseudo request for initializing app builder and SQL Alchemy
    with app.app_context():
        db.init_app(app)  # Flask SQL Alchemy gets initialized with our Flask App
        if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):  # Tune if SQLite is used
            tune_sqlite()

        appbuilder.init_app(app, db.session)  # Flask App Builder gets initialized with our Flask App and SQL Alchemy interface
        # init_errorhandlers(appbuilder)

        appbuilder.add_view(MoosicViews, "MoosicViews")

    return app
