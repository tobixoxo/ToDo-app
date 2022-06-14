from app import db, User, SkillLevel, Task

db.Session.add(SkillLevel({
    'badge' : 'Brave-Pawn',
    'color' : 'orange',
    'min_completed_task' : 0,
    'max_completed_task' : 5
}))

db.session.add(User({
    'first_name' : 'Sanjeev',
    'last_name' : 'Rawat',
    'email' : 'abc@mail',
    'dob' : "2002-09-02",
    'bio' : "the admin :D",
    'skill_id' : 1,
    'accomplished_tasks' : 0
}))