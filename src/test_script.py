from src.models import initialize_db, add_expense, get_expenses, edit_expense, delete_expense

# Step 1: Initialize the database
# This function sets up the database, creating the necessary tables if they do not already exist.
initialize_db()

# Step 2: Add some test expenses
# Use the `add_expense` function to insert test data into the database for various expense categories.
add_expense("2024-01-01", "Groceries", 20.5, "Milk and bread")  # Adding a grocery expense for January 1, 2024.
add_expense("2024-01-02", "Rent", 1200, "January rent")  # Adding a rent payment for January 2, 2024.
add_expense("2024-01-03", "Entertainment", 50, "Movie night")  # Adding an entertainment expense for January 3, 2024.

# Step 3: Retrieve and print all expenses
# Fetch all expenses from the database using the `get_expenses` function.
# This prints a list of tuples representing each expense.
print(get_expenses())  # Display all expenses to verify they were added correctly.

# Step 4: Edit an expense
# Use the `edit_expense` function to modify an existing expense.
# Here, the expense with ID 1 (Groceries) is being updated with a new amount and description.
edit_expense(1, amount=25.0, description="Milk, bread, and eggs")  # Update the grocery expense.

# Step 5: Retrieve and print updated expenses
# Fetch and print all expenses again to confirm that the edits to the grocery expense were saved successfully.
print(get_expenses())  # Verify the updates are reflected in the database.

# Step 6: Delete an expense
# Use the `delete_expense` function to remove an expense from the database.
# Here, the expense with ID 2 (Rent) is being deleted.
delete_expense(2)  # Remove the rent expense from the database.

# Step 7: Retrieve and print remaining expenses
# Fetch and print the remaining expenses to confirm that the rent expense was successfully deleted.
print(get_expenses())  # Ensure the database only contains the updated grocery and entertainment expenses.
