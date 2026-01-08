import pathlib


workers_info_path = pathlib.Path(__file__).parent / 'workers_info.txt'



def salary_calculation(worker_data):
    with workers_info_path.open("r", encoding="utf-8") as file:
        workers_info = file.readlines()
        workers_info = [line.strip() for line in workers_info]
        total_salary = 0
        for worker in workers_info:
            worker_data = worker.split(',')
            salary = int(worker_data[1])
            total_salary += salary
    print(f'Загальний дохід: {total_salary}\nСередня заробітна плата: {total_salary / len(workers_info):.0f}')

try:
    salary_calculation(workers_info_path)
except FileNotFoundError:
    print("Файл не знайдено. Перевірте шлях до файлу.")