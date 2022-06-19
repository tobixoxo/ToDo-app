from server import app
from server.models import *

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/<int:id>')
def dashboard(id):
    user_name = User.query.filter(User.id == id).first().first_name
    return render_template('dashboard.html')