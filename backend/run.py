
from app import create_app
from app.extensions import db
from app.db_utils.init_sql import execute_sql_file
from sqlalchemy import inspect

app = create_app()

if __name__ == "__main__":

    # Check if database already exists, if not, create database from app/db/init_schema.sql
    with app.app_context():
        try:

            inspector = inspect(db.engine)

            if not inspector.has_table("users"):
                print("🔧 First-time setup: initializing schema...")
                execute_sql_file("app/db_utils/init_schema.sql")
            else:
                print("✅ Database already initialized.")

        except Exception as e:
            print(f"Connection failed: {e}")

    app.run(debug=True, port=8080)
