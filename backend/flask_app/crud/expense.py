# backend/crud/expense.py
from core.db import db
from models.expense import Expense

def create_expense(data):
    """Creates a new expense record in the database."""
    new_expense = Expense(
        amount=data['amount'],
        type=data.get('type', 'Expense'),
        category=data['category'],
        sub_category=data.get('sub_category', ''),
        tags=data.get('tags', ''),
        note=data.get('note', '')
    )
    db.session.add(new_expense)
    db.session.commit()
    return new_expense

def get_all_expenses():
    """Fetches all expenses, ordered by the newest first."""
    return Expense.query.order_by(Expense.date.desc()).all()

def get_expense_by_id(expense_id):
    """Fetches a single expense by its ID."""
    return Expense.query.get(expense_id)

def delete_expense(expense_id):
    """Deletes an expense from the database."""
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return True
    return False