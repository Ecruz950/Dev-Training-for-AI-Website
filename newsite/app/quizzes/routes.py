﻿from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.quizzes import bp
from app import db

# Routes will be added here
