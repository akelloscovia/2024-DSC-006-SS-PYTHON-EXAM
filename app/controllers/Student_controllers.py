from app.extensions import db
from datetime import datetime
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.Integer, nullable=False)
    program_id=db.Column(db.integer,nullable = False)
    email = db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, default = datetime.now())
    updated_at=db.Column(db.DateTime, onupdate = datetime.now())
    
    
    def __str__(self):
        return f"{self.id},({self.first_name}, {self.last_name}, {self.program_id},{self.email}, {self.created_at} ,{self.updated_at})"