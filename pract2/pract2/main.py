from datetime import date

def get_day_of_week(day, month, year):
        """Функция для определения дня недели по дате."""
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return days[date(year, month, day).weekday()]

def is_leap_year(year):
    """Функция, которая определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birth_date):
    """Функция для расчета возраста пользователя."""
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def display_digit(digit):
    # Шаблоны для отображения цифр от 0 до 9
    digits = {
        '0': [
            "***",
            "* *",
            "* *",
            "* *",
            "***"
        ],
        '1': [
            "**  ",
            " *  ",
            " *  ",
            " *  ",
            "*** "
        ],
        '2': [
            "*** ",
            "  * ",
            "*** ",
            "*   ",
            "*** "
        ],
        '3': [
            "*** ",
            "  * ",
            "*** ",
            "  * ",
            "*** "
        ],
        '4': [
            "* * ",
            "* * ",
            "*** ",
            "  * ",
            "  * "
        ],
        '5': [
            "*** ",
            "*   ",
            "*** ",
            "  * ",
            "*** "
        ],
        '6': [
            "*** ",
            "*   ",
            "*** ",
            "* * ",
            "*** "
        ],
        '7': [
            "*** ",
            "  * ",
            "  * ",
            "  * ",
            "  * "
        ],
        '8': [
            "*** ",
            "* * ",
            "*** ",
            "* * ",
            "*** "
        ],
        '9': [
            "*** ",
            "* * ",
            "*** ",
            "  * ",
            "*** "
        ]
    }
    return digits[str(digit)]

def print_date_in_tablo_format(day, month, year):
    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)
    year_str = str(year)
    date_chars = list(day_str + "." + month_str + "." + year_str)
    for i in range(5):
        line = ""
        for char in date_chars:
            if char == '.':
                line += "   "
            else:
                line += display_digit(int(char))[i]
        print(line)

# Запрашиваем у пользователя дату рождения
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))
day_of_week = get_day_of_week(day, month, year)
print(f"День недели рождения: {day_of_week}")
# Определяем, был ли год високосным
if is_leap_year(year):
    print(f"{year} год был високосным")
else:
    print(f"{year} год не был високосным")
# Определяем возраст пользователя
age = calculate_age(date(year, month, day))
print(f"Вам {age} лет")

# Выводим дату рождения в формате электронного табло
print("\nВаша дата рождения:")
print_date_in_tablo_format(day, month, year)