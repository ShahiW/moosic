import logging
from typing import Any
from flask_appbuilder import SQLA  # type: ignore[import]

logger = logging.getLogger(__name__)

db = SQLA()


def tune_sqlite() -> None:
    from sqlalchemy.engine import Engine
    from sqlalchemy import event

    # Only include this for SQLLite constraints
    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):  # type: ignore[no-untyped-def]
        # Will force sqlite constraint foreign keys
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
