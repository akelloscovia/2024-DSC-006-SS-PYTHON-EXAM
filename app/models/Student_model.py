from  flask import Flask
from app.extensions import db
from datetime import datetime

#Table for students
class Students(db.Model):
 id = db.Column(db.integer,primary_key=True)
fisrt_name = db.Column(db.string(50),nullable = False)
last_name= db.Column(db.string(100),nullable = False)
program_id= db.Column(db.integer,nullable = False)
email= db.Column(db.string(100),nullable = False)
created_at= db.Column(db.DateTime, default = datetime.now())
updated_at=db.Column(db.DateTime, onupdate = datetime.now())

def __str__(self):
        return f"{self.id},({self.first_name}, {self.last_name}, {self.program_id},{self.email}, {self.created_at} ,{self.updated_at})"
students_detail= Students("001","Akello","Scovia","2440150","akelloscovia907@gmail.com") 
print(students_detail)   