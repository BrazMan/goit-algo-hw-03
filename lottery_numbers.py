import random

# Функція для генерації лотерейних номерів
def get_numbers_ticket(min_value, max_value, quantity):
    ticket = set()
    try:
        min_value = int(min_value)
        max_value = int(max_value)
        quantity = int(quantity) 
        if min_value >= 1 and max_value <=1000 and quantity <= (max_value - min_value + 1) and min_value < max_value:
            for number in range(min_value, max_value + 1):
                ticket.add(number)
            ticket_numbers = sorted(random.sample(list(ticket), quantity))
            return ticket_numbers
        else:
            return []
    except ValueError:
        print('Перевірте коректність введених даних. Мінімальне значення має бути не меншим за 1, максимальне не більшим за 1000, а '\
              'кількість номерів має бути в межах від мінімального до максимального значення.')
        return []

# Запит користувача на введення параметрів

min_value = input('Введіть мінімальне значення: ')
max_value = input('Введіть максимальне значення: ')
quantity = input('Введіть кількість номерів: ')

# Генерація та виведення лотерейних номерів
print('Ваші лотерейні номери:', get_numbers_ticket(min_value, max_value, quantity))