from flask import Flask, request, jsonify
from backend.database import Database
from backend.repositories.user_repository import UserRepository
from backend.services.auth_services import AuthService

app = Flask(__name__)

db = Database("fitness.db")
db.initialize()
user_repo = UserRepository(db)

#@app.route('/health')
#def health():
    #return jsonify({'status': 'ok'}), 200

@app.post("/register")
def register():
    data = request.get_json()

    # Validate JSON payload
    required = ["username", "password", "email"]

    if not data:
        return jsonify({"error": "Missing required fields"}), 400
    
    for field in required:
        if field not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
    username = data["username"]
    password = data["password"]
    email = data["email"]

    # Hash password
    password_hash = AuthService.hash_password(password)

    # Try to create user
    try:
        user_id = user_repo.create_user(username, password_hash, email)
    except ValueError:
        return jsonify({"error": "Username already exists"}), 409
    
    return jsonify({"user_id": user_id}), 201

if __name__ == '__main__':
    app.run(debug=True)