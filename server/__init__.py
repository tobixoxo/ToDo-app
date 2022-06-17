from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # we don't need real time updates as this is a REST based api

db = SQLAlchemy(app)

# db.create_all()

# db.session.add(SkillLevel( **{
#     'badge' : 'Brave-Pawn',
#     'color' : 'orange',
#     'min_completed_task' : 0,
#     'max_completed_task' : 5
# }))

# db.session.add(User(** {
#     'first_name' : 'Sanjeev',
#     'last_name' : 'Rawat',
#     'email' : 'abc@mail',
#     'dob' : datetime(2002,9,28,0,0,0),
#     'bio' : "the admin :D",
#     'skill_id' : 1,
#     'accomplished_tasks' : 0
# }))

# db.session.commit()

from server import routes

