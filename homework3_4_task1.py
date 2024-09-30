from datetime import datetime

def get_days_from_today(date: str) -> int:
    current_date = datetime.now()
    try:
        inputed_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Incorrect date format/value. Usage: "YYYY-MM-DD"')
        return None
    else:
        return current_date.toordinal() - inputed_date.toordinal()
    