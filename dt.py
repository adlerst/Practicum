import datetime as dt

# В эту переменную запишите формат для
# преобразования даты
FORMAT = '%d.%m.%Y'

# Добавьте в объявление функции ещё один параметр - имя
def get_days_to_birthday(name, date_birthday):
    # Преобразуйте полученную строку с датой в объект нужного типа
    date_birthday = dt.datetime.strptime(date_birthday, FORMAT)
    date_birthday = date_birthday.date()

    today = dt.date.today()
    date_birthday = date_birthday.replace(year=today.year)

    if date_birthday < today:
        date_birthday = date_birthday.replace(year=today.year + 1)

    days_to_birthday = date_birthday - dt.date.today()
    return f'{name}, до твоего дня рождения осталось дней: {days_to_birthday.days}'

birthdays = [
    ('Лера', '16.05.2015'),
    ('Максим', '16.12.2011'),
    ('Толя', '12.06.2016')
]

for arg in range(len(birthdays)):
    name, birthday = birthdays[arg]
    print(get_days_to_birthday(name, birthday))

# Напечатайте результат вызова функции get_days_to_birthday()
# для каждой пары из списка birthdays
#print(get_days_to_birthday('Лера', birthday))
#print(get_days_to_birthday('Максим', birthday))
#print(get_days_to_birthday('Толя', birthday))