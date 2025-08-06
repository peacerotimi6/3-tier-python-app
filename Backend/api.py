from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

with open('/run/secrets/db_pass') as f:
    DB_PASS = f.read().strip()

DB_HOST = os.getenv("DB_HOST", "database")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "peacerotimi6")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/api")
def api():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from Backend API and DB!'")
        msg = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"message": msg})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
