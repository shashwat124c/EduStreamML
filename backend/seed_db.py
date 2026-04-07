from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.learning_path_db

def seed_database():
    # 1. Drop existing collections to start fresh
    print("Dropping old collections...")
    db.modules.drop()
    db.skills.drop()

    # 2. Define the new Expansive CS & AI Curriculum
    curriculum = [
        # --- COURSE 1: Programming Fundamentals ---
        {
            "topic_id": "prog_basics_1",
            "course": "Programming Fundamentals",
            "name": "Intro to Programming & Variables",
            "difficulty": "beginner",
            "learning_objective": "Understand how computers store data in memory using variables and the basic syntax of programming.",
            "primary_video_url": "https://www.youtube.com/watch?v=zOjov-2OZ0E",
            "fallback_video_url": "https://www.youtube.com/watch?v=k5E2AVpwsko",
            "prerequisites": [],
            "skills": ["variables_and_control_flow"],
            "quiz": [
                {
                    "question": "What is a variable in programming?",
                    "options": [
                        "A mathematical formula",
                        "A named container for storing data values",
                        "A type of loop",
                        "A syntax error"
                    ],
                    "correct_index": 1,
                    "explanation": "A variable is like a box in memory with a name that we use to store and retrieve data."
                }
            ]
        },
        {
            "topic_id": "prog_basics_2",
            "course": "Programming Fundamentals",
            "name": "Memory Basics: Stack vs Heap",
            "difficulty": "intermediate",
            "learning_objective": "Learn how programs manage memory behind the scenes, distinguishing between the Stack and the Heap.",
            "primary_video_url": "https://www.youtube.com/watch?v=5OJRqkYbK-4",
            "fallback_video_url": "https://www.youtube.com/watch?v=_8-ht2AKyH4",
            "prerequisites": ["variables_and_control_flow"],
            "skills": ["memory_management"],
            "quiz": [
                {
                    "question": "Which memory region is used for dynamic memory allocation?",
                    "options": [
                        "The CPU Register",
                        "The Stack",
                        "The Heap",
                        "The Hard Drive"
                    ],
                    "correct_index": 2,
                    "explanation": "The Heap is used for dynamically allocated memory whose size may change during runtime, unlike the rigidly structured Stack."
                }
            ]
        },

        # --- COURSE 2: Data Structures ---
        {
            "topic_id": "ds_1",
            "course": "Data Structures",
            "name": "Arrays & Pointers",
            "difficulty": "intermediate",
            "learning_objective": "Understand contiguous memory allocation and how pointers interact with arrays under the hood.",
            "primary_video_url": "https://www.youtube.com/watch?v=RBSGKlAvoiM",
            "fallback_video_url": "https://www.youtube.com/watch?v=zTj-Uu6UvE0",
            "prerequisites": ["memory_management"],
            "skills": ["pointer_arithmetic", "contiguous_memory"],
            "quiz": [
                {
                    "question": "Why is accessing an array element by its index extremely fast (O(1))?",
                    "options": [
                        "Because the computer searches from the beginning",
                        "Because it predicts the memory address",
                        "Because arrays are stored in contiguous memory so the address is calculated mathematically",
                        "Because it is stored in the cache"
                    ],
                    "correct_index": 2,
                    "explanation": "Since array elements are placed side-by-side in memory, the exact address of any element can be computed instantly using its index."
                }
            ]
        },
        {
            "topic_id": "ds_2",
            "course": "Data Structures",
            "name": "Hash Tables Under the Hood",
            "difficulty": "advanced",
            "learning_objective": "Discover how mapping keys to values via hashing functions allows for near-instant data retrieval.",
            "primary_video_url": "https://www.youtube.com/watch?v=knV86FlSXJ8",
            "fallback_video_url": "https://www.youtube.com/watch?v=shs0KM3wKv8",
            "prerequisites": ["contiguous_memory"],
            "skills": ["hashing_concepts"],
            "quiz": [
                {
                    "question": "What is a 'collision' in a Hash Table?",
                    "options": [
                        "When the table runs out of memory",
                        "When two different keys generate the exact same hash code index",
                        "When a key is deleted twice",
                        "When the data types mismatch"
                    ],
                    "correct_index": 1,
                    "explanation": "A collision occurs when the hashing function accidentally computes the same index for two entirely different keys."
                }
            ]
        },

        # --- COURSE 3: Algorithms ---
        {
            "topic_id": "algo_1",
            "course": "Algorithms",
            "name": "Big-O & Time Complexity",
            "difficulty": "intermediate",
            "learning_objective": "Learn how to calculate and express the mathematical efficiency of an algorithm.",
            "primary_video_url": "https://www.youtube.com/watch?v=D6xkbGLQesk",
            "fallback_video_url": "https://www.youtube.com/watch?v=v4cd1O4zkGw",
            "prerequisites": ["variables_and_control_flow"],
            "skills": ["algorithmic_thinking"],
            "quiz": [
                {
                    "question": "Which Big-O notation represents an algorithm whose execution time grows exponentially as the input size increases?",
                    "options": [
                        "O(1)",
                        "O(log n)",
                        "O(n)",
                        "O(2^n)"
                    ],
                    "correct_index": 3,
                    "explanation": "O(2^n) represents exponential time complexity, where adding a single element to the input doubles the computation time."
                }
            ]
        },
        {
            "topic_id": "algo_2",
            "course": "Algorithms",
            "name": "Sorting Algorithms Deep Dive",
            "difficulty": "advanced",
            "learning_objective": "Compare the mechanics and runtime tradeoffs of Bubble Sort, Merge Sort, and Quick Sort.",
            "primary_video_url": "https://www.youtube.com/watch?v=kPRAFWXl1g0",
            "fallback_video_url": "https://www.youtube.com/watch?v=Hoixgm4-P4M",
            "prerequisites": ["algorithmic_thinking", "contiguous_memory"],
            "skills": ["sorting_logic"],
            "quiz": [
                {
                    "question": "Which of these sorting algorithms uses a 'Divide and Conquer' paradigm?",
                    "options": [
                        "Bubble Sort",
                        "Insertion Sort",
                        "Merge Sort",
                        "Selection Sort"
                    ],
                    "correct_index": 2,
                    "explanation": "Merge sort divides the array in half recursively until sub-arrays are of size 1, then merges them back together in sorted order."
                }
            ]
        },

        # --- COURSE 4: Database Internals ---
        {
            "topic_id": "db_1",
            "course": "Database Internals",
            "name": "SQL vs NoSQL Architecture",
            "difficulty": "beginner",
            "learning_objective": "Understand the structural differences between relational tables and document-based data stores.",
            "primary_video_url": "https://www.youtube.com/watch?v=ZS_kXvOeQ5Y",
            "fallback_video_url": "https://www.youtube.com/watch?v=cODCpNpZQLQ",
            "prerequisites": ["hashing_concepts"],
            "skills": ["schema_design"],
            "quiz": [
                {
                    "question": "Which scenario best fits a NoSQL database?",
                    "options": [
                        "A banking system requiring strict ACID transactions",
                        "A highly flexible application dealing with unstructured, rapidly changing document formats",
                        "An application that relies entirely on complex SQL JOINs",
                        "A system where data schema will never change"
                    ],
                    "correct_index": 1,
                    "explanation": "NoSQL (like MongoDB) shines when dealing with unstructured data forms that change frequently without rigid predefined tables."
                }
            ]
        },

        # --- COURSE 5: Artificial Intelligence ---
        {
            "topic_id": "ai_1",
            "course": "Artificial Intelligence",
            "name": "Intro to Machine Learning",
            "difficulty": "beginner",
            "learning_objective": "Understand the basics of how algorithms learn from data without being explicitly programmed.",
            "primary_video_url": "https://www.youtube.com/watch?v=NWONeJKn6kc",
            "fallback_video_url": "https://www.youtube.com/watch?v=ukzFI9rgwfU",
            "prerequisites": ["algorithmic_thinking"],
            "skills": ["ml_basics"],
            "quiz": [
                {
                    "question": "What is the key difference between Supervised and Unsupervised Learning?",
                    "options": [
                        "Supervised learning requires human observation 24/7",
                        "Supervised learning trains on labeled data (answers provided), while Unsupervised learning finds patterns in completely unlabelled data.",
                        "Unsupervised learning is significantly faster",
                        "Supervised learning only works on images"
                    ],
                    "correct_index": 1,
                    "explanation": "Supervised models learn by mapping inputs to known labels. Unsupervised models try to inherently cluster or group unlabelled data."
                }
            ]
        },
        {
            "topic_id": "ai_2",
            "course": "Artificial Intelligence",
            "name": "Neural Networks & Deep Learning",
            "difficulty": "advanced",
            "learning_objective": "Dive into perceptrons, activation functions, and backpropagation.",
            "primary_video_url": "https://www.youtube.com/watch?v=aircAruvnKk",
            "fallback_video_url": "https://www.youtube.com/watch?v=IHZwWFHWa-w",
            "prerequisites": ["ml_basics", "memory_management"],
            "skills": ["neural_networks"],
            "quiz": [
                {
                    "question": "What is the purpose of an 'Activation Function' in a neural network?",
                    "options": [
                        "To turn the computer on",
                        "To multiply weights",
                        "To introduce non-linearity, allowing the network to learn complex patterns",
                        "To reduce memory consumption"
                    ],
                    "correct_index": 2,
                    "explanation": "Without activation functions, a neural network is just a giant linear regression model and cannot learn complex, non-linear relationships."
                }
            ]
        }
    ]

    print(f"Seeding {len(curriculum)} expansive modules across Computer Science...")
    db.modules.insert_many(curriculum)
    
    print("Database seeding Complete! You now have a massive CS/AI Curriculum.")

if __name__ == "__main__":
    seed_database()