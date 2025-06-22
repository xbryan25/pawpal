from flask import current_app

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app import db


def execute_sql_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()

    for statement in sql.split(';'):
        statement_strip = statement.strip()

        if statement_strip:
            db.session.execute(text(statement_strip))

    db.session.commit()
