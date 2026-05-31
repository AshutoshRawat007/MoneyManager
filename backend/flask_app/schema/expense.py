# backend/schema/expense.py
from core.db import ma
from models.expense import Expense

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
        load_instance = True  # Automatically load JSON into the Expense model

# Initialize schemas
expense_schema = ExpenseSchema()             # For a single expense (e.g., adding one)
expenses_schema = ExpenseSchema(many=True)   # For a list of expenses (e.g., viewing all)