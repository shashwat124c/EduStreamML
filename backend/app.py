# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import our custom services
from services.youtube_service import fetch_youtube_resources
from ML.classifier import dummy_classify_difficulty

from services.db_service import get_cached_path, save_to_cache

app = Flask(__name__)
CORS(app) # Allows your React frontend to communicate with Flask

@app.route('/api/search', methods=['GET'])
def generate_learning_path():
    query = request.args.get('q')
    
    if not query:
        return jsonify({"error": "Please provide a search query (e.g., ?q=react hooks)"}), 400

    print(f"User searched for: {query}")

    try:
        cached_data = get_cached_path(query)
        if cached_data:
            return jsonify({
                "topic": query,
                "status": "success",
                "source": "database_cache", # Tells React where it came from
                "learning_path": cached_data["learning_path"]
            }), 200
        
        # Fetch raw data from YouTube 
        # We fetch a bit more (e.g., 15) so the ML has enough to sort into 3 buckets
        raw_resources = fetch_youtube_resources(query, max_results=15)
        
        if not raw_resources:
            return jsonify({"error": "No resources found for this topic."}), 404

        # 2. Pass data to the ML component (Developer 1's domain)
        structured_path = dummy_classify_difficulty(raw_resources)

        save_to_cache(query, structured_path) #saving cache for future reference

        # 3. Return the final structured JSON
        return jsonify({
            "topic": query,
            "status": "success",
            "learning_path": structured_path
        }), 200

    except Exception as e:
        print(f"Error during search: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Runs the server on port 5000
    print("Starting backend server on http://localhost:5000...")
    app.run(debug=True, port=5000)