import datetime


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:

    # Input validation
    if not isinstance(users, list) or not all(isinstance(user, dict) for user in users):
        print("Input must be a list of dictionaries.")
        return None

    current_date = datetime.date.today()

    # Inputed date processing with validation
    result_list = []
    for i, user in enumerate(users):
        try:
            birthday_str = user["birthday"]
            birthday = datetime.datetime.strptime(birthday_str, "%Y.%m.%d").date()
        except (KeyError, ValueError):
            print(
                f"Incorrect values in user #{i+1} (name: {user.get('name')}): missing or invalid birthday format."
            )
            continue

        # Calculate birthday in the current year
        birthday_current_year = birthday.replace(year=current_date.year)

        # Check if birthday has already passed in the current year
        if birthday_current_year < current_date:
            birthday_current_year = birthday.replace(year=current_date.year + 1)

        # Calculate appropriate congratulation date (considering weekends)
        congratulation_date = birthday_current_year
        if birthday_current_year.weekday() == 5:
            congratulation_date += datetime.timedelta(days=2)
        elif birthday_current_year.weekday() == 6:
            congratulation_date += datetime.timedelta(days=1)

        # Calculate the number of days until the congratulation date
        days_until_congratulation = (congratulation_date - current_date).days

        # Add user information to the result list if birthday is within the week
        if 0 <= days_until_congratulation <= 7:
            user_congrat = {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                "birthday_date": birthday.strftime("%Y.%m.%d"),
            }
            result_list.append(user_congrat)

    return result_list


# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Doe", "birthday": "1985.10.06"},
    {"name": "Jane Smith", "birthday": "1990.10.07"},
    {"invalid_name": "This is not a birthday format"},  # Test case for invalid input
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Upcoming birthdays this week:", upcoming_birthdays)
