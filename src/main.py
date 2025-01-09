# Import necessary modules
from src.models import initialize_db, add_expense, delete_expense, edit_expense, get_expenses
from src.reports import generate_report, visualize_expenses
from src.utils import get_user_input

# Initialize database
initialize_db()

# Define the main function
def main():
    """
    Main function to handle the application workflow.
    Provides a menu to the user for expense management.
    """
    while True:
        # Display main menu options
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Generate Report")
        print("6. Visualize Expenses")
        print("7. Exit")

        # Get user choice
        choice = get_user_input("Enter your choice: ")

        # Handle user choices
        if choice == "1":
            # Prompt user to add an expense
            date = get_user_input("Enter the date (YYYY-MM-DD): ")
            category = get_user_input("Enter the category (ex. Housing, Groceries, Transportation, Entertainment: ")
            amount = float(get_user_input("Enter the amount: "))
            description = get_user_input("Enter a description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")
        elif choice == "2":
            # List all expenses
            expenses = get_expenses()
            print("\n=== All Expenses ===")
            for expense in expenses:
                print(expense)
        elif choice == "3":
            # Edit an expense
            expense_id = int(get_user_input("Enter the expense ID to edit: "))
            new_date = get_user_input("Enter the new date (leave blank to keep unchanged): ")
            new_category = get_user_input("Enter the new category (leave blank to keep unchanged): ")
            new_amount = get_user_input("Enter the new amount (leave blank to keep unchanged): ")
            new_description = get_user_input("Enter the new description (leave blank to keep unchanged): ")
            edit_expense(
                expense_id,
                date=new_date if new_date else None,
                category=new_category if new_category else None,
                amount=float(new_amount) if new_amount else None,
                description=new_description if new_description else None,
            )
            print("Expense updated successfully!")
        elif choice == "4":
            # Delete an expense
            expense_id = int(get_user_input("Enter the expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted successfully!")
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

# Run the main function
if __name__ == "__main__":
    main()