# backend/routes/expense.py
from flask import Blueprint, request, jsonify
from crud.expense import create_expense, get_all_expenses
# , delete_expense
from schema.expense import expense_schema, expenses_schema

# Create a Blueprint (a mini-app) for expense routes
expense_bp = Blueprint('expense_bp', __name__)

@expense_bp.route('/api/expenses', methods=['GET'])
def fetch_expenses():
    """GET request to retrieve all money tracking records."""
    expenses = get_all_expenses()
    # Convert Python objects to JSON using the schema
    result = expenses_schema.dump(expenses)
    return jsonify(result), 200

@expense_bp.route('/api/expenses', methods=['POST'])
def add_expense():
    """POST request to add a new money tracking record."""
    data = request.get_json()
    try:
        # Pass the incoming JSON to our CRUD function
        new_expense = create_expense(data)
        # Return the created object as JSON
        return jsonify(expense_schema.dump(new_expense)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    # Too make the app simple will do the delte later

# @expense_bp.route('/api/expenses/<int:id>', methods=['DELETE'])
# def remove_expense(id):
#     """DELETE request to remove a record."""
#     success = delete_expense(id)
#     if success:
#         return jsonify({"message": "Expense deleted successfully"}), 200
#     return jsonify({"error": "Expense not found"}), 404