# Import SQLite module
import sqlite3

def initialize_db():
    # Connect to SQLite database
    # Create table for expenses if it doesn't exist
    # Columns: id (auto-increment), date, category, amount, description

def add_expense():
    # Prompt user for date, category, amount, and description
    # Insert expense into the database

def get_expenses():
    # Query database for all expenses
    # Format and display results to the user

def edit_expense():
    # Prompt user for expense ID
    # Allow user to modify fields (date, category, amount, description)
    # Update the database with new values

def delete_expense():
    # Prompt user for expense ID
    # Remove the corresponding expense from the database