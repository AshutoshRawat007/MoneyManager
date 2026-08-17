    # backend/models/expense.py
from core.db import db
from datetime import datetime
from zoneinfo import ZoneInfo
class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False, default="Expense") # Income or Expense
    category = db.Column(db.String(50), nullable=False)
    sub_category = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(100), nullable=True) # Stored as comma-separated string
    note = db.Column(db.Text, nullable=True)
    # add payment type to know if it was cash, UPI or Creditcard payment and which UPI and whcih credit card was used
    payment_method = db.Column(db.String(100), nullable=True) 
    payment_account = db.Column(db.String(100), nullable=True)
    # add decision note to track what caused this expenditure, mostly its essentials but in case of non recussing cost what triggered the expense
    expense_reason = db.Column(db.Text, nullable=True) 
    is_recurring = db.Column(db.Boolean, default=False, nullable=False)
    date = db.Column(
    db.DateTime,
    default=datetime.now
)
    # date = db.Column(
    # db.DateTime,
    # default=lambda: datetime.now(ZoneInfo("Asia/Kolkata")).replace(tzinfo=None)
# )


    def __repr__(self):
        return f"<Expense {self.category} - ${self.amount}>"