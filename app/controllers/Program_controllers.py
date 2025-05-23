from app.extensions import db
from datetime import datetime
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    peroid = db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, default = datetime.now())
    updated_at=db.Column(db.DateTime, onupdate = datetime.now())
    
    
    def __str__(self):
        return f"{self.id},({self.name}, {self.period}, {self.created_at} ,{self.updated_at})"
