import re


def phone_number(number: str) -> str:

    # Remove all non-numeric characters from a string
    number = re.sub("\D", "", number)

    # Suffix correction
    if len(number) == 12:
        return "+" + number
    if len(number) == 11:
        return "+3" + number
    if len(number) == 10:
        return "+38" + number
    return "Incorrect number"


# Example of usage
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [phone_number(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
