from app import create_app, db
from app.models import Quiz

app = create_app()

with app.app_context():
    # Update the module 1 quiz passing score
    quiz = Quiz.query.filter_by(module_id=1).first()
    if quiz:
        quiz.passing_score = 100
        db.session.commit()
        print(f"Updated quiz '{quiz.title}' passing score to 100%")
    else:
        print("Quiz for module 1 not found") 