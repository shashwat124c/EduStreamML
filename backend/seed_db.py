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
        {
            "topic_id": "prog_basics_3",
            "course": "Programming Fundamentals",
            "name": "Control Flow: Conditionals and Loops",
            "difficulty": "beginner",
            "learning_objective": "Learn how to make decisions in code using if/else statements and repeat actions using for and while loops.",
            "primary_video_url": "https://www.youtube.com/watch?v=PqFKRqpHrjw",
            "fallback_video_url": "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ",
            "prerequisites": ["Intro to Programming & Variables"],
            "skills": ["conditional_logic", "iteration"],
            "quiz": [
                {
                    "question": "Which of the following is the best use case for a 'while' loop?",
                    "options": [
                        "Iterating exactly 10 times",
                        "Repeating an action until a specific condition becomes false",
                        "Declaring a new variable",
                        "Stopping a program from running"
                    ],
                    "correct_index": 1,
                    "explanation": "While loops are designed to run indefinitely as long as their condition evaluates to true, making them perfect for unpredictable iteration counts."
                }
            ]
        },
        {
            "topic_id": "prog_basics_4",
            "course": "Programming Fundamentals",
            "name": "Functions and Scope",
            "difficulty": "intermediate",
            "learning_objective": "Understand how to write reusable blocks of code and learn the rules of variable visibility (local vs. global scope).",
            "primary_video_url": "https://www.youtube.com/watch?v=NSZA4qxyTNE",
            "fallback_video_url": "https://www.youtube.com/watch?v=R8SjM4DKK80",
            "prerequisites": ["Intro to Programming & Variables"],
            "skills": ["modular_programming", "scoping"],
            "quiz": [
                {
                    "question": "If a variable is declared inside a function, can it be accessed directly from outside that function?",
                    "options": [
                        "Yes, always",
                        "Only if it is an integer",
                        "No, it has local scope",
                        "Yes, but only in Python"
                    ],
                    "correct_index": 2,
                    "explanation": "Variables declared inside a function have 'local scope' and are destroyed once the function finishes executing."
                }
            ]
        },
        {
            "topic_id": "prog_basics_5",
            "course": "Programming Fundamentals",
            "name": "Error Handling and Debugging",
            "difficulty": "intermediate",
            "learning_objective": "Learn how to identify, read, and handle common runtime and syntax errors safely using try/catch blocks.",
            "primary_video_url": "https://www.youtube.com/watch?v=NIWwJbo-9_8",
            "fallback_video_url": "https://www.youtube.com/watch?v=1b-N7D-h50E",
            "prerequisites": ["Functions and Scope"],
            "skills": ["debugging", "exception_handling"],
            "quiz": [
                {
                    "question": "What is the primary purpose of a try/catch (or try/except) block?",
                    "options": [
                        "To make the code run faster",
                        "To safely handle errors without crashing the entire program",
                        "To create an infinite loop",
                        "To define a new function"
                    ],
                    "correct_index": 1,
                    "explanation": "Try/catch blocks allow developers to 'catch' exceptions when things go wrong and handle them gracefully instead of the application crashing abruptly."
                }
            ]
        },
        {
            "topic_id": "prog_basics_6",
            "course": "Programming Fundamentals",
            "name": "Object-Oriented Programming (OOP)",
            "difficulty": "intermediate",
            "learning_objective": "Learn the four pillars of OOP: Encapsulation, Abstraction, Inheritance, and Polymorphism.",
            "primary_video_url": "https://www.youtube.com/watch?v=pTB0EiLXUC8",
            "fallback_video_url": "https://www.youtube.com/watch?v=m_MQYyJpIjg",
            "prerequisites": ["Functions and Scope"],
            "skills": ["object_oriented_design"],
            "quiz": [
                {
                    "question": "Which OOP principle involves hiding the internal state and requiring all interaction to be performed through an object's methods?",
                    "options": [
                        "Inheritance",
                        "Polymorphism",
                        "Encapsulation",
                        "Abstraction"
                    ],
                    "correct_index": 2,
                    "explanation": "Encapsulation bundles the data (attributes) and methods that operate on the data into a single unit (class), hiding the internal representation from the outside."
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
        {
            "topic_id": "ds_3",
            "course": "Data Structures",
            "name": "Trees and Graphs",
            "difficulty": "advanced",
            "learning_objective": "Explore non-linear data structures like Binary Search Trees, Tries, and directed/undirected graphs.",
            "primary_video_url": "https://www.youtube.com/watch?v=oSWTXtMglKE",
            "fallback_video_url": "https://www.youtube.com/watch?v=tWVWeAqZ0WU",
            "prerequisites": ["contiguous_memory", "pointer_arithmetic"],
            "skills": ["graph_theory", "tree_traversal"],
            "quiz": [
                {
                    "question": "In a Binary Search Tree (BST), where are smaller values placed relative to the root node?",
                    "options": [
                        "Always on the right",
                        "Always on the left",
                        "They are placed randomly",
                        "At the very bottom leaf nodes"
                    ],
                    "correct_index": 1,
                    "explanation": "In a correctly formulated BST, the left child of a node contains a value less than the parent node, and the right child contains a higher value."
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
        {
            "topic_id": "algo_3",
            "course": "Algorithms",
            "name": "Dynamic Programming",
            "difficulty": "advanced",
            "learning_objective": "Learn how to optimize complex algorithms by breaking problems down and storing the results of subproblems.",
            "primary_video_url": "https://www.youtube.com/watch?v=oBt53YbR9Kk",
            "fallback_video_url": "https://www.youtube.com/watch?v=aPQY__2H3tE",
            "prerequisites": ["algorithmic_thinking", "recursive_logic"],
            "skills": ["dynamic_programming", "memoization"],
            "quiz": [
                {
                    "question": "What is the core technique used in Dynamic Programming to avoid redundant calculations?",
                    "options": [
                        "Memoization",
                        "Multithreading",
                        "Polymorphism",
                        "Garbage Collection"
                    ],
                    "correct_index": 0,
                    "explanation": "Memoization involves caching the results of expensive function calls and returning the cached result when the same inputs occur again."
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
        {
            "topic_id": "db_2",
            "course": "Database Internals",
            "name": "Indexing and Optimization",
            "difficulty": "intermediate",
            "learning_objective": "Understand how B-Trees and Hash Indexes dramatically speed up database queries.",
            "primary_video_url": "https://www.youtube.com/watch?v=-qRSjqNWgYQ",
            "fallback_video_url": "https://www.youtube.com/watch?v=HrvxzpdjEUg",
            "prerequisites": ["schema_design"],
            "skills": ["query_optimization", "indexing"],
            "quiz": [
                {
                    "question": "Which data structure is most commonly used by relational databases for indexing?",
                    "options": [
                        "Linked List",
                        "Queue",
                        "B-Tree (or B+ Tree)",
                        "Stack"
                    ],
                    "correct_index": 2,
                    "explanation": "B+ Trees are widely used for DB indexing because their branching factor is large, keeping the tree shallow and minimizing expensive disk I/O reads."
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
        },
        {
            "topic_id": "ai_3",
            "course": "Artificial Intelligence",
            "name": "Natural Language Processing (NLP)",
            "difficulty": "advanced",
            "learning_objective": "Discover how computers process and generate human language using techniques like embeddings and transformers.",
            "primary_video_url": "https://www.youtube.com/watch?v=fNxaJsNG3-s",
            "fallback_video_url": "https://www.youtube.com/watch?v=XcgHO16cZyQ",
            "prerequisites": ["neural_networks", "ml_basics"],
            "skills": ["nlp_fundamentals"],
            "quiz": [
                {
                    "question": "What does an 'Embedding' do in NLP?",
                    "options": [
                        "It translates code to binary",
                        "It creates a graphical user interface for texts",
                        "It maps words to dense vectors of numbers where similar words have similar vectors",
                        "It prevents syntax errors in code"
                    ],
                    "correct_index": 2,
                    "explanation": "Word embeddings capture semantic meaning by mapping words to points in a high-dimensional mathematical space, letting AI perform math on relationships (like King - Man + Woman = Queen)."
                }
            ]
        },

        # --- COURSE 6: Web Development ---
        {
            "topic_id": "web_1",
            "course": "Web Development",
            "name": "HTML & CSS Basics",
            "difficulty": "beginner",
            "learning_objective": "Learn the building blocks of the web and how to style them.",
            "primary_video_url": "https://www.youtube.com/watch?v=mU6anWqZJcc",
            "fallback_video_url": "https://www.youtube.com/watch?v=G3e-cpL7ofc",
            "prerequisites": [],
            "skills": ["html_css_basics"],
            "quiz": [
                {
                    "question": "Which HTML tag is used to define the deepest level heading?",
                    "options": [
                        "<h1>",
                        "<heading>",
                        "<h6>",
                        "<h9>"
                    ],
                    "correct_index": 2,
                    "explanation": "<h1> is the highest level (largest) heading, and <h6> is the lowest level (smallest) standard HTML heading."
                }
            ]
        },
        {
            "topic_id": "web_2",
            "course": "Web Development",
            "name": "JavaScript in the Browser",
            "difficulty": "intermediate",
            "learning_objective": "Add interactivity to web pages using vanilla JavaScript and the DOM API.",
            "primary_video_url": "https://www.youtube.com/watch?v=W6NZfCO5SIk",
            "fallback_video_url": "https://www.youtube.com/watch?v=upDLs1sn7g4",
            "prerequisites": ["html_css_basics", "variables_and_control_flow"],
            "skills": ["dom_manipulation"],
            "quiz": [
                {
                    "question": "What is the DOM?",
                    "options": [
                        "Data Object Model",
                        "Document Object Model",
                        "Desktop Orientation Mode",
                        "Digital Operation Machine"
                    ],
                    "correct_index": 1,
                    "explanation": "The Document Object Model (DOM) is a programming interface for web documents, representing the page so that programs can change the document structure, style, and content."
                }
            ]
        },

        # --- COURSE 7: Operating Systems ---
        {
            "topic_id": "os_1",
            "course": "Operating Systems",
            "name": "Processes and Threads",
            "difficulty": "intermediate",
            "learning_objective": "Understand how the OS manages executing programs and multiple streams of execution.",
            "primary_video_url": "https://www.youtube.com/watch?v=OrM7nZcxXZU",
            "fallback_video_url": "https://www.youtube.com/watch?v=4rLW7zg21gI",
            "prerequisites": ["memory_management"],
            "skills": ["concurrency", "process_management"],
            "quiz": [
                {
                    "question": "What is the primary difference between a process and a thread?",
                    "options": [
                        "Threads are heavier and consume more memory than processes.",
                        "A process has its own isolated memory space, while threads within the same process share memory.",
                        "Processes can only run on single-core CPUs.",
                        "There is no difference."
                    ],
                    "correct_index": 1,
                    "explanation": "Processes are isolated execution environments, whereas threads are lightweight units of execution that share the memory and resources of their parent process."
                }
            ]
        },
        {
            "topic_id": "os_2",
            "course": "Operating Systems",
            "name": "Concurrency and Deadlocks",
            "difficulty": "advanced",
            "learning_objective": "Learn about the challenges of concurrent programming, such as race conditions and deadlocks, and how to resolve them.",
            "primary_video_url": "https://www.youtube.com/watch?v=rrsJ4O9gCxo",
            "fallback_video_url": "https://www.youtube.com/watch?v=oq29KUy29iQ",
            "prerequisites": ["concurrency", "process_management"],
            "skills": ["synchronization"],
            "quiz": [
                {
                    "question": "Which of the following is NOT one of the Coffman conditions required for a deadlock to occur?",
                    "options": [
                        "Mutual Exclusion",
                        "Hold and Wait",
                        "Preemption",
                        "Circular Wait"
                    ],
                    "correct_index": 2,
                    "explanation": "The four conditions for deadlock are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. If preemption is allowed, deadlocks can be broken."
                }
            ]
        },

        # --- COURSE 8: Computer Networks ---
        {
            "topic_id": "net_1",
            "course": "Computer Networks",
            "name": "OSI Model and TCP/IP",
            "difficulty": "beginner",
            "learning_objective": "Learn the conceptual layers of network communication and the fundamental protocols of the internet.",
            "primary_video_url": "https://www.youtube.com/watch?v=vv4y_uOneC0",
            "fallback_video_url": "https://www.youtube.com/watch?v=3b_TAYtzuho",
            "prerequisites": [],
            "skills": ["networking_basics"],
            "quiz": [
                {
                    "question": "Which layer of the OSI model is responsible for reliable end-to-end data transfer?",
                    "options": [
                        "Physical Layer",
                        "Network Layer",
                        "Transport Layer",
                        "Application Layer"
                    ],
                    "correct_index": 2,
                    "explanation": "The Transport Layer (Layer 4), where TCP operates, ensures that data is reliably and sequentially delivered between host applications."
                }
            ]
        },
        {
            "topic_id": "net_2",
            "course": "Computer Networks",
            "name": "Network Security Fundamentals",
            "difficulty": "intermediate",
            "learning_objective": "Understand essential network security concepts, including encryption, firewalls, and common attacks.",
            "primary_video_url": "https://www.youtube.com/watch?v=inWWhr5tnEA",
            "fallback_video_url": "https://www.youtube.com/watch?v=bPVaOlJ6ln0",
            "prerequisites": ["networking_basics"],
            "skills": ["cybersecurity_basics"],
            "quiz": [
                {
                    "question": "What is the main purpose of a firewall?",
                    "options": [
                        "To physically protect servers from fire",
                        "To encrypt all wireless traffic",
                        "To monitor and control incoming and outgoing network traffic based on predetermined security rules",
                        "To speed up the internet connection"
                    ],
                    "correct_index": 2,
                    "explanation": "A firewall acts as a barrier between a trusted internal network and an untrusted external network, filtering traffic based on security policies."
                }
            ]
        }
    ]

    from additional_topics import extra_curriculum
    curriculum.extend(extra_curriculum)

    print(f"Seeding {len(curriculum)} expansive modules across Computer Science...")
    db.modules.insert_many(curriculum)
    
    print("Database seeding Complete! You now have a massive CS/AI Curriculum.")

if __name__ == "__main__":
    seed_database()