from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class StudentModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    grade = db.Column(db.Integer())
 
    def __init__(self, student_id,name,grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
 
    def __repr__(self):
        return f"{self.name}:{self.student_id}:{self.grade}"
