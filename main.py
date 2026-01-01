from datetime import datetime, date


users = [{'name': 'Alice', 'birthday': '1990.05.15'},
         {'name': 'Bob', 'birthday': '1985.12.20'}]


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user['birthday'].replace(year = today.year)
        
        
        print(birthday_this_year)
        
            
            
    return birthday_this_year
