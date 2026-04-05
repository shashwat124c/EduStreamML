# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient  

app = Flask(__name__)
CORS(app) # Allows your React frontend to communicate with Flask

# Initialize MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.learning_path_db


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


if __name__ == '__main__':
    # Runs the server on port 5000
    print("Starting backend server on http://localhost:5000...")
    app.run(debug=True, port=5000)