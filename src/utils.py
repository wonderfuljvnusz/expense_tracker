from datetime import datetime


def get_user_input(prompt):
    """
    Display a prompt to the user and return their input.
    """
    return input(prompt)


def validate_date(date_string):
    """
    Validate if the provided string is a valid date in the format YYYY-MM-DD.

    Args:
        date_string (str): The date string to validate.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        # Try parsing the date string
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        # If parsing fails, it's not a valid date
        return False


def validate_positive_number(value):
    """
    Validate if the provided value is a positive number (integer or float).

    Args:
        value (str): The value to validate.

    Returns:
        bool: True if the value is a positive number, False otherwise.
    """
    try:
        # Convert to a float and check if it is positive
        return float(value) > 0
    except ValueError:
        # If conversion fails, it's not a number
        return False