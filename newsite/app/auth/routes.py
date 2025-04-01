from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db, Group, Notification
from werkzeug.utils import secure_filename
from app.auth import bp
import os
from werkzeug.urls import url_parse
from app.auth.forms import LoginForm, RegistrationForm

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        
        # Debug information
        print(f"Login successful for user: {user.username}")
        print(f"User admin status: is_admin={user.is_admin}, is_group_admin={user.is_group_admin}")
        
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            if user.is_admin:
                next_page = url_for('admin.index')
                print(f"Redirecting admin to: {next_page}")
            else:
                next_page = url_for('main.index')
        
        flash('Welcome back!', 'success')
        return redirect(next_page)
    
    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Register', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
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
