from app import create_app, db
from app.models import Quiz, Question, Option
import json
import os

app = create_app()

with app.app_context():
    # Get the quiz for module 1
    quiz = Quiz.query.filter_by(module_id=1).first()
    
    if quiz:
        # Check if questions already exist
        if len(quiz.questions) > 0:
            print(f"Quiz already has {len(quiz.questions)} questions.")
        else:
            # Load the questions from the JSON file
            json_path = os.path.join('app', 'static', 'quizzes', '1_quiz.json')
            
            if os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    quiz_data = json.load(f)
                
                questions_added = 0
                
                # Add each question from the JSON
                for i, q_data in enumerate(quiz_data['questions']):
                    # Create question and commit it first to get an ID
                    question = Question(
                        quiz_id=quiz.id,
                        text=q_data['text'],
                        order=i+1
                    )
                    db.session.add(question)
                    db.session.commit()
                    
                    # Now that we have a question ID, create options
                    for j, option_text in enumerate(q_data['options']):
                        option = Option(
                            question_id=question.id,
                            text=option_text,
                            is_correct=(j == q_data['correct_answer']),
                            order=j+1
                        )
                        db.session.add(option)
                    
                    questions_added += 1
                
                db.session.commit()
                print(f"Added {questions_added} questions to quiz with {len(quiz_data['questions'])} in the JSON.")
            else:
                print(f"Quiz JSON file not found at {json_path}")
    else:
        print("Quiz for module 1 not found.") 