from server import db

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
