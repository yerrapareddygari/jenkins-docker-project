from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Learn Jenkins"},
    {"id": 3, "task": "Learn Kubernetes"},
    {"id": 4, "task": "Get DevOps Job 🚀"}
]

@app.route('/todos')
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

