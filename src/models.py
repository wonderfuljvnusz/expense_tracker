# Import SQLite module
import os
import sqlite3


def initialize_db():
    """Initialize the database and create tables if they don't exist."""
    # Ensure the 'data' directory exists
    os.makedirs("data", exist_ok=True)

    # Connect to the database
    with sqlite3.connect("data/expenses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        """)
        conn.commit()

def add_expense(date, category, amount, description=""):
    """Add a new expense to the database."""
    with sqlite3.connect("data/expenses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        """, (date, category, amount, description))
        conn.commit()

def get_expenses(category=None, start_date=None, end_date=None):
    """Retrieve expenses with optional filters for category and date range."""
    query = "SELECT * FROM expenses WHERE 1=1"
    params = []

    if category:
        query += " AND category = ?"
        params.append(category)
    if start_date:
        query += " AND date >= ?"
        params.append(start_date)
    if end_date:
        query += " AND date <= ?"
        params.append(end_date)

    with sqlite3.connect("data/expenses.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def edit_expense(expense_id, date=None, category=None, amount=None, description=None):
    """Edit an existing expense."""
    updates = []
    params = []

    if date:
        updates.append("date = ?")
        params.append(date)
    if category:
        updates.append("category = ?")
        params.append(category)
    if amount:
        updates.append("amount = ?")
        params.append(amount)
    if description is not None:  # Allow empty description
        updates.append("description = ?")
        params.append(description)

    query = f"UPDATE expenses SET {', '.join(updates)} WHERE id = ?"
    params.append(expense_id)

    with sqlite3.connect("data/expenses.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

def delete_expense(expense_id):
    """Delete an expense by its ID."""
    with sqlite3.connect("data/expenses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()