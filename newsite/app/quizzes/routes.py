from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.quizzes import bp
from app import db
from app.models import Quiz, QuizAttempt

@bp.route('/')
@login_required
def index():
    quizzes = Quiz.query.all()
    return render_template('quizzes/index.html', quizzes=quizzes)

@bp.route('/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quizzes/take_quiz.html', quiz=quiz)

@bp.route('/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    # Quiz submission logic will be implemented here
    return redirect(url_for('quizzes.index'))
