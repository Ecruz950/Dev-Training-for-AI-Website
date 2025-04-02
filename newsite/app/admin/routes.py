from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.admin import bp
from app import db
from app.models import User, Group, Module, Quiz
from functools import wraps

def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        print(f"Checking admin access for user: {current_user.username}")
        print(f"Admin status: is_admin={current_user.is_admin}, is_group_admin={current_user.is_group_admin}")
        
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'error')
            print(f"Access denied: User {current_user.username} is not an admin")
            return redirect(url_for('main.index'))
        
        print(f"Access granted: User {current_user.username} is an admin")
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@admin_required
def index():
    users = User.query.all()
    groups = Group.query.all()
    modules = Module.query.all()
    quizzes = Quiz.query.all()
    return render_template('admin/index.html', 
                         users=users, 
                         groups=groups, 
                         modules=modules, 
                         quizzes=quizzes)

@bp.route('/users')
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@bp.route('/groups')
@admin_required
def groups():
    groups = Group.query.all()
    return render_template('admin/groups.html', groups=groups)

@bp.route('/modules')
@admin_required
def modules():
    modules = Module.query.all()
    quizzes = Quiz.query.all()
    return render_template('admin/modules.html', modules=modules, quizzes=quizzes)

@bp.route('/quizzes')
@admin_required
def quizzes():
    quizzes = Quiz.query.all()
    return render_template('admin/quizzes.html', quizzes=quizzes)
