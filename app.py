from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "mydatabase")
DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "password")

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Hey, this is Velma’s Docker trial app! PostgreSQL version: {db_version[0]}"
    except Exception as e:
        return f"Error connecting to PostgreSQL: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)



