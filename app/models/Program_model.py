from flask import Flask
from app.extensions import db
from datetime import datetime

# Table for model
class Program(db.Model):
 id = db.Column(db.integer,primary_key=True)
name = db.Column(db.string(50),nullable = False)
period = db.Column(db.integer,nullable = False)
created_at= db.Column(db.DateTime, default = datetime.now())
updated_at=db.Column(db.DateTime, onupdate = datetime.now())


def __str__(self):
        return f"{self.id},({self.name}, {self.period}, {self.created_at} ,{self.updated_at})"
program_detail= Program("001","Diploma in Computer Science","2years")
print(program_detail)