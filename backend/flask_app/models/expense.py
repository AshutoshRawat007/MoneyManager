    # backend/models/expense.py
from core.db import db
from datetime import datetime

class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False, default="Expense") # Income or Expense
    category = db.Column(db.String(50), nullable=False)
    sub_category = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(100), nullable=True) # Stored as comma-separated string
    note = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Expense {self.category} - ${self.amount}>"