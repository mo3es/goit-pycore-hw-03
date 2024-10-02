from datetime import datetime


def get_days_from_today(date: str) -> int:

    # Current date setting
    current_date = datetime.now()

    # Input validation
    try:
        inputed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print('Incorrect date format/value. Usage: "YYYY-MM-DD"')
        return None

    # Calculation quantity of days in interval of current and given date
    else:
        return current_date.toordinal() - inputed_date.toordinal()


# Usage example
interval = get_days_from_today("2021-10-09")
print(f"Current day is in {interval} days from given")
