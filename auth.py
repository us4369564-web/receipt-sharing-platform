from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)

users = []

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    user = {
        "username": data.get("username"),
        "email": data.get("email"),
        "password": data.get("password")
    }
    users.append(user)
    return jsonify({"message": "User registered successfully"})

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user["email"] == data.get("email") and user["password"] == data.get("password"):
            return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"})

@auth.route('/profile', methods=['GET'])
def profile():
    return jsonify(users)

@auth.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "Logged out successfully"})
