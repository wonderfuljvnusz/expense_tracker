# Import required modules
import pandas as pd
import matplotlib.pyplot as plt
from src.models import get_expenses

def generate_report():
    """
    Generate a summarized report of expenses based on user selection.
    The report can be daily, weekly, or monthly.
    """
    # Query database for all expenses
    expenses = get_expenses()

    # Convert the data to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(expenses, columns=["id", "date", "category", "amount", "description"])
    df["date"] = pd.to_datetime(df["date"])  # Convert date column to datetime

    # Prompt user for report type
    report_type = input("Enter report type (daily, weekly, monthly): ").strip().lower()

    # Summarize expenses based on the selected type
    if report_type == "daily":
        summary = df.groupby(df["date"].dt.date).sum()
    elif report_type == "weekly":
        summary = df.groupby(df["date"].dt.to_period("W")).sum()
    elif report_type == "monthly":
        summary = df.groupby(df["date"].dt.to_period("M")).sum()
    else:
        print("Invalid report type. Please choose daily, weekly, or monthly.")
        return

    # Display the report in tabular format
    print("\nExpense Summary:")
    print(summary[["amount"]])

def visualize_expenses():
    """
    Visualize expenses using bar, pie, and line charts.
    """
    # Query database for all expenses
    expenses = get_expenses()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(expenses, columns=["id", "date", "category", "amount", "description"])
    df["date"] = pd.to_datetime(df["date"])  # Convert date column to datetime

    # Summarize expenses by category
    category_summary = df.groupby("category")["amount"].sum()

    # Generate a bar chart for spending by category
    plt.figure(figsize=(10, 6))
    category_summary.plot(kind="bar", color="skyblue", alpha=0.8)
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Generate a line chart for spending trends over time
    time_summary = df.groupby("date")["amount"].sum()

    plt.figure(figsize=(10, 6))
    time_summary.plot(kind="line", marker="o", color="green", alpha=0.8)
    plt.title("Spending Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()

    # Generate a pie chart for spending by category
    plt.figure(figsize=(8, 8))
    category_summary.plot(kind="pie", autopct="%1.1f%%", startangle=90, colormap="Set3")
    plt.title("Spending Distribution by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()