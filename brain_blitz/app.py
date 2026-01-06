from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'brain_blitz_secret_key'

def load_questions():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading questions: {e}")
        return {}

def get_category_display_name(category):
    category_names = {
        'javascript': 'JavaScript',
        'python': 'Python', 
        'java': 'Java',
        'cpp': 'C++',
        'html_css': 'HTML & CSS',
        'react': 'React.js',
        'data_structures': 'Data Structures',
        'algorithms': 'Algorithms',
        'sql': 'SQL',
        'nodejs': 'Node.js'
    }
    return category_names.get(category, category.title())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    category = request.args.get('category', 'javascript')
    return render_template('quiz.html', category=category)

@app.route('/result')
def result():
    score = request.args.get('score', 0)
    total = request.args.get('total', 1)
    category = request.args.get('category', 'general')
    
    # Get display name for the category
    category_display = get_category_display_name(category)
    
    return render_template('result.html', 
                         score=score, 
                         total=total, 
                         category=category,
                         category_display=category_display)

@app.route('/api/questions/<category>')
def get_questions(category):
    questions = load_questions()
    category_questions = questions.get(category, [])
    print(f"Returning {len(category_questions)} questions for {category}")
    return jsonify(category_questions)

@app.route('/api/leaderboard')
def get_leaderboard():
    leaderboard = [
        {'rank': 1, 'player': 'CodeMaster', 'score': '9/10', 'category': 'JavaScript'},
        {'rank': 2, 'player': 'PythonPro', 'score': '8/10', 'category': 'Python'},
        {'rank': 3, 'player': 'JavaExpert', 'score': '7/10', 'category': 'Java'},
        {'rank': 4, 'player': 'CppGuru', 'score': '8/10', 'category': 'C++'},
        {'rank': 5, 'player': 'WebWizard', 'score': '9/10', 'category': 'HTML & CSS'},
        {'rank': 6, 'player': 'ReactNinja', 'score': '8/10', 'category': 'React.js'},
        {'rank': 7, 'player': 'DSAExpert', 'score': '7/10', 'category': 'Data Structures'},
        {'rank': 8, 'player': 'AlgoMaster', 'score': '9/10', 'category': 'Algorithms'},
        {'rank': 9, 'player': 'DatabasePro', 'score': '8/10', 'category': 'SQL'},
        {'rank': 10, 'player': 'BackendBoss', 'score': '7/10', 'category': 'Node.js'}
    ]
    return jsonify(leaderboard)

@app.route('/api/categories')
def get_categories():
    """API endpoint to get all available categories"""
    questions = load_questions()
    categories = list(questions.keys())
    
    # Return categories with their display names
    categories_with_names = []
    for category in categories:
        categories_with_names.append({
            'id': category,
            'name': get_category_display_name(category),
            'question_count': len(questions.get(category, []))
        })
    
    return jsonify(categories_with_names)

@app.route('/stats')
def stats():
    """Page showing statistics about available questions"""
    questions = load_questions()
    stats_data = {}
    
    for category, category_questions in questions.items():
        stats_data[get_category_display_name(category)] = len(category_questions)
    
    return f"""
    <html>
        <body style="font-family: Arial; padding: 20px;">
            <h1>Brain Blitz - Question Statistics</h1>
            <h2>Total Categories: {len(questions)}</h2>
            <ul>
                {"".join([f"<li><b>{name}</b>: {count} questions</li>" for name, count in stats_data.items()])}
            </ul>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error="Internal server error"), 500

if __name__ == '__main__':
    print("🚀 Brain Blitz Server Starting...")
    print("📁 Current directory:", os.getcwd())
    
    # Load questions to verify they're available
    questions = load_questions()
    print(f"📊 Loaded {len(questions)} categories:")
    for category, category_questions in questions.items():
        display_name = get_category_display_name(category)
        print(f"   • {display_name}: {len(category_questions)} questions")
    
    print("🌐 Server running on: http://127.0.0.1:5000")
    print("=" * 50)
    
    app.run(debug=True, host='127.0.0.1', port=5000)