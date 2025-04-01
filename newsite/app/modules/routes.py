from flask import render_template, redirect, url_for, flash, request, send_from_directory, current_app
from flask_login import login_required, current_user
from app.modules import bp
from app import db
from app.models import Module, ModuleProgress
import os
import json

# Routes will be added here

@bp.route('/')
@login_required
def index():
    modules = Module.query.order_by(Module.order).all()
    return render_template('modules/index.html', modules=modules)

@bp.route('/<int:module_id>/video')
@login_required
def video(module_id):
    module = Module.query.get_or_404(module_id)
    
    # Set the video path if not already set
    if not module.video_path and module.id == 1:
        module.video_path = 'modules/module1Video.mp4'
        db.session.commit()
        
    return render_template('modules/video.html', module=module)

@bp.route('/<int:module_id>/quiz')
@login_required
def quiz(module_id):
    module = Module.query.get_or_404(module_id)
    
    # Check if quiz JSON exists
    quiz_path = os.path.join(current_app.static_folder, 'quizzes', f'{module.id}_quiz.json')
    if not os.path.exists(quiz_path):
        flash('Quiz not available for this module.', 'error')
        return redirect(url_for('modules.video', module_id=module.id))
        
    return render_template('modules/quiz.html', module=module)

@bp.route('/videos/<path:filename>')
@login_required
def serve_video(filename):
    return send_from_directory(
        os.path.join(current_app.static_folder, 'modules'),
        filename
    )

@bp.route('/api/quiz/submit', methods=['POST'])
@login_required
def submit_quiz():
    data = request.get_json()
    module_id = data.get('module_id')
    answers = data.get('answers', [])
    
    # Load quiz questions
    quiz_path = os.path.join(current_app.static_folder, 'quizzes', f'{module_id}_quiz.json')
    
    if not os.path.exists(quiz_path):
        return {'status': 'error', 'message': 'Quiz not found'}
        
    with open(quiz_path, 'r') as f:
        quiz_data = json.load(f)
    
    # Calculate score
    correct_count = 0
    for i, answer in enumerate(answers):
        if i < len(quiz_data['questions']) and answer == quiz_data['questions'][i]['correct_answer']:
            correct_count += 1
    
    # Calculate percentage score
    if len(quiz_data['questions']) > 0:
        score = int((correct_count / len(quiz_data['questions'])) * 100)
    else:
        score = 0
    
    # Update progress
    progress = ModuleProgress.query.filter_by(
        user_id=current_user.id,
        module_id=module_id
    ).first()
    
    if not progress:
        progress = ModuleProgress(
            user_id=current_user.id,
            module_id=module_id,
            video_completed=True
        )
        db.session.add(progress)
    
    progress.quiz_completed = True
    progress.quiz_score = score
    db.session.commit()
    
    return {'status': 'success', 'score': score}
