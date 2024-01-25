#Home work 3 2nd
import random

def get_numbers_ticket(min, max, quantity):
    for numbers in [min, max, quantity]:
        if (1 <= numbers <= 1000):
            unique_numbers = random.sample(range(min, max + 1), quantity)
            return sorted(unique_numbers)
        else:
            return[]
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)