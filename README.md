# EduStreamAI 🚀
**An Intelligent, Path-Based Learning Management System (LMS)**

EduStreamAI is a modern web application designed to help students master technical subjects through structured dependency graphs and diagnostic knowledge checks. Unlike traditional video platforms, EduStreamAI ensures a student has the foundational knowledge required before proceeding to advanced modules.

## ✨ Core Features
- **Dynamic Curriculum Roadmap:** Courses are broken down into logical modules with a clear dependency graph.
- **Diagnostic Knowledge Checks:** Integrated MCQ-based "Gateways" that assess user readiness for a topic.
- **Intelligent Routing:** If a user fails a diagnostic check, the system identifies knowledge gaps and recommends prerequisite content.
- **Google OAuth 2.0 Integration:** Secure authentication and personalized progress tracking.
- **Modern Tech Stack:** A sleek, responsive UI built with React and Tailwind CSS v4.

## 🛠️ Technology Stack
- **Frontend:** React.js, Vite, Tailwind CSS v4, Axios
- **Backend:** Python, Flask, Flask-CORS
- **Database:** MongoDB (NoSQL)
- **Auth:** Google OAuth 2.0 (JWT Verification)

## 🏗️ Project Structure
```text
EduStreamAI/
├── backend/
│   ├── app.py             # Flask API & Auth Logic
│   ├── seed_db.py         # Database Seeding Script
│   └── requirements.txt   # Python Dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Main Logic & Routing
│   │   └── index.css      # Tailwind Styles
│   ├── .env               # Google Client ID (Local Only)
│   └── package.json       # Node Dependencies
└── README.md
```

##🚀 Getting Started
**1. Backend Setup
```text
cd backend
python -m venv myenv
source myenv/bin/activate  # Or `myenv\Scripts\activate` on Windows
pip install -r requirements.txt
python seed_db.py          # Initialize the database
python app.py
```
**2. Frontend Setup
```text
cd frontend
npm install
npm run dev
```
**3. Environment Variables
Create a .env file in the frontend folder:
```text
VITE_GOOGLE_CLIENT_ID=your_google_id_here
```
💾 Database Setup (MongoDB)
EduStreamAI uses MongoDB as a NoSQL document store. Follow these steps to get the database running on your machine:

1. Install MongoDB Community Server
Download and install the MongoDB Community Server from the official website.

During installation, ensure "Install MongoDB as a Service" is checked (this makes sure the database starts automatically when you turn on your PC).

2. Install MongoDB Compass (Visual UI)
Download and install MongoDB Compass here.

Open Compass and click "Connect" using the default connection string: mongodb://localhost:27017.

3. Initialize the Data
Once the server is running, you need to push the curriculum data from your backend folder:

Bash
cd backend
python seed_db.py
Verification: Open MongoDB Compass. You should now see a database named learning_path_db with a collection called modules containing your course data.
