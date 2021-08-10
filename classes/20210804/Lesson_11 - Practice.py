def task_01():
    print("=========================\nTask 1\n-------------------------")
    print('* * * * * * *\nReading all at once\n* * * * * * *')
    with open('Lesson_11 - Practice.txt', "r", encoding="utf-8") as input_file:
        content = input_file.readlines()
        count = 0
        for line in content:
            count += 1
            print(f'Line {count}: {line}')
        input_file.close()

    print('* * * * * * *\nReading by looping\n* * * * * * *')
    with open('Lesson_11 - Practice.txt', "r", encoding="utf-8") as input_file:
        line = input_file.readline()
        count = 0
        while line:
            count += 1
            print(f'Line {count}: {line}')
            line = input_file.readline()
        input_file.close()

    print('* * * * * * *\nReading once, print later\n* * * * * * *')
    lines = []
    with open('Lesson_11 - Practice.txt', "r", encoding="utf-8") as input_file:
        line = input_file.readline()
        while line:
            lines.append(line)
            line = input_file.readline()
        input_file.close()
    count = 0
    for line in lines:
        count += 1
        print(f'Line {count}: {line}')


def task_02():
    print("=========================\nTask 2\n-------------------------")
    with open('Lesson_11 - Practice.txt', "r", encoding="utf-8") as input_file:
        content = input_file.readlines()
        count = 0
        for line in content:
            count += 1
            print(f'Line {count}: {line.replace("Python", "Go")}')
        input_file.close()


def task_03():
    print("=========================\nTask 3\n-------------------------")
    name = input('Please tell me your name: ')
    if name:
        with open('guest.txt', "a", encoding="utf-8") as output_file:
            output_file.write(name + '\n')
            output_file.close()


def task_04():
    print("=========================\nTask 4\n-------------------------")
    name = '*'
    while name:
        name = input('Please tell me your name (leave empty to exit): ')
        if name:
            print(f"Hello {name}, welcome to this program, your name will be recorded as a guest")
            with open('guest.txt', "a", encoding="utf-8") as output_file:
                output_file.write(name + '\n')
                output_file.close()


def task_05():
    print("=========================\nTask 5\n-------------------------")
    reason = '*'
    while reason:
        reason = input('Please tell me a reason you love programming (leave empty to exit): ')
        if reason:
            with open('reasons.txt', "a", encoding="utf-8") as output_file:
                output_file.write(reason + '\n')
                output_file.close()


class Credential:
    def __init__(self, string_line: str):
        parts = string_line.split(',')
        self.name = parts[0]
        self.password = parts[1]

    def validate(self, name: str, password: str) -> bool:
        return (self.name == name) & (self.password == password)


def interesting_task():
    print("=========================\nInteresting Task\n-------------------------")
    credentials: list[Credential] = []
    with open('credentials.txt', "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
        for line in lines:
            credentials.append(Credential(line.strip('\n\r')))
        input_file.close()
        name = input('Please enter your username: ')
        password = input('Please enter your password: ')
        for user in credentials:
            if user.validate(name, password):
                print("User authenticated")
                return
        else:
            print("User not authenticated")


# task_01()
# task_02()
# task_03()
# task_04()
# task_05()
interesting_task()
