from datetime import datetime

# Розраховує кількість днів між заданою датою і поточною датою
def get_days_from_today(date): 
    date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today()
    diff_days = today - date
    
    return diff_days.days

input_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")

 # Перевірка правильності формату дати
try:
    datetime.strptime(input_date, '%Y-%m-%d')
except ValueError:
    print("Неправильний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД.")
    exit()

days_difference = get_days_from_today(input_date)

print(f"Кількість днів між {input_date} і сьогоднішньою датою: {days_difference} днів.")


