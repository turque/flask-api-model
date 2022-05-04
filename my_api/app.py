# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask
from loguru import logger

from my_api import api, auth, manage
from my_api.extensions import apispec, db, jwt, ma, migrate


def create_app(config_object="my_api.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    configure_logger(app)
    configure_cli(app)
    configure_apispec(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
    app.register_blueprint(api.health.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)
    return None


def configure_logger(app):
    """Configure loggers."""
    fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} [{function} @ {file}]"
    logger.start(
        app.config["LOGFILE"],
        level=app.config["LOG_LEVEL"],
        format=fmt,
        colorize=True,
        enqueue=True,
        backtrace=app.config["LOG_BACKTRACE"],
        rotation="25 MB",
    )


def configure_cli(app):
    """Configure Flask 2.0's cli for easy entity management"""
    app.cli.add_command(manage.init)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )
