extra_curriculum = [
    # --- COURSE 1: Programming Fundamentals (+2) ---
    {
        "topic_id": "prog_basics_7",
        "course": "Programming Fundamentals",
        "name": "File I/O",
        "difficulty": "intermediate",
        "learning_objective": "Learn how to read from and write to external files on the disk.",
        "primary_video_url": "https://www.youtube.com/watch?v=Uh2ebFW8OYM",
        "fallback_video_url": "https://www.youtube.com/watch?v=4mX0uPQFLDU",
        "prerequisites": ["Variables and Control Flow"],
        "skills": ["file_handling"],
        "quiz": [
            {
                "question": "What happens when you open a file in 'write' (w) mode in most programming languages?",
                "options": [
                    "It appends to the end of the file",
                    "It reads the file",
                    "It overwrites the existing file or creates a new one",
                    "It throws an error if the file exists"
                ],
                "correct_index": 2,
                "explanation": "Write mode ('w') will overwrite any existing file content. To safely add to a file, append mode ('a') should be used."
            }
        ]
    },
    {
        "topic_id": "prog_basics_8",
        "course": "Programming Fundamentals",
        "name": "Functional Programming Basics",
        "difficulty": "advanced",
        "learning_objective": "Understand pure functions, immutability, and higher-order functions like map/filter/reduce.",
        "primary_video_url": "https://www.youtube.com/watch?v=e-5obm1G_FY",
        "fallback_video_url": "https://www.youtube.com/watch?v=rjo0Ew8n2wU",
        "prerequisites": ["Functions and Scope"],
        "skills": ["functional_programming"],
        "quiz": [
            {
                "question": "What is a 'pure function'?",
                "options": [
                    "A function that returns nothing",
                    "A function that only uses integers",
                    "A function that given the same input, will always return the same output and produces no side effects",
                    "A function written without loops"
                ],
                "correct_index": 2,
                "explanation": "Pure functions do not modify external state (no side effects) and have deterministic outputs based strictly on their inputs."
            }
        ]
    },

    # --- COURSE 2: Data Structures (+5) ---
    {
        "topic_id": "ds_4",
        "course": "Data Structures",
        "name": "Stacks and Queues",
        "difficulty": "beginner",
        "learning_objective": "Understand LIFO (Stack) and FIFO (Queue) data structures.",
        "primary_video_url": "https://www.youtube.com/watch?v=wjI1WNcIntg",
        "fallback_video_url": "https://www.youtube.com/watch?v=A3ZUIGTO-OA",
        "prerequisites": ["Arrays & Pointers"],
        "skills": ["linear_data_structures"],
        "quiz": [
            {
                "question": "Which principle does a Stack follow?",
                "options": ["FIFO (First In First Out)", "LIFO (Last In First Out)", "Random Access", "Sorted Access"],
                "correct_index": 1,
                "explanation": "A stack operates like a stack of plates: the last one placed on top is the first one taken off (LIFO)."
            }
        ]
    },
    {
        "topic_id": "ds_5",
        "course": "Data Structures",
        "name": "Linked Lists",
        "difficulty": "intermediate",
        "learning_objective": "Learn how nodes hold data and pointers to form non-contiguous data chains.",
        "primary_video_url": "https://www.youtube.com/watch?v=WwfhLC16nc8",
        "fallback_video_url": "https://www.youtube.com/watch?v=njTh_OwMmlA",
        "prerequisites": ["Arrays & Pointers"],
        "skills": ["linked_lists"],
        "quiz": [
            {
                "question": "What is the main advantage of a Linked List over an Array?",
                "options": [
                    "Faster access to the nth element",
                    "Takes up less memory overall",
                    "Dynamic size and efficient insertions/deletions without shifting elements",
                    "Built-in sorting"
                ],
                "correct_index": 2,
                "explanation": "Linked lists can expand indefinitely as long as there is memory, and inserting a node between two others only requires updating pointers, not moving all subsequent elements."
            }
        ]
    },
    {
        "topic_id": "ds_6",
        "course": "Data Structures",
        "name": "Heaps and Priority Queues",
        "difficulty": "advanced",
        "learning_objective": "Understand how binary heaps maintain maximum or minimum values efficiently.",
        "primary_video_url": "https://www.youtube.com/watch?v=t0Cq6tVNRBA",
        "fallback_video_url": "https://www.youtube.com/watch?v=HqPJF2L5h9U",
        "prerequisites": ["Trees and Graphs"],
        "skills": ["heaps"],
        "quiz": [
            {
                "question": "In a Max-Heap, where is the largest element located?",
                "options": ["At the deepest leaf", "At the root node", "At the rightmost node", "In the center"],
                "correct_index": 1,
                "explanation": "By definition, a Max-Heap ensures that the value of parent nodes is always greater than or equal to their children, making the root the absolute maximum."
            }
        ]
    },
    {
        "topic_id": "ds_7",
        "course": "Data Structures",
        "name": "Advanced Hash Tables",
        "difficulty": "advanced",
        "learning_objective": "Deep dive into load factors, probing, and chaining resolution methods.",
        "primary_video_url": "https://www.youtube.com/watch?v=ncHmEUmJZf4",
        "fallback_video_url": "https://www.youtube.com/watch?v=2BldESGZKB8",
        "prerequisites": ["Hash Tables Under the Hood"],
        "skills": ["collision_resolution"],
        "quiz": [
            {
                "question": "What happens during Separate Chaining collision resolution?",
                "options": [
                    "The table resizes automatically",
                    "The new element is placed in the next empty slot",
                    "The colliding elements are stored in a linked list at that index",
                    "An error is thrown"
                ],
                "correct_index": 2,
                "explanation": "Separate chaining resolves collisions by having each hash table slot act as the head of a linked list holding all elements that map to that index."
            }
        ]
    },
    {
        "topic_id": "ds_8",
        "course": "Data Structures",
        "name": "Bloom Filters",
        "difficulty": "advanced",
        "learning_objective": "Learn about probabilistic data structures used for fast space-efficient membership testing.",
        "primary_video_url": "https://www.youtube.com/watch?v=cgEjxsjB0WA",
        "fallback_video_url": "https://www.youtube.com/watch?v=V3pzxngeLqw",
        "prerequisites": ["hashing_concepts"],
        "skills": ["probabilistic_data_structures"],
        "quiz": [
            {
                "question": "What kind of error is possible with a Bloom Filter?",
                "options": ["False Positives", "False Negatives", "Both", "Neither"],
                "correct_index": 0,
                "explanation": "Bloom filters can definitively say an item is NOT in a set. However, they may occasionally produce a False Positive, saying an item IS in the set when it isn't."
            }
        ]
    },

    # --- COURSE 3: Algorithms (+5) ---
    {
        "topic_id": "algo_4",
        "course": "Algorithms",
        "name": "Graph Traversal (BFS & DFS)",
        "difficulty": "intermediate",
        "learning_objective": "Learn how to systematically explore nodes in a graph or tree.",
        "primary_video_url": "https://www.youtube.com/watch?v=tWVWeAqZ0WU",
        "fallback_video_url": "https://www.youtube.com/watch?v=pcKY4hjDrxk",
        "prerequisites": ["Trees and Graphs"],
        "skills": ["graph_algorithms"],
        "quiz": [
            {
                "question": "Which data structure is typically used to implement Breadth-First Search (BFS)?",
                "options": ["Stack", "Queue", "Hash Map", "Binary Tree"],
                "correct_index": 1,
                "explanation": "BFS explores nodes level by level, making a Queue (FIFO) the perfect data structure to track the next nodes to visit."
            }
        ]
    },
    {
        "topic_id": "algo_5",
        "course": "Algorithms",
        "name": "Greedy Algorithms",
        "difficulty": "intermediate",
        "learning_objective": "Understand algorithms that make locally optimal choices at each step.",
        "primary_video_url": "https://www.youtube.com/watch?v=HzeK7g8cD0Y",
        "fallback_video_url": "https://www.youtube.com/watch?v=ARvQcqJ_-NY",
        "prerequisites": ["Big-O & Time Complexity"],
        "skills": ["algorithmic_paradigms"],
        "quiz": [
            {
                "question": "Do greedy algorithms always produce the globally optimal solution?",
                "options": ["Yes, always", "No, they optimize locally which may not yield a global optimum", "Only for sorting arrays", "Yes, if the input is small"],
                "correct_index": 1,
                "explanation": "Greedy algorithms make the best choice at the moment. In problems like the fractional knapsack, it works perfectly, but for 0/1 knapsack, it can fail to find the global optimum."
            }
        ]
    },
    {
        "topic_id": "algo_6",
        "course": "Algorithms",
        "name": "Shortest Path (Dijkstra's Algorithm)",
        "difficulty": "advanced",
        "learning_objective": "Learn how to find the quickest route between nodes in a weighted graph.",
        "primary_video_url": "https://www.youtube.com/watch?v=EFg3u_E6eHU",
        "fallback_video_url": "https://www.youtube.com/watch?v=bZkzH5x0SKU",
        "prerequisites": ["Graph Traversal (BFS & DFS)", "Heaps and Priority Queues"],
        "skills": ["pathfinding"],
        "quiz": [
            {
                "question": "What type of edge weights cause standard Dijkstra's algorithm to fail?",
                "options": ["Zero weights", "Decimal weights", "Negative weights", "Very large weights"],
                "correct_index": 2,
                "explanation": "Dijkstra assumes that once a node is visited, its shortest path is finalized. Negative weights break this assumption. (Bellman-Ford is needed for negative weights)."
            }
        ]
    },
    {
        "topic_id": "algo_7",
        "course": "Algorithms",
        "name": "String Matching Algorithms",
        "difficulty": "advanced",
        "learning_objective": "Study efficient algorithms like KMP or Rabin-Karp to find substrings.",
        "primary_video_url": "https://www.youtube.com/watch?v=V5-7GzOfADQ",
        "fallback_video_url": "https://www.youtube.com/watch?v=GTJr8OvyEVQ",
        "prerequisites": ["Big-O & Time Complexity"],
        "skills": ["string_algorithms"],
        "quiz": [
            {
                "question": "Why is the naive string matching algorithm sometimes slow?",
                "options": [
                    "It uses too much memory",
                    "It checks from right to left only",
                    "It resets the search pointer and character comparisons after every mismatch (O(n*m))",
                    "It can't handle spaces"
                ],
                "correct_index": 2,
                "explanation": "Naive matching backtracks significantly. Efficient algorithms like KMP preprocess the pattern to skip unnecessary comparisons."
            }
        ]
    },
    {
        "topic_id": "algo_8",
        "course": "Algorithms",
        "name": "Divide and Conquer Deep Dive",
        "difficulty": "intermediate",
        "learning_objective": "Learn to break large problems down into identical smaller subproblems.",
        "primary_video_url": "https://www.youtube.com/watch?v=2Rr2tW9zvRg",
        "fallback_video_url": "https://www.youtube.com/watch?v=4VqmGXwpLqc",
        "prerequisites": ["Sorting Algorithms Deep Dive"],
        "skills": ["algorithmic_paradigms"],
        "quiz": [
            {
                "question": "Which of these is heavily reliant on the Divide and Conquer strategy?",
                "options": ["Selection Sort", "Linear Search", "Binary Search", "Breadth-First Search"],
                "correct_index": 2,
                "explanation": "Binary search continually divides the sorted search space in half until the target is found."
            }
        ]
    },

    # --- COURSE 4: Database Internals (+6) ---
    {
        "topic_id": "db_3",
        "course": "Database Internals",
        "name": "ACID Properties & Transactions",
        "difficulty": "intermediate",
        "learning_objective": "Ensure data integrity by understanding Atomicity, Consistency, Isolation, and Durability.",
        "primary_video_url": "https://www.youtube.com/watch?v=pomxJODGya4",
        "fallback_video_url": "https://www.youtube.com/watch?v=t5wg0mEUoew",
        "prerequisites": ["SQL vs NoSQL Architecture"],
        "skills": ["transaction_management"],
        "quiz": [
            {
                "question": "What does 'Atomicity' guarantee in a database transaction?",
                "options": [
                    "Data is saved perfectly",
                    "Either all sub-operations succeed, or none of them are applied",
                    "Only one user can query at a time",
                    "The database is sharded efficiently"
                ],
                "correct_index": 1,
                "explanation": "Atomicity means 'all or nothing'. If a multi-step transaction fails midway, the entire transaction rolls back to prevent inconsistent states."
            }
        ]
    },
    {
        "topic_id": "db_4",
        "course": "Database Internals",
        "name": "Database Normalization",
        "difficulty": "intermediate",
        "learning_objective": "Learn how to organize relational tables to minimize data redundancy.",
        "primary_video_url": "https://www.youtube.com/watch?v=GFQaEYEc8_8",
        "fallback_video_url": "https://www.youtube.com/watch?v=UrYLYV7WSHM",
        "prerequisites": ["SQL vs NoSQL Architecture"],
        "skills": ["relational_design"],
        "quiz": [
            {
                "question": "What is the primary goal of the 1st Normal Form (1NF)?",
                "options": [
                    "To remove all foreign keys",
                    "To ensure there are no repeating groups and all attributes are atomic",
                    "To duplicate data for faster reads",
                    "To secure the database"
                ],
                "correct_index": 1,
                "explanation": "1NF dictates that a table cell should not hold multiple values (like a comma-separated list); every column must hold atomic values."
            }
        ]
    },
    {
        "topic_id": "db_5",
        "course": "Database Internals",
        "name": "CAP Theorem",
        "difficulty": "advanced",
        "learning_objective": "Understand the fundamental tradeoffs when designing distributed systems.",
        "primary_video_url": "https://www.youtube.com/watch?v=k-Yaq8AHlFA",
        "fallback_video_url": "https://www.youtube.com/watch?v=hULJHNpcH2o",
        "prerequisites": ["SQL vs NoSQL Architecture"],
        "skills": ["distributed_systems"],
        "quiz": [
            {
                "question": "According to the CAP Theorem, a distributed system can only provide two of which three guarantees simultaneously?",
                "options": [
                    "Consistency, Availability, Partition Tolerance",
                    "Concurrency, Atomicity, Performance",
                    "Capacity, Availability, Pricing",
                    "Compute, Availability, Partition Tolerance"
                ],
                "correct_index": 0,
                "explanation": "In the event of a network failure (Partition), a system must choose to either remain Available but serve potentially stale data, or remain Consistent and refuse connections."
            }
        ]
    },
    {
        "topic_id": "db_6",
        "course": "Database Internals",
        "name": "Query Parsing & Execution Plans",
        "difficulty": "advanced",
        "learning_objective": "Look under the hood mapping SQL queries to computational execution plans.",
        "primary_video_url": "https://www.youtube.com/watch?v=HrvxzpdjEUg",
        "fallback_video_url": "https://www.youtube.com/watch?v=wTPGW1PNy_Y",
        "prerequisites": ["Indexing and Optimization"],
        "skills": ["query_profiling"],
        "quiz": [
            {
                "question": "What role does the Query Optimizer play?",
                "options": [
                    "It compresses database files",
                    "It rewrites the user interface",
                    "It evaluates different execution paths to find the most efficient way to fetch requested data",
                    "It repairs corrupted indexes"
                ],
                "correct_index": 2,
                "explanation": "The Query Optimizer analyzes indexes and table statistics to construct an execution plan that hits the disk as little as possible."
            }
        ]
    },
    {
        "topic_id": "db_7",
        "course": "Database Internals",
        "name": "Data Warehousing vs Data Lakes",
        "difficulty": "intermediate",
        "learning_objective": "Understand the differences between structured OLAP systems and raw data repositories.",
        "primary_video_url": "https://www.youtube.com/watch?v=JMWFsTeqzCE",
        "fallback_video_url": "https://www.youtube.com/watch?v=vYp4LMIGcvw",
        "prerequisites": ["SQL vs NoSQL Architecture"],
        "skills": ["big_data_architecture"],
        "quiz": [
            {
                "question": "Which of the following best describes a Data Lake?",
                "options": [
                    "A strictly relational schema tailored for fast ad-hoc queries",
                    "A massive repository storing raw, unstructured data until it is needed",
                    "An in-memory cache",
                    "A highly normalized OLTP database"
                ],
                "correct_index": 1,
                "explanation": "Data lakes use 'Schema-on-Read', allowing vast amounts of raw data (logs, images, JSON) to be saved cheaply before formatting it for analysis."
            }
        ]
    },
    {
        "topic_id": "db_8",
        "course": "Database Internals",
        "name": "In-Memory Databases",
        "difficulty": "intermediate",
        "learning_objective": "Learn why Redis and Memcached can serve data significantly faster than traditional disk-based databases.",
        "primary_video_url": "https://www.youtube.com/watch?v=G1rOthIU-uo",
        "fallback_video_url": "https://www.youtube.com/watch?v=jgpVdJB2sKQ",
        "prerequisites": ["SQL vs NoSQL Architecture"],
        "skills": ["caching"],
        "quiz": [
            {
                "question": "Why are in-memory databases like Redis heavily used for caching?",
                "options": [
                    "RAM access is magnitudes faster than solid-state or hard disk drives.",
                    "They don't require any electricity",
                    "They understand SQL natively",
                    "They can store terabytes cheaply"
                ],
                "correct_index": 0,
                "explanation": "Reading from RAM happens in nanoseconds, drastically reducing read latencies compared to disk IO."
            }
        ]
    },

    # --- COURSE 5: Artificial Intelligence (+5) ---
    {
        "topic_id": "ai_4",
        "course": "Artificial Intelligence",
        "name": "Computer Vision Fundamentals",
        "difficulty": "advanced",
        "learning_objective": "Understand how Convolutional Neural Networks (CNNs) process and classify images.",
        "primary_video_url": "https://www.youtube.com/watch?v=YRhxdVk_sIs",
        "fallback_video_url": "https://www.youtube.com/watch?v=FTr3n7uBIuE",
        "prerequisites": ["Neural Networks & Deep Learning"],
        "skills": ["computer_vision"],
        "quiz": [
            {
                "question": "What does a Convolution layer do in a CNN?",
                "options": [
                    "It translates text",
                    "It applies specific filters (kernels) to an image to detect features like edges or textures",
                    "It sorts the array elements",
                    "It connects to a database"
                ],
                "correct_index": 1,
                "explanation": "Convolutional layers slide filters over the image mathematically to extract hierarchical visual features."
            }
        ]
    },
    {
        "topic_id": "ai_5",
        "course": "Artificial Intelligence",
        "name": "Reinforcement Learning",
        "difficulty": "advanced",
        "learning_objective": "Learn how agents maximize cumulative rewards by interacting with environments.",
        "primary_video_url": "https://www.youtube.com/watch?v=JgvyzIkgxF0",
        "fallback_video_url": "https://www.youtube.com/watch?v=cO5g5qLrLCE",
        "prerequisites": ["Intro to Machine Learning"],
        "skills": ["reinforcement_learning"],
        "quiz": [
            {
                "question": "In Reinforcement Learning, what defines the feedback an agent receives?",
                "options": [
                    "A predefined label dataset",
                    "Reward or punishment signals based on actions taken in a given state",
                    "A set of unsupervised clusters",
                    "HTML inputs"
                ],
                "correct_index": 1,
                "explanation": "RL relies on a reward function. The agent explores the environment, receiving positive or negative rewards guiding it toward an optimal policy."
            }
        ]
    },
    {
        "topic_id": "ai_6",
        "course": "Artificial Intelligence",
        "name": "Generative AI & LLMs",
        "difficulty": "advanced",
        "learning_objective": "Explore Large Language Models, self-attention mechanisms, and the Transformer architecture.",
        "primary_video_url": "https://www.youtube.com/watch?v=zjkBMFhNj_g",
        "fallback_video_url": "https://www.youtube.com/watch?v=bQ5BoolX9Ag",
        "prerequisites": ["Natural Language Processing (NLP)"],
        "skills": ["generative_ai"],
        "quiz": [
            {
                "question": "What was the game-changing mechanism introduced by the 'Attention Is All You Need' paper?",
                "options": [
                    "Recurrent Connections",
                    "Self-Attention mechanism, resolving long-range context efficiently",
                    "Convolutional filters for text",
                    "Backpropagation"
                ],
                "correct_index": 1,
                "explanation": "Self-attention allows the model to look at all other words in a sentence simultaneously to deeply understand context and intent."
            }
        ]
    },
    {
        "topic_id": "ai_7",
        "course": "Artificial Intelligence",
        "name": "Model Evaluation",
        "difficulty": "intermediate",
        "learning_objective": "Understand Precision, Recall, F1 Score, and Confusion Matrices.",
        "primary_video_url": "https://www.youtube.com/watch?v=Kdsp6soqA7o",
        "fallback_video_url": "https://www.youtube.com/watch?v=4jRBRDbJemM",
        "prerequisites": ["Intro to Machine Learning"],
        "skills": ["ml_evaluation"],
        "quiz": [
            {
                "question": "If you are building a spam filter and want to make sure you ALMOST NEVER classify an important email as spam, what metric should you prioritize?",
                "options": [
                    "Recall",
                    "Precision",
                    "Accuracy",
                    "Mean Squared Error"
                ],
                "correct_index": 1,
                "explanation": "High precision means when the model says 'Spam', it's almost certainly correct (minimizing False Positives)."
            }
        ]
    },
    {
        "topic_id": "ai_8",
        "course": "Artificial Intelligence",
        "name": "Bias and Ethics in AI",
        "difficulty": "beginner",
        "learning_objective": "Recognize algorithmic bias and the ethical responsibilities of building AI.",
        "primary_video_url": "https://www.youtube.com/watch?v=gV0_raZR2PM",
        "fallback_video_url": "https://www.youtube.com/watch?v=59bMh59JQDo",
        "prerequisites": ["Intro to Machine Learning"],
        "skills": ["ai_ethics"],
        "quiz": [
            {
                "question": "Where does algorithmic prejudice or bias primarily originate?",
                "options": [
                    "The neural networks decide to be malicious",
                    "The training data already reflects historical or human biases",
                    "Programming languages inherently introduce bias",
                    "Computers read the news"
                ],
                "correct_index": 1,
                "explanation": "Models are statistical mirrors. If trained on biased historical human decisions or unrepresentative datasets, they will replicate and scale those biases."
            }
        ]
    },

    # --- COURSE 6: Web Development (+6) ---
    {
        "topic_id": "web_3",
        "course": "Web Development",
        "name": "CSS Frameworks (Tailwind)",
        "difficulty": "intermediate",
        "learning_objective": "Speed up styling using utility-first CSS frameworks.",
        "primary_video_url": "https://www.youtube.com/watch?v=lCxcTsOHrjo",
        "fallback_video_url": "https://www.youtube.com/watch?v=pfaSUYaSgRo",
        "prerequisites": ["HTML & CSS Basics"],
        "skills": ["css_frameworks"],
        "quiz": [
            {
                "question": "What is the specific methodology behind Tailwind CSS?",
                "options": [
                    "It prebuilds large components like Bootstrap",
                    "Utility-first: composing styles using small, single-purpose classes directly in HTML",
                    "It uses Python to generate CSS",
                    "It removes all styles"
                ],
                "correct_index": 1,
                "explanation": "Tailwind provides low-level utility classes (like flex, pt-4, text-center) that let you build custom designs without writing custom CSS."
            }
        ]
    },
    {
        "topic_id": "web_4",
        "course": "Web Development",
        "name": "Frontend Frameworks (React)",
        "difficulty": "advanced",
        "learning_objective": "Build dynamic Component-based user interfaces with React.",
        "primary_video_url": "https://www.youtube.com/watch?v=bMknfKXIFA8",
        "fallback_video_url": "https://www.youtube.com/watch?v=RGKi6LSPDLU",
        "prerequisites": ["JavaScript in the Browser"],
        "skills": ["react_fundamentals"],
        "quiz": [
            {
                "question": "What makes React update the UI efficiently?",
                "options": [
                    "It re-downloads the page constantly",
                    "It uses a Virtual DOM to compute minimal changes before updating the real DOM",
                    "It compresses images automatically",
                    "It converts JavaScript to WebAssembly"
                ],
                "correct_index": 1,
                "explanation": "The Virtual DOM acts as an optimized middleman. React calculates diffs on the virtual tree, applying only the necessary changes to the much slower actual DOM."
            }
        ]
    },
    {
        "topic_id": "web_5",
        "course": "Web Development",
        "name": "Backend Engineering (Node.js/Express)",
        "difficulty": "intermediate",
        "learning_objective": "Learn to write server-side code and create HTTP servers with JavaScript.",
        "primary_video_url": "https://www.youtube.com/watch?v=TlB_eWDSMt4",
        "fallback_video_url": "https://www.youtube.com/watch?v=Oe421EPjeBE",
        "prerequisites": ["JavaScript in the Browser"],
        "skills": ["backend_basics"],
        "quiz": [
            {
                "question": "What does Node.js allow developers to do?",
                "options": [
                    "Run Python scripts in Chrome",
                    "Design CSS easily",
                    "Execute JavaScript outside of a web browser (e.g., on a server)",
                    "Compile code to machine language instantly"
                ],
                "correct_index": 2,
                "explanation": "Node.js utilizes the V8 engine to run JS externally, opening the door for full-stack JavaScript development."
            }
        ]
    },
    {
        "topic_id": "web_6",
        "course": "Web Development",
        "name": "RESTful APIs",
        "difficulty": "intermediate",
        "learning_objective": "Understand API architecture for client-server communication.",
        "primary_video_url": "https://www.youtube.com/watch?v=-mN3VyJuCjM",
        "fallback_video_url": "https://www.youtube.com/watch?v=lsMQRaeKNDk",
        "prerequisites": ["Backend Engineering (Node.js/Express)"],
        "skills": ["api_design"],
        "quiz": [
            {
                "question": "Which HTTP method should be used to partially update an existing resource?",
                "options": ["GET", "POST", "PATCH", "DELETE"],
                "correct_index": 2,
                "explanation": "While PUT replaces the entire resource, PATCH is the semantic standard for applying partial modifications."
            }
        ]
    },
    {
        "topic_id": "web_7",
        "course": "Web Development",
        "name": "Authentication & JWTs",
        "difficulty": "advanced",
        "learning_objective": "Implement secure login systems using JSON Web Tokens.",
        "primary_video_url": "https://www.youtube.com/watch?v=mbsmsiPbOoo",
        "fallback_video_url": "https://www.youtube.com/watch?v=7Q17ubqLfaM",
        "prerequisites": ["RESTful APIs"],
        "skills": ["web_security"],
        "quiz": [
            {
                "question": "What is the key benefit of JSON Web Tokens (JWT) for authentication?",
                "options": [
                    "They hide all user data through encryption",
                    "They allow the server to remain stateless because the token itself carries valid user information securely signed",
                    "They run faster than cookies",
                    "They cannot be stolen"
                ],
                "correct_index": 1,
                "explanation": "Because JWTs contain a cryptographic signature, servers can verify the user's identity simply by validating the token, without querying a central database for active sessions."
            }
        ]
    },
    {
        "topic_id": "web_8",
        "course": "Web Development",
        "name": "WebSockets for Real-Time",
        "difficulty": "advanced",
        "learning_objective": "Establish persistent two-way communication channels between client and server.",
        "primary_video_url": "https://www.youtube.com/watch?v=8ARodQ4Wlf4",
        "fallback_video_url": "https://www.youtube.com/watch?v=1BfCnjr_Vjg",
        "prerequisites": ["Backend Engineering (Node.js/Express)"],
        "skills": ["realtime_communication"],
        "quiz": [
            {
                "question": "How do WebSockets differ fundamentally from standard HTTP requests?",
                "options": [
                    "They only transfer images",
                    "HTTP requests are unidirectional and close after response; WebSockets establish an open, persistent bi-directional connection.",
                    "WebSockets are always less secure",
                    "WebSockets compress data automatically"
                ],
                "correct_index": 1,
                "explanation": "Once a WebSocket handshake is complete, data can seamlessly stream back and forth continuously without establishing new connections per message."
            }
        ]
    },

    # --- COURSE 7: Operating Systems (+6) ---
    {
        "topic_id": "os_3",
        "course": "Operating Systems",
        "name": "Memory Allocation",
        "difficulty": "intermediate",
        "learning_objective": "Examine how operating systems dish out RAM using methods like First-Fit vs Best-Fit.",
        "primary_video_url": "https://www.youtube.com/watch?v=qcBIb1U4-x0",
        "fallback_video_url": "https://www.youtube.com/watch?v=E-b0LwEwGeg",
        "prerequisites": ["Processes and Threads"],
        "skills": ["os_memory"],
        "quiz": [
            {
                "question": "What is external fragmentation?",
                "options": [
                    "When the hard drive shatters",
                    "When total free memory space is adequate for a request, but it is not contiguous",
                    "Memory allocated is slightly larger than requested",
                    "A virus attack"
                ],
                "correct_index": 1,
                "explanation": "External fragmentation happens as processes load and unload, leaving tiny scattered memory gaps that sum up to a large total but are individually useless for new large requests."
            }
        ]
    },
    {
        "topic_id": "os_4",
        "course": "Operating Systems",
        "name": "Virtual Memory & Paging",
        "difficulty": "advanced",
        "learning_objective": "Learn how the OS tricks programs into thinking they have more RAM than physically exists.",
        "primary_video_url": "https://www.youtube.com/watch?v=qlH4-oHnBb8",
        "fallback_video_url": "https://www.youtube.com/watch?v=3RAtNqgNnqw",
        "prerequisites": ["Memory Allocation"],
        "skills": ["virtual_memory"],
        "quiz": [
            {
                "question": "What is a 'Page Fault'?",
                "options": [
                    "A hardware breakdown",
                    "When a program crashes on a web page",
                    "When an application asks for memory that is not currently mapped in physical RAM and must be fetched from the disk",
                    "A security violation"
                ],
                "correct_index": 2,
                "explanation": "Page faults are routinely handled by the OS which pauses the process, fetches the required memory 'page' from the hard drive swap space, and resumes."
            }
        ]
    },
    {
        "topic_id": "os_5",
        "course": "Operating Systems",
        "name": "File System Architecture",
        "difficulty": "intermediate",
        "learning_objective": "Understand how bytes on a disk platter translate to logical folders and files.",
        "primary_video_url": "https://www.youtube.com/watch?v=n2AAhiCGmAo",
        "fallback_video_url": "https://www.youtube.com/watch?v=v=zE_aA_K_hQE",
        "prerequisites": ["Memory Allocation"],
        "skills": ["file_systems"],
        "quiz": [
            {
                "question": "What is an INODE in a typical Unix/Linux file system?",
                "options": [
                    "A text editor",
                    "An internet node",
                    "A data structure describing file metadata (permissions, disk blocks, timestamps) without the file name",
                    "A folder"
                ],
                "correct_index": 2,
                "explanation": "Inodes hold all structural and permission information about a file. The directory structure merely links human-readable filenames to these inodes."
            }
        ]
    },
    {
        "topic_id": "os_6",
        "course": "Operating Systems",
        "name": "I/O Subsystems",
        "difficulty": "advanced",
        "learning_objective": "Observe how the CPU interacts with vastly slower hardware peripherals like keyboards and disks.",
        "primary_video_url": "https://www.youtube.com/watch?v=1b-N7D-h50E",
        "fallback_video_url": "https://www.youtube.com/watch?v=i9YQJvQdwtg",
        "prerequisites": ["Processes and Threads"],
        "skills": ["device_management"],
        "quiz": [
            {
                "question": "How does an interrupt-driven I/O system improve efficiency?",
                "options": [
                    "It makes the CPU run faster",
                    "It removes necessity for RAM",
                    "The CPU does not waste time continuously checking if data is ready (polling); the device alerts the CPU exactly when needed.",
                    "It compresses peripheral data"
                ],
                "correct_index": 2,
                "explanation": "Interrupts allow the CPU to execute other processes while waiting for slow devices to finish their work."
            }
        ]
    },
    {
        "topic_id": "os_7",
        "course": "Operating Systems",
        "name": "Virtualization & Hypervisors",
        "difficulty": "intermediate",
        "learning_objective": "Differentiate between running multiple operating systems natively or virtually.",
        "primary_video_url": "https://www.youtube.com/watch?v=GiaHBGPMkE0",
        "fallback_video_url": "https://www.youtube.com/watch?v=A8eG2K4hIfU",
        "prerequisites": ["Virtual Memory & Paging"],
        "skills": ["virtualization"],
        "quiz": [
            {
                "question": "What is the distinction of a Type 1 (Bare Metal) Hypervisor?",
                "options": [
                    "It handles audio specifically",
                    "It runs directly on the server's hardware to control the hardware directly, bypass a host OS",
                    "It runs as an app on MacOS",
                    "It only virtualizes storage"
                ],
                "correct_index": 1,
                "explanation": "Type 1 hypervisors like VMware ESXi run directly on the physical hardware for maximum performance, unlike Type 2 (like VirtualBox) which run atop a host OS."
            }
        ]
    },
    {
        "topic_id": "os_8",
        "course": "Operating Systems",
        "name": "Containerization (Docker)",
        "difficulty": "intermediate",
        "learning_objective": "Package applications with all their dependencies to run reliably anywhere.",
        "primary_video_url": "https://www.youtube.com/watch?v=Gjnup-PuquQ",
        "fallback_video_url": "https://www.youtube.com/watch?v=pTFZFxd4hOI",
        "prerequisites": ["Virtualization & Hypervisors"],
        "skills": ["docker_fundamentals"],
        "quiz": [
            {
                "question": "How do containers primarily differ from Virtual Machines?",
                "options": [
                    "Containers are slower",
                    "Containers share the host's OS kernel making them significantly lighter and faster to boot",
                    "Containers require specific hardware",
                    "There is no difference"
                ],
                "correct_index": 1,
                "explanation": "While VMs virtualize the entire hardware stack and run a full guest OS, Containers securely isolate applications but share the same base kernel, dropping massive overhead."
            }
        ]
    },

    # --- COURSE 8: Computer Networks (+6) ---
    {
        "topic_id": "net_3",
        "course": "Computer Networks",
        "name": "IP Addressing & Subnetting",
        "difficulty": "intermediate",
        "learning_objective": "Divide the global internet logically using IPv4/IPv6 architectures and Subnet Masks.",
        "primary_video_url": "https://www.youtube.com/watch?v=VCvd_hXq32s",
        "fallback_video_url": "https://www.youtube.com/watch?v=s_Ntt6eTN94",
        "prerequisites": ["OSI Model and TCP/IP"],
        "skills": ["networking_infrastructure"],
        "quiz": [
            {
                "question": "What does a Subnet Mask dictate?",
                "options": [
                    "The password for the WiFi",
                    "Which portion of the IP address represents the Network, and which represents the Host",
                    "The encryption level of data",
                    "The physical ethernet cable type"
                ],
                "correct_index": 1,
                "explanation": "The subnet mask is used by devices to determine whether an IP address belongs to the local network or internet/remote network."
            }
        ]
    },
    {
        "topic_id": "net_4",
        "course": "Computer Networks",
        "name": "Routing Protocols",
        "difficulty": "advanced",
        "learning_objective": "Discover how internet routers dynamically figure out the physical path data needs to travel.",
        "primary_video_url": "https://www.youtube.com/watch?v=nEswLh2vJjQ",
        "fallback_video_url": "https://www.youtube.com/watch?v=U36h_3_TkhM",
        "prerequisites": ["IP Addressing & Subnetting"],
        "skills": ["routing"],
        "quiz": [
            {
                "question": "Which of these is an example of an Interior Gateway distance-vector routing protocol?",
                "options": ["BGP", "HTTP", "RIP (Routing Information Protocol)", "UDP"],
                "correct_index": 2,
                "explanation": "RIP is a classic distance-vector protocol using hop-count as a routing metric."
            }
        ]
    },
    {
        "topic_id": "net_5",
        "course": "Computer Networks",
        "name": "DNS Architecture",
        "difficulty": "beginner",
        "learning_objective": "Understand the 'phonebook of the internet' mapping human names to IP addresses.",
        "primary_video_url": "https://www.youtube.com/watch?v=mpQZVYPuDGU",
        "fallback_video_url": "https://www.youtube.com/watch?v=2ZUxoi7YNqc",
        "prerequisites": ["OSI Model and TCP/IP"],
        "skills": ["dns_resolution"],
        "quiz": [
            {
                "question": "If your local DNS cache cannot find the IP address for google.com, what server type does it query first?",
                "options": ["Top-Level Domain Server", "Root Name Server", "Authoritative Name Server", "Web Server"],
                "correct_index": 1,
                "explanation": "The resolution process generally hits the highly powerful Root Name Servers first to determine the TLD (like .com) server location."
            }
        ]
    },
    {
        "topic_id": "net_6",
        "course": "Computer Networks",
        "name": "HTTP Protocol Deep Dive",
        "difficulty": "intermediate",
        "learning_objective": "Examine headers, status codes, and the mechanics of web requests.",
        "primary_video_url": "https://www.youtube.com/watch?v=iYM2zFP3Zn0",
        "fallback_video_url": "https://www.youtube.com/watch?v=KzPNrEaWc4k",
        "prerequisites": ["OSI Model and TCP/IP"],
        "skills": ["application_layer"],
        "quiz": [
            {
                "question": "What broad problem does an HTTP 500 status code represent?",
                "options": [
                    "Client input error",
                    "Success",
                    "Internal Server Error (Backend failure)",
                    "Resource not found"
                ],
                "correct_index": 2,
                "explanation": "5xx status codes mean the client's request was seemingly valid, but the server failed to fulfill it due to an unexpected error on their end."
            }
        ]
    },
    {
        "topic_id": "net_7",
        "course": "Computer Networks",
        "name": "TLS and HTTPS",
        "difficulty": "advanced",
        "learning_objective": "Learn about asymmetric encryption, certificates, and the mathematical safety underpinning eCommerce.",
        "primary_video_url": "https://www.youtube.com/watch?v=T4Df5_cojAs",
        "fallback_video_url": "https://www.youtube.com/watch?v=j9QmMEWmcfo",
        "prerequisites": ["Network Security Fundamentals"],
        "skills": ["network_encryption"],
        "quiz": [
            {
                "question": "In Public Key Cryptography, if I encrypt data with someone's Public Key, what is exclusively needed to decrypt it?",
                "options": [
                    "The same Public Key",
                    "A master password",
                    "Their unique Private Key",
                    "An SSL certificate"
                ],
                "correct_index": 2,
                "explanation": "Asymmetric encryption relies on a mathematically paired public-private key set. The public key locks the message, and strictly only the corresponding private key can unlock it."
            }
        ]
    },
    {
        "topic_id": "net_8",
        "course": "Computer Networks",
        "name": "Load Balancing and Proxies",
        "difficulty": "advanced",
        "learning_objective": "Handle massive traffic by distributing requests across multiple backend servers.",
        "primary_video_url": "https://www.youtube.com/watch?v=K0Ta65OqQkY",
        "fallback_video_url": "https://www.youtube.com/watch?v=1b-N7D-h50E",
        "prerequisites": ["HTTP Protocol Deep Dive", "OSI Model and TCP/IP"],
        "skills": ["system_design"],
        "quiz": [
            {
                "question": "What is the purpose of a Reverse Proxy?",
                "options": [
                    "To hide the client's IP from the server",
                    "To sit in front of backend servers, handling tasks like SSL termination and directing client requests",
                    "To block all incoming traffic",
                    "To encrypt database passwords"
                ],
                "correct_index": 1,
                "explanation": "While a forward proxy protects clients, a Reverse Proxy protects and balances traffic for servers, acting as a unified entry point."
            }
        ]
    }
]
