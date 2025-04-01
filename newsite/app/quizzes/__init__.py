from flask import Blueprint

bp = Blueprint('quizzes', __name__)

from app.quizzes import routes
