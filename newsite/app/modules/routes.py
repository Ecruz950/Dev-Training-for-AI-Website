from flask import render_template, redirect, url_for, flash, request, send_from_directory
from flask_login import login_required, current_user
from app.modules import bp
from app import db
from app.models import Module, ModuleProgress
import os

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
    return render_template('modules/video.html', module=module)

@bp.route('/<int:module_id>/quiz')
@login_required
def quiz(module_id):
    module = Module.query.get_or_404(module_id)
    return render_template('modules/quiz.html', module=module)

@bp.route('/static/videos/<path:filename>')
@login_required
def serve_video(filename):
    return send_from_directory('static/videos', filename)

@bp.route('/api/quiz/submit', methods=['POST'])
@login_required
def submit_quiz():
    data = request.get_json()
    module_id = data.get('module_id')
    score = data.get('score')
    
    progress = ModuleProgress.query.filter_by(
        user_id=current_user.id,
        module_id=module_id
    ).first()
    
    if not progress:
        progress = ModuleProgress(
            user_id=current_user.id,
            module_id=module_id
        )
        db.session.add(progress)
    
    progress.quiz_completed = True
    progress.quiz_score = score
    db.session.commit()
    
    return {'status': 'success'}
