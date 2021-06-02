def MyPrint(title, value):
    print(title, value, "... And its type is: ", type(value))


def Exercise_2_1():
    print("=========================\nExercise 2.1\n-------------------------")
    confirmation_message = "Your account has been created"
    MyPrint("Confirmation message: ", confirmation_message)


def Exercise_2_2():
    print("=========================\nExercise 2.2\n-------------------------")
    confirmation_message = "Your account has been created"
    MyPrint("Confirmation message: ", confirmation_message)
    confirmation_message = "Your account has been modified"
    MyPrint("Modified message: ", confirmation_message)


def Exercise_2_3():
    print("=========================\nExercise 2.3\n-------------------------")
    customer_name = "Diego Ortiz"
    print("Hello, " + customer_name + " it is a pleasure to meet you.")


def Exercise_2_4():
    print("=========================\nExercise 2.4\n-------------------------")
    customer_name = "Diego Ortiz"
    print("lowercase: " + customer_name.lower())
    print("uppercase: " + customer_name.upper())
    print("camelcase: " + customer_name.title())


def Exercise_2_5():
    print("=========================\nExercise 2.5\n-------------------------")
    quote = "You Don't Know The Power Of The Dark Side"
    autor = "Dart Vader"
    print(autor + ' once said, "' + quote + '"')


def Exercise_2_6():
    print("=========================\nExercise 2.6\n-------------------------")
    quote = "You Don't Know The Power Of The Dark Side"
    famous_person = "  Dart Vader   "
    message = famous_person + ' once said, "' + quote + '"'
    print(message)


def Exercise_2_7():
    print("=========================\nExercise 2.7\n-------------------------")
    famous_person = " \n\t  Dart Vader  \n\t "
    print("un-stripped: ", famous_person)
    print("Left stripped: ", famous_person.lstrip("\n\t "))
    print("Right stripped: ", famous_person.rstrip("\n\t "))
    print("Stripped: ", famous_person.strip("\n\t "))


def Exercise_2_8():
    print("=========================\nExercise 2.8\n-------------------------")
    MyPrint("5+3", 5 + 3)
    MyPrint("16/2", 16 / 2)
    MyPrint("10-2", 10 - 2)
    MyPrint("4*2", 4 * 2)


def Exercise_2_9():
    print("=========================\nExercise 2.9\n-------------------------")
    favorite_number = 64
    print("My favorite number is:", favorite_number)


Exercise_2_1()
Exercise_2_2()
Exercise_2_3()
Exercise_2_4()
Exercise_2_5()
Exercise_2_6()
Exercise_2_7()
Exercise_2_8()
Exercise_2_9()
