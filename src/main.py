# Import necessary modules
from models import initialize_db, add_expense, delete_expense, edit_expense, get_expenses
from reports import generate_report, visualize_expenses
from utils import get_user_input

# Initialize database
initialize_db()

# Display main menu options
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Generate Report")
    print("6. Visualize Expenses")
    print("7. Exit")

    # Get user choice
    choice = get_user_input("Enter your choice: ")

    if choice == "1":
        # Prompt user to add an expense
        add_expense()
    elif choice == "2":
        # List all expenses
        get_expenses()
    elif choice == "3":
        # Edit an expense
        edit_expense()
    elif choice == "4":
        # Delete an expense
        delete_expense()
    elif choice == "5":
        # Generate and display report
        generate_report()
    elif choice == "6":
        # Visualize expenses with charts
        visualize_expenses()
    elif choice == "7":
        # Exit the program
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")