def task01():
    print("=========================\nTask 1\n-------------------------")
    n = 0
    while n < 10:
        print(n)
        n = n + 1


def task02():
    print("=========================\nTask 2\n-------------------------")
    for row in range(1, 5):
        for column in range(1, row + 1):
            print(column, end=' ')
        print()


def task03():
    print("=========================\nTask 3\n-------------------------")
    number = int(input('Please tell me one number to calculate the sum:'))
    number_sum = 0
    for i in range(number + 1):
        number_sum = number_sum + i
    print(f'The sum of the numbers from 0 to {number} is {number_sum}')


def task04():
    print("=========================\nTask 4\n-------------------------")
    number = int(input('Please tell me one number to display multiplication table:'))
    for i in range(1, 11):
        print(f'{number} x {i} = {i * number}')


def task05():
    print("=========================\nTask 5\n-------------------------")
    list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for n in list1:
        if n > 150:
            break
        if n % 5 == 0:
            print(n)


def task06():
    print("=========================\nTask 6\n-------------------------")
    number = input('Please tell me one number to count its digits:')
    print(f'The number that you have entered is: {number} and has {len(number)} digits')


def task07():
    print("=========================\nTask 7\n-------------------------")
    for row in range(5, 0, -1):
        for column in range(row, 0, -1):
            print(column, end=' ')
        print()


def task08():
    print("=========================\nTask 8\n-------------------------")
    list = [10, 20, 30, 40, 50]
    print(f'List: {list}')
    reversed_list = []
    for value in list:
        reversed_list.insert(0, value)
    print(f'Reversed list: {reversed_list}')


def task09():
    print("=========================\nTask 9\n-------------------------")
    for i in range(2):
        print(i)
    else:
        print('Done!')


def task10():
    print("=========================\nTask 10\n-------------------------")
    value = 0
    next_value = 1
    for i in range(10):
        print(value, end=' ')
        value, next_value = next_value, value + next_value


def task11():
    print("=========================\nTask 11\n-------------------------")
    number = int(input('Please tell me one number to calculate the factorial:'))
    number_factorial = 1
    for i in range(1, number + 1):
        number_factorial = number_factorial * i
    print(f'The factorial of the number {number} is {number_factorial}')


def task12():
    print("=========================\nTask 12\n-------------------------")
    print('This is a program to print prime numbers in a range...')
    start = int(input('Please enter the range start:'))
    end = int(input('Please enter the range end:'))
    for n in range(start, end + 1):
        is_prime = True
        for factor in range(2, n // 2):
            if n % factor == 0:
                is_prime = False
                break
        if is_prime:
            print(n)


task01()
task02()
task03()
task04()
task05()
task06()
task07()
task08()
task09()
task10()
task11()
task12()
