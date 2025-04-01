from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Module, Quiz

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('modules.index'))
    return render_template('main/index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html') 