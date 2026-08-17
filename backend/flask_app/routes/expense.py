# backend/routes/expense.py
from flask import Blueprint, request, jsonify
from crud.expense import create_expense, get_all_expenses ,update_expense ,delete_expense
# , delete_expense
from schema.expense import expense_schema, expenses_schema
from core.db import db

# need to add try catch block

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
@expense_bp.route('/api/expenses/<int:expense_id>', methods=['PATCH'])
def modify_expense(expense_id):
    """PATCH request to modify an existing money tracking record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        updated_expense = update_expense(expense_id, data)
        if updated_expense is None:
            return jsonify({"error": "Expense not found"}), 404
        return jsonify(expense_schema.dump(updated_expense)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@expense_bp.route('/api/expenses/<int:id>', methods=['DELETE'])
def remove_expense(id):
    """DELETE request to remove a record."""
    try:
        success = delete_expense(id)
        if success:
            return jsonify({"message": "Expense deleted successfully"}), 200
        return jsonify({"error": "Expense not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400