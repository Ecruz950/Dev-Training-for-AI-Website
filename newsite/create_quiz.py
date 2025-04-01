from app import create_app, db
from app.models import Quiz, Module
import json
import os

app = create_app()

with app.app_context():
    # Check if module 1 quiz already exists
    existing_quiz = Quiz.query.filter_by(module_id=1).first()
    if existing_quiz:
        print(f"Quiz for module 1 already exists: {existing_quiz.title}")
    else:
        # Get quiz data from JSON
        json_path = os.path.join('app', 'static', 'quizzes', '1_quiz.json')
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                quiz_data = json.load(f)
                
            # Create the quiz record
            quiz = Quiz(
                module_id=1,
                title=quiz_data['title'],
                passing_score=quiz_data['passing_score']
            )
            db.session.add(quiz)
            db.session.commit()
            print(f"Created quiz: {quiz.title} with ID {quiz.id}")
        else:
            print(f"Quiz JSON file not found at {json_path}") 