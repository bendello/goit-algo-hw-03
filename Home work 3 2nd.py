#Home work 3 2nd
import random

def get_numbers_ticket(min, max, quantity):
    for numbers in [min, max, quantity]:
        if (1 <= numbers <= 1000) and min <= max:
            unique_numbers = random.sample(range(min, max + 1), quantity)
            return sorted(unique_numbers)
        else:
            return[]
lottery_numbers = get_numbers_ticket(49, 1, 6)
print("Your lottery numbers are: ", lottery_numbers)