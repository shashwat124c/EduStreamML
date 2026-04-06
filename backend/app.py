# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient  
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

app = Flask(__name__)
CORS(app) # Allows your React frontend to communicate with Flask

# Initialize MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.learning_path_db

GOOGLE_CLIENT_ID = "655631990423-n5gsmr8hlae8d8s3fqj8hqbgugr8vs6n.apps.googleusercontent.com"

@app.route('/api/modules', methods=['GET'])
def get_curriculum():
    try:
        # Fetch all modules from the database
        modules = list(db.modules.find({}))
        
        # Clean up the MongoDB ObjectId for JSON serialization
        for mod in modules:
            mod['_id'] = str(mod['_id'])
            
        return jsonify({
            "status": "success",
            "data": modules
        }), 200
        
    except Exception as e:
        print(f"Error fetching modules: {e}")
        return jsonify({"error": "Failed to fetch curriculum"}), 500

# --- NEW OAUTH ROUTE ---
@app.route('/api/auth/google', methods=['POST'])
def google_auth():
    # 1. React sends us the token
    token = request.json.get('token')
    if not token:
        return jsonify({"error": "No token provided"}), 400

    try:
        # 2. Ask Google if the token is valid
        idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), GOOGLE_CLIENT_ID)
        
        # 3. Extract user info from Google's response
        email = idinfo['email']
        name = idinfo.get('name', 'Student')
        picture = idinfo.get('picture', '')

        # 4. Check if user exists in MongoDB
        user = db.users.find_one({"email": email})
        
        if not user:
            # First time logging in! Create their profile.
            new_user = {
                "email": email,
                "name": name,
                "picture": picture,
                "completed_topics": [], # They start with 0 progress
                "role": "student"
            }
            db.users.insert_one(new_user)
            user_data = new_user
        else:
            # Returning user
            user_data = user

        # Remove the MongoDB ObjectId before sending to React
        user_data['_id'] = str(user_data.get('_id', ''))

        return jsonify({
            "status": "success",
            "user": user_data
        }), 200

    except ValueError:
        # Invalid token
        return jsonify({"error": "Invalid Google token"}), 401

if __name__ == '__main__':
    # Runs the server on port 5000
    print("Starting backend server on http://localhost:5000...")
    app.run(debug=True, port=5000)