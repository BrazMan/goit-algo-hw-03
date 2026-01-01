import random

# Функція для генерації лотерейних номерів
def get_numbers_ticket(min, max, quantity):
    ticket = set()
    if min >= 1 and max <=1000 and 1 <=quantity <= max:
        for number in range(min, max):
            ticket.add(number)
        return random.sample(list(ticket), quantity)
    else:
        print('Мінімальне значення має бути не меншим за 1, максимальне не більшим за 1000, а '\
              'кількість номерів має бути в межах від мінімального до максимального значення.')
        exit()

min = input('Введіть мінімальне значення: ')
max = input('Введіть максимальне значення: ')
quantity = input('Введіть кількість номерів: ')

# Перевірка на коректність введених даних
try:
    int(min)
    int(max)
    int(quantity)
except ValueError:
    print('Будь ласка, введіть коректні числові значення для мінімального, максимального значень та кількості номерів.')
    exit() 

# Генерація та виведення лотерейних номерів
ticket_numbers = get_numbers_ticket(int(min), int(max), int(quantity))
print(sorted(ticket_numbers))