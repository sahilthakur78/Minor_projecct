# 🧠 Brain Blitz – Quiz Web Application

Brain Blitz is a **category-based quiz web application** built using **Flask (Python)**, **HTML**, **CSS**, and **JavaScript**.  
It allows users to select a programming category, attempt quizzes, and view results dynamically.

---

## 🚀 Features

- 🎯 Category-based quizzes (JavaScript, Python, Java, C++, DSA, etc.)
- 📊 Dynamic questions loaded from JSON
- 🧩 Interactive UI with smooth screen transitions
- 🏆 Leaderboard API (demo data)
- 📈 Question statistics page
- ❌ Custom 404 & 500 error pages
- 🔁 REST APIs for questions & categories

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (Vanilla JS)

### Backend
- Python
- Flask

### Data
- JSON (`questions.json`)

---

## 📁 Project Structure

brain_blitz/
│
├── static/
│ ├── css/
│ └── js/
│ └── script.js
│
├── templates/
│ ├── index.html
│ ├── quiz.html
│ ├── result.html
│ └── error.html
│
├── questions.json
├── app.py
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/sahilthakur78/Minor_projecct.git
cd brain_blitz
2️⃣ Create virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install flask
4️⃣ Run the application
bash
Copy code
python app.py
5️⃣ Open in browser
cpp
Copy code
http://127.0.0.1:5000
🌐 API Endpoints
Endpoint	Description
/	Home page
/quiz?category=javascript	Quiz page
/result	Result page
/api/questions/<category>	Get questions
/api/categories	List categories
/api/leaderboard	Leaderboard data
/stats	Question statistics

📊 Supported Categories
JavaScript

Python

HTML & CSS

🧪 Sample Console Logs
text
Copy code
🚀 Brain Blitz Server Starting...
📊 Loaded 10 categories
🌐 Server running on: http://127.0.0.1:5000
📸 Screenshots
Add screenshots here later for better presentation 😉

🔮 Future Improvements
User authentication (login/signup)

Database integration (SQLite / MongoDB)

Timer-based quizzes

Real leaderboard storage

Mobile responsive UI

Admin panel to add questions

👨‍💻 Author
Sahil Thakur
BCA Student | Aspiring Full Stack Developer

⭐ Support
If you like this project, don’t forget to star ⭐ the repository
and share feedback 🙌
