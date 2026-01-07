from datetime import datetime

# Розраховує кількість днів між заданою датою і поточною датою
def get_days_from_today(date):
    # Перевірка правильності формату дати
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Неправильний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД.")
        return
    
    # Обчислення різниці в днях
    today = datetime.today()
    diff_days = today - date
    print(f"Кількість днів між {date.strftime('%Y-%m-%d')} і сьогоднішньою датою: {diff_days.days} днів.")


get_days_from_today(input("Введіть дату у форматі РРРР-ММ-ДД: "))




