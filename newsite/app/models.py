from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    admin = db.relationship('User', backref=db.backref('administered_groups', lazy=True))
    members = db.relationship('User', secondary='group_members', backref=db.backref('groups', lazy='dynamic'))

class GroupMember(db.Model):
    __tablename__ = 'group_members'
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'group_invite', 'system', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)
    data = db.Column(db.JSON)  # For storing additional data like group_id for invites

    def mark_as_read(self):
        self.read = True
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    is_group_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    avatar = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notifications = db.relationship('Notification', backref='user', lazy=True, order_by='desc(Notification.created_at)')
    email_notifications = db.Column(db.Boolean, default=True)
    progress_updates = db.Column(db.Boolean, default=True)
    new_modules = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_notifications(self):
        return len(self.notifications) > 0

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    video_path = db.Column(db.String(200))
    video_url = db.Column(db.String(200))
    quiz_url = db.Column(db.String(200))
    order = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    progress = db.relationship('ModuleProgress', backref='module', lazy=True)

    def __repr__(self):
        return f'<Module {self.title}>'

class ModuleProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    video_completed = db.Column(db.Boolean, default=False)
    quiz_completed = db.Column(db.Boolean, default=False)
    quiz_score = db.Column(db.Integer)
    progress = db.Column(db.Integer, default=0)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def completed(self):
        return self.video_completed and self.quiz_completed

    def __repr__(self):
        return f'<ModuleProgress {self.user.username} - {self.module.title}>'

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    passing_score = db.Column(db.Integer, default=70)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    questions = db.relationship('Question', backref='quiz', lazy=True)
    attempts = db.relationship('QuizAttempt', backref='quiz', lazy=True)

    def __repr__(self):
        return f'<Quiz {self.title}>'

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    options = db.relationship('Option', backref='question', lazy=True)

    def __repr__(self):
        return f'<Question {self.text[:50]}...>'

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Option {self.text[:50]}...>'

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer)
    passed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<QuizAttempt {self.user.username} - {self.quiz.title}>' 