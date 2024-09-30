import random

def get_numbers_ticket(min, max, quantity: int) -> set:
    result = set()
    try:
        min, max, quantity = int(min), int(max), int(quantity)
        if (min < 1 or min > 999 or min >= max) or (max > 1000 or max < 2) or (quantity > max - min):
            raise ValueError
    except (TypeError, ValueError):
        print("Incorrect type/value of inputted numbers")
        return result
    else:
        while len(result) < quantity:
            next_random = random.randint(min, max)
            result.add(next_random)
    return sorted(result)
