#Home work 3 4th
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    today = datetime.today().date()

    upcoming = []

    for user in users:

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_diff = (birthday_this_year - today).days

        if 0 <= days_diff <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)
            upcoming.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")})

    return upcoming

users = [   {"name": "John Doe", "birthday": "1985.01.23"},
            {"name": "Amanda Sifred", "birthday": "1978.05.24"},
            {"name": "Will Smith", "birthday": "1965.01.26"},
            {"name": "Tom Cruise", "birthday": "1994.10.30"},
            {"name": "Vin Diesel", "birthday": "1984.01.27"}
        ]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List wishes on this week: ", upcoming_birthdays)
