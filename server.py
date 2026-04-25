from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if JSON was provided and contains the required keys
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"status": "failed", "message": "Missing username or password"}), 400

    # Validate credentials
    if data['username'] == "test" and data['password'] == "1234":
        return jsonify({"status": "success", "message": "Welcome!"}), 200
    else:
        return jsonify({"status": "invalid", "message": "Incorrect credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)