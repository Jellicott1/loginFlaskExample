from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
with open('loginDetails.txt') as f:
    line = f.readline().split(',')
    users.append([line[0],line[1]])

@app.route('/signup', methods=['POST'])
def signup():
    #Get the JSON fata from the request
    data = request.get_json()

    #Check if JSON was provided and contains the required keys
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"status": "failed", "message": "Missing username or password"}), 400
    
    users.append([data['username'].strip(),data['password'].strip()])
    print(users)
    return jsonify({"status": "success", "message": "Signed up successfully."})


@app.route('/login', methods=['POST'])
def login():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if JSON was provided and contains the required keys
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"status": "failed", "message": "Missing username or password"}), 400

    # Validate credentials
    print(users)
    for i in range(len(users)):
        if data['username'].strip() == users[i][0] and data['password'].strip() == users[i][1]:
            return jsonify({"status": "success", "message": "Welcome!"}), 200
    return jsonify({"status": "invalid", "message": "Incorrect credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)