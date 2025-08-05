cat > backend/api.py << 'EOF'
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/api")
def api():
    return jsonify({"message": "Hello from Backend API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF
