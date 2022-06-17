from server import app
from server.models import *

@app.route('/')
def index():
    return "<h1>Hello!</h1>"

@app.route('/dashboard/<int:id>')
def dashboard(id):
    user_name = User.query.filter(User.id == id).first().first_name
    print(user_name)
    return f"<h1>{user_name}</h1>"