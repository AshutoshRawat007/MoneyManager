# backend/main.py
from flask import Flask
from flask_cors import CORS
from core.db import db, ma

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///money_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # --- NEW: Register the Routes ---
    from routes.expense import expense_bp
    app.register_blueprint(expense_bp)
    # --------------------------------

    with app.app_context():
        from models.expense import Expense
        db.create_all()

    @app.route("/")
    def home():
        return {"message": "Expense Tracker API Running"}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)