#Home work 3 1st
from datetime import datetime

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference = current_date - user_date
        return difference.days
    except ValueError:
        return "Incorrect date format. Please use the 'YYYY-MM-DD' format."
date = input("Input date in format: yyyy-mm-dd ")

print(get_days_from_today(date))

