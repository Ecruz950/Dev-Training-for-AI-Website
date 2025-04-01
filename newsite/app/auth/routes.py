from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db, Group, Notification
from werkzeug.utils import secure_filename
from app.auth import bp
import os

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('auth.register'))
            
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('auth.register'))
            
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/notifications')
@login_required
def notifications():
    notifications = current_user.notifications
    return render_template('auth/notifications.html', notifications=notifications)

@bp.route('/notifications/mark-read/<int:notification_id>')
@login_required
def mark_notification_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    if notification.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('main.index'))
    notification.mark_as_read()
    return redirect(url_for('auth.notifications'))

@bp.route('/notifications/accept-invite/<int:notification_id>')
@login_required
def accept_invite(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    if notification.user_id != current_user.id or notification.type != 'group_invite':
        flash('Invalid notification', 'error')
        return redirect(url_for('main.index'))
        
    group_id = notification.data.get('group_id')
    group = Group.query.get_or_404(group_id)
    
    # Add user to group members
    group.members.append(current_user)
    notification.mark_as_read()
    db.session.commit()
    
    flash(f'You have joined the group: {group.name}', 'success')
    return redirect(url_for('main.group_management'))

@bp.route('/notifications/reject-invite/<int:notification_id>')
@login_required
def reject_invite(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    if notification.user_id != current_user.id or notification.type != 'group_invite':
        flash('Invalid notification', 'error')
        return redirect(url_for('main.index'))
        
    group_id = notification.data.get('group_id')
    group = Group.query.get_or_404(group_id)
    
    notification.mark_as_read()
    db.session.commit()
    
    flash(f'You have declined the invitation to join: {group.name}', 'info')
    return redirect(url_for('main.index'))

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes will be added here
