# backend/crud/expense.py
from core.db import db
from models.expense import Expense
from sqlalchemy import select

def create_expense(data):
    """Creates a new expense record in the database."""
    new_expense = Expense(
        amount=data['amount'],
        transaction_type=data.get('transaction_type', 'Expense'),
        category=data['category'],
        sub_category=data.get('sub_category', ''),
        tags=data.get('tags', ''),
        note=data.get('note', ''),
        expense_reason=data.get('expense_reason',''),
        payment_method=data.get('payment_method',''),
        payment_account=data.get('payment_account',''),
        is_recurring=data.get('is_recurring',False)
    )
    db.session.add(new_expense)
    db.session.commit()
    return new_expense

def get_all_expenses():
    """Fetches all expenses, ordered by the newest first."""
    # return Expense.query.order_by(Expense.date.desc()).all()
    statement = select(Expense).order_by(Expense.date.desc())
    return db.session.scalars(statement).all()

def get_expense_by_id(expense_id):
    """Fetches a single expense by its ID."""
    # return Expense.query.get(expense_id)
    return db.session.get(Expense, expense_id)

def update_expense(expense_id,data):
    expense = db.session.get(Expense, expense_id)
    if not expense:
        return None
    if "amount" in data:
        expense.amount = data["amount"]
    if "transaction_type" in data:
        expense.transaction_type = data["transaction_type"]
    if "category" in data:
        expense.category = data["category"]
    if "sub_category" in data:
        expense.sub_category = data["sub_category"]
    if "tags" in data:
        expense.tags = data["tags"]
    if "note" in data:
        expense.note = data["note"]
    if "payment_method" in data:
        expense.payment_method = data["payment_method"]
    if "payment_account" in data:
        expense.payment_account = data["payment_account"]
    if "expense_reason" in data:
        expense.expense_reason = data["expense_reason"]
    if "is_recurring" in data:
        expense.is_recurring = data["is_recurring"]
    if "date" in data:
        expense.date = data["date"]
    db.session.commit()
    return expense


def delete_expense(expense_id):
    """Deletes an expense from the database."""
    # expense = Expense.query.get(expense_id)
    expense = db.session.get(Expense, expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return True
    return False