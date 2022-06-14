from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # we don't need real time updates as this is a REST based api

db = SQLAlchemy(app)

# model 
class SkillLevel(db.Model):
    __tablename__ = 'SkillLevel'
    id = db.Column(db.Integer, primary_key = True, unique = True)
    badge = db.Column(db.String, unique = True)
    color = db.Column(db.String, unique = True)
    min_completed_task = db.Column(db.Integer, unique = True)
    max_completed_task = db.Column(db.Integer, unique = True)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True, unique = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    dob = db.Column(db.Date, unique = False, nullable = False)
    bio = db.Column(db.Text, unique = False, nullable = True)
    skill_id = db.Column(db.Integer, db.ForeignKey("SkillLevel.id"))
    accomplished_tasks = db.Column(db.Integer)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    user_id = db.Column(db.Integer,db.ForeignKey("User.id"), nullable = False)
    description = db.Column(db.Text, unique = False, nullable = False)
    deadline = db.Column(db.DateTime, nullable = False)

# db.create_all()

db.session.add(SkillLevel( **{
    'badge' : 'Brave-Pawn',
    'color' : 'orange',
    'min_completed_task' : 0,
    'max_completed_task' : 5
}))

db.session.add(User(** {
    'first_name' : 'Sanjeev',
    'last_name' : 'Rawat',
    'email' : 'abc@mail',
    'dob' : datetime(2002,9,28,0,0,0),
    'bio' : "the admin :D",
    'skill_id' : 1,
    'accomplished_tasks' : 0
}))

db.session.commit()

@app.route('/')
def index():
    return "<h1>Hello!</h1>"
