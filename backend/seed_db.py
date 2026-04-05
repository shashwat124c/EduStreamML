# backend/seed_db.py
from pymongo import MongoClient

# Connect to your local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.learning_path_db
modules_collection = db.modules

def seed_database():
    # 1. Clear out any old data
    print("Clearing old curriculum data...")
    modules_collection.delete_many({})
    
    # 2. Define the Complete Curriculum
    curriculum = [
        # --- FOUNDATION COURSE ---
        {
            "topic_id": "web_101",
            "course": "Web Fundamentals",
            "name": "How the Web Works",
            "description": "Understand HTTP, DNS, and the Request/Response cycle.",
            "video_url": "https://www.youtube.com/watch?v=RsQ1tVNmcOU",
            "prerequisites": [], 
            "difficulty": "beginner",
            "quiz": [
                {
                    "question": "What does HTTP stand for?",
                    "options": ["HyperText Transfer Protocol", "HyperText Transmission Process", "HyperLink Transfer Protocol", "Host Text Transmission"],
                    "correct_index": 0
                },
                {
                    "question": "Which of these is responsible for translating domain names to IP addresses?",
                    "options": ["Router", "DNS", "TCP", "MAC"],
                    "correct_index": 1
                }
            ]
        },

        # --- REACT COURSE ---
        {
            "topic_id": "react_components",
            "course": "React",
            "name": "React Components",
            "description": "Building reusable UI blocks in React.",
            "video_url": "https://www.youtube.com/watch?v=Y2hgEGPzTZY",
            "prerequisites": ["web_101"],
            "difficulty": "beginner",
            "quiz": [
                {
                    "question": "In React, a component must always return:",
                    "options": ["A string", "Multiple DOM elements", "A single JSX element", "A JavaScript function"],
                    "correct_index": 2
                }
            ]
        },
        {
            "topic_id": "react_state",
            "course": "React",
            "name": "State & Props",
            "description": "Managing data flow and internal state.",
            "video_url": "https://www.youtube.com/watch?v=O6P86uwfdR0",
            "prerequisites": ["react_components"],
            "difficulty": "intermediate",
            "quiz": [
                {
                    "question": "How do you pass data from a parent to a child component?",
                    "options": ["Using State", "Using Props", "Using Context", "Using Redux"],
                    "correct_index": 1
                }
            ]
        },

        # --- FLASK COURSE ---
        {
            "topic_id": "flask_routing",
            "course": "Flask",
            "name": "Routing Basics",
            "description": "Creating endpoints in a Flask application.",
            "video_url": "https://www.youtube.com/watch?v=mqhxxeeTbu0",
            "prerequisites": ["web_101"],
            "difficulty": "beginner",
            "quiz": [
                {
                    "question": "Which decorator is used to bind a function to a URL in Flask?",
                    "options": ["@app.route()", "@flask.url()", "@app.bind()", "@url.route()"],
                    "correct_index": 0
                }
            ]
        },
        {
            "topic_id": "flask_templates",
            "course": "Flask",
            "name": "Jinja2 Templates",
            "description": "Rendering dynamic HTML pages using Jinja2.",
            "video_url": "https://www.youtube.com/watch?v=QnDWIZuWYW0",
            "prerequisites": ["flask_routing"],
            "difficulty": "intermediate",
            "quiz": [
                {
                    "question": "What syntax is used in Jinja2 to output a Python variable?",
                    "options": ["<% var %>", "{% var %}", "{{ var }}", "[[ var ]]"],
                    "correct_index": 2
                }
            ]
        }
    ]

    # 3. Insert into MongoDB
    modules_collection.insert_many(curriculum)
    print(f"✅ Successfully seeded {len(curriculum)} modules into the database!")

if __name__ == "__main__":
    seed_database()