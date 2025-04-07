from app import create_app, db
from app.models import Quiz, Question, Option
import json
import os

def create_quiz(module_id):
    """Create quiz for specified module"""
    app = create_app()
    
    with app.app_context():
        # Delete all quizzes for the specified module
        quizzes = Quiz.query.filter_by(module_id=module_id).all()
        for quiz in quizzes:
            # Delete all options and questions first
            for question in quiz.questions:
                for option in question.options:
                    db.session.delete(option)
                db.session.delete(question)
            db.session.delete(quiz)
        db.session.commit()
        print(f"Existing quizzes for module {module_id} deleted")
        
        # Quiz titles and descriptions
        quiz_info = {
            1: {
                "title": "Introduction to LLMs and Responsible Use Quiz",
                "description": "Test your knowledge of LLMs and responsible AI use"
            },
            2: {
                "title": "Developer Tips for using AI Quiz",
                "description": "Test your knowledge of AI development best practices"
            }
        }
        
        # Create the quiz with explicit ID
        quiz = Quiz(
            id=module_id,  # Explicitly set the ID
            module_id=module_id,
            title=quiz_info[module_id]["title"],
            description=quiz_info[module_id]["description"],
            passing_score=70
        )
        db.session.add(quiz)
        db.session.commit()
        
        # Add questions from the JSON file
        quiz_path = os.path.join(app.static_folder, 'quizzes', f'{module_id}_quiz.json')
        if os.path.exists(quiz_path):
            with open(quiz_path, 'r', encoding='utf-8') as f:
                quiz_data = json.load(f)
                
            for i, q in enumerate(quiz_data['questions'], 1):
                question = Question(
                    quiz_id=quiz.id,
                    text=q['text'],
                    order=i
                )
                db.session.add(question)
                db.session.commit()
                
                for j, opt in enumerate(q['options'], 1):
                    option = Option(
                        question_id=question.id,
                        text=opt,
                        is_correct=(j-1 == q['correct_answer']),
                        order=j
                    )
                    db.session.add(option)
            
            db.session.commit()
            print(f"Quiz for module {module_id} created successfully with ID: {quiz.id}")
        else:
            print(f"Quiz JSON file not found at {quiz_path}")

if __name__ == '__main__':
    # Create quizzes for both modules
    create_quiz(1)
    create_quiz(2) 