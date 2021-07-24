import datetime


def task01():
    print("=========================\nTask 1\n-------------------------")
    birth_date = datetime.date(1982, 5, 1)
    print(f"Your birthday is: {birth_date}")
    today = datetime.date.today()
    print(f"Today is {today}")
    age = today - birth_date
    print(f"Your age today is {age.days // 365}")


def task02():
    print("=========================\nTask 2\n-------------------------")
    college_start_date = datetime.date(2021, 5, 3)
    print(f"Your college start was in: {college_start_date}")
    today = datetime.date.today()
    print(f"Today is {today}")
    college_age = today - college_start_date
    print(f"You have {college_age.days // 30} months in college")


task01()
task02()


def practice01():
    print("=========================\nPractice 1\n-------------------------")
    today = datetime.date.today()
    print(f"Today is {today:%A}")


def practice02():
    print("=========================\nPractice 2\n-------------------------")
    today = datetime.datetime.today()
    birthday_str = input('Please enter the birthday date in YYYY-MM-DD format: ')
    year, month, day = map(int, birthday_str.split('-'))
    # Builds the actual birthday date
    birthday_date = datetime.datetime(year, month, day)
    print(f'Your birthday is: {birthday_date:%b %d %Y}')
    age = today - birthday_date
    print(f"Your age today is {age.days // 365}")
    next_birthday_date = datetime.datetime(today.year, birthday_date.month, birthday_date.day)
    if next_birthday_date <= today:
        next_birthday_date = datetime.datetime(today.year + 1, birthday_date.month, birthday_date.day)
    print(f'Your next birthday is on: {next_birthday_date:%b %d %Y}')
    days_to_next_birthday = next_birthday_date - today
    seconds = days_to_next_birthday.seconds
    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minute = seconds // 60
    seconds = seconds - minute * 60
    print(f'You need to wait {days_to_next_birthday.days} days, {hours} hours, {minute} minutes, {seconds} seconds')


def practice03():
    print("=========================\nPractice 3\n-------------------------")
    today = datetime.datetime.today()
    birthday_str = input('Please enter the birthday date in YYYY-MM-DD format: ')
    year, month, day = map(int, birthday_str.split('-'))
    # Builds the actual birthday date
    birthday_date = datetime.datetime(year, month, day)
    age = birthday_date - today
    print(f'You have lived {age.seconds} seconds')


def practice04():
    print("=========================\nPractice 4\n-------------------------")
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    print(f'Today is: {today:%b %d %Y}')
    print(f'Yesteday was: {yesterday:%b %d %Y}')
    print(f'Tomorrow will be: {tomorrow:%b %d %Y}')


practice01()
practice02()
practice03()
practice04()
