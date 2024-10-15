import csv

employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", "250000", "М"],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", "75000", "Ж"],
    ["Струков Иван Сергеевич", "Старший программист", "23.09.2024", "150000", "М"],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", "120000", "Ж"],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", "50000", "М"],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", "200000", "М"],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", "100000", "Ж"]
]

with open('employees.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["ФИО", "Должность", "Дата найма", "Оклад", "Пол"])
    writer.writerows(employees) #сделал(подсмотрел....) так чтоб можно было обращаться быстро просто к конкретной части строки в словаре

from datetime import datetime

def find_employee(surname):# выбор работнкиа
    for employee in employees:
        if employee[0].split()[0] == surname:
            return employee 
    return None

def calculate_programmer_bonus(employee):#премию щитаем
    if "программист" in employee[1].lower():
        return int(employee[3]) * 0.03
    else:
        return 0

def calculate_bonus_for_all(employee):#подарочек 
    return 2000

def index_salary(employee): #индексируем зп
    hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
    years_worked = (datetime.now() - hire_date).days / 365
    
    if years_worked > 10:
        return int(employee[3]) * 1.07
    else:
        return int(employee[3]) * 1.05

def check_vacation(employee): #можно ли в отпуск данной особе узнаем
    hire_date = datetime.strptime(employee[2], "%d.%m.%Y")
    months_worked = (datetime.now() - hire_date).days / 30
    
    if months_worked > 6:#всем пора бы
        return "Пора в отпуск!"
    else:
        return "Рано в отпуск!"

while True:
    surname = input("Введите фамилию сотрудника (или 'выход' для завершения): ")
    
    if surname.lower() == 'выход': #выводим все что насчитано
        break
    
    employee = find_employee(surname)
    
    if employee:
        print(f"Сотрудник: {employee[0]}")
        print(f"Должность: {employee[1]}")
        print(f"Текущий оклад: {employee[3]}")
        print(f"Премия программисту: {calculate_programmer_bonus(employee)}")
        print(f"Премия в честь праздника: {calculate_bonus_for_all(employee)}")
        print(f"Индексированная зарплата: {index_salary(employee):.2f}")
        print(check_vacation(employee))
    else:
        print("Сотрудник не найден")

print("Программа завершена")
