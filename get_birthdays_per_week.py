"""
    Домашнє завдання №1
    Завдання №1
"""
from datetime import datetime
from datetime import timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    """
    Функція get_birthdays_per_week приймає список словників виду:
        [{"name": "Bill Goots", "birthday": datetime(1955, 2, 24)},
         {"name": "Foo Bar", "birthday": datetime(1975, 2, 26)},
         {"name": "John Smith", "birthday": datetime(1981, 3, 1)}]
    
    i виводить імена іменинників
        з днями народження на тиждень вперед від поточного дня,
        Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
        
        у форматі:
        Monday: Bill Goots, Foo Bar
        Friday: John Smith
    """
    today = datetime.today().date()
    weekday_to_name = []
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
        if birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            weekday_to_name.append((delta_days, birthday_this_year.strftime('%A'), name))
    weekday_to_name.sort()
    dd_list = defaultdict(list)
    for delta_days, weekday, name in weekday_to_name:
        dd_list[weekday].append(name)
    print('\n'.join([f"{day}: {', '.join(names)}" for day, names in dd_list.items()]))


def main():
    """
    Перевірка роботи get_birthdays_per_week
    """
    test_users = [{"name": "John Smith Jr", "birthday": datetime(2001, 3, 1)},
                  {"name": "Bill Goots", "birthday": datetime(1955, 2, 24)},
                  {"name": "Foo Bar", "birthday": datetime(1975, 2, 26)},
                  {"name": "John Smith", "birthday": datetime(2024, 2, 29)}]
    get_birthdays_per_week(test_users)

if __name__ == "__main__":
    main()
