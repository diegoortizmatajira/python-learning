def practice_5_1():
    print("=========================\nPractice 5.1\n-------------------------")
    character = "Obi Wan Kenobi"
    print("1. Is character == 'Obi Wan Kenobi'? I Predict True")
    print(character == 'Obi Wan Kenobi')
    print("2. Is character == 'Luke Skywalker'? I Predict False")
    print(character == 'Luke Skywalker')

    character = 'Yoda'
    print("3. Is character == 'Yoda'? I Predict True")
    print(character == 'Yoda')
    print("4. Is character == 'Dart Vader'? I Predict False")
    print(character == 'Dart Vader')

    character = 'Han Solo'
    print("5. Is character == 'Han Solo'? I Predict True, He shooted first")
    print(character == 'Han Solo')
    print("6. Is character == 'Greedo'? I Predict False")
    print(character == 'Greedo')

    dart_vader_children = 2
    print("7. Is dart_vader_children == 2? I Predict True, Luke and Leia")
    print(dart_vader_children == 2)
    print("8. Is dart_vader_children == 1? I Predict False")
    print(dart_vader_children == 1)

    worst_star_wars_episode = 1
    print("9. Is worst_star_wars_episode == 1? I Predict True, it is the worst")
    print(worst_star_wars_episode == 1)
    print("10. Is worst_star_wars_episode == 4? I Predict False")
    print(worst_star_wars_episode == 4)


def practice_5_2():
    print("=========================\nPractice 5.2\n-------------------------")
    print("Equality with strings\n- - - - - - -")
    print("- 'ABC' == 'ABC' I Predict True")
    print('ABC' == 'ABC')
    print("- 'ABC' == 'abc' I Predict False")
    print('ABC' == 'abc')

    print("\nInequality with strings\n- - - - - - -")
    print("- 'CDE' != 'ABC' I Predict True")
    print('CDE' != 'ABC')
    print("- 'abd' != 'abc' I Predict False")
    print('abc' != 'abc')

    print("\nlower() method\n- - - - - - -")
    print("- 'ABC'.lower() == 'ABC'.lower() I Predict True")
    print('ABC'.lower() == 'ABC'.lower())
    print("- 'ABC' == 'ABC'.lower() I Predict False")
    print('ABC' == 'ABC'.lower())

    print("\nNumerical tests\n- - - - - - -")
    print("- 1 > 0 I Predict True")
    print(1 > 0)
    print("- 1 < 0 I Predict False")
    print(1 < 0)
    print("- 4 >= 3 I Predict True")
    print(4 >= 3)
    print("- 4 <= 3 I Predict False")
    print(4 <= 3)
    print("- 96 == 96 I Predict True")
    print(96 == 96)
    print("- 96 != 96 I Predict False")
    print(96 != 96)

    print("\nLogical operators\n- - - - - - -")
    print("- True or False, I expect True")
    print(True or False)
    print("- False or False, I expect False")
    print(False or False)
    print("- True and True, I expect True")
    print(True and True)
    print("- True and False, I expect False")
    print(True and False)

    test_list = ["One", "Two", "Three", "Four"]
    print("We are going to use the list:", test_list)

    print("\nIn a List\n- - - - - - -")
    print("- 'One' is in the list, I expect True")
    print("One" in test_list)
    print("- 'Five' is in the list, I expect False")
    print("Five" in test_list)

    print("\nNot in a List\n- - - - - - -")
    print("- 'Five' is not in the list, I expect True")
    print("Five" not in test_list)
    print("- 'One' is not in the list, I expect False")
    print("One" not in test_list)


def test_alien01(alien_color):
    print("*************************************************")
    print(f"Testing the alien color, it currently is {alien_color}")
    if alien_color == "green":
        print("- Player has earned 5 points")


def practice_5_3():
    print("=========================\nPractice 5.3\n-------------------------")
    test_alien01("green")
    test_alien01("yellow")
    test_alien01("red")


def test_alien02(alien_color):
    print("*************************************************")
    print(f"Testing the alien color, it currently is {alien_color}")
    if alien_color == "green":
        print("- Player has earned 5 points")
    else:
        print("- Player has earned 10 points")


def practice_5_4():
    print("=========================\nPractice 5.4\n-------------------------")
    test_alien02("green")
    test_alien02("yellow")
    test_alien02("red")


def test_alien03(alien_color):
    print("*************************************************")
    print(f"Testing the alien color, it currently is {alien_color}")
    if alien_color == "green":
        print("- Player has earned 5 points")
    elif alien_color == "yellow":
        print("- Player has earned 10 points")
    elif alien_color == "red":
        print("- Player has earned 15 points")


def practice_5_5():
    print("=========================\nPractice 5.5\n-------------------------")
    test_alien03("green")
    test_alien03("yellow")
    test_alien03("red")


def stages_of_life(age):
    print("*************************************************")
    print(f"We are evaluating a person who is {age}")
    if age < 2:
        print("- This person is a baby")
    elif age < 4:
        print("- This person is a toddler")
    elif age < 13:
        print("- This person is a kid")
    elif age < 20:
        print("- This person is a teenager")
    elif age < 65:
        print("- This person is a adult")
    else:
        print("- This person is a elder")


def practice_5_6():
    print("=========================\nPractice 5.6\n-------------------------")
    stages_of_life(0)
    stages_of_life(1)
    stages_of_life(3)
    stages_of_life(4)
    stages_of_life(12)
    stages_of_life(13)
    stages_of_life(19)
    stages_of_life(21)
    stages_of_life(45)
    stages_of_life(65)
    stages_of_life(70)


def practice_5_7():
    print("=========================\nPractice 5.7\n-------------------------")
    fruit_list = ["strawberry", "passion fruit", "mango"]
    if "blackberry" in fruit_list:
        print(f"Ohh, blackberry is one of your favorites!")
    if "pineapple" in fruit_list:
        print(f"Ohh, pineapple is one of your favorites!")
    if "mango" in fruit_list:
        print(f"Ohh, mango is one of your favorites!")
    if "banana" in fruit_list:
        print(f"Ohh, banana is one of your favorites!")
    if "strawberry" in fruit_list:
        print(f"Ohh, strawberry is one of your favorites!")


users = ["admin", "user1", "user2", "user3"]


def welcome_user(user):
    if user == "admin":
        print("Hello admin, you have access to everything")
    else:
        print(f"Hello {user}, welcome back. What can I do for you?")


def practice_5_8():
    print("=========================\nPractice 5.8\n-------------------------")
    for user in users:
        welcome_user(user)


def practice_5_9():
    print("=========================\nPractice 5.9\n-------------------------")
    users.clear()
    if len(users) == 0:
        print("We need to fin some users!")
    else:
        for user in users:
            welcome_user(user)


def practice_5_10():
    print("=========================\nPractice 5.10\n-------------------------")
    current_users = ["admin", "user1", "user2", "user3"]
    verifiable_users = []
    for user in current_users:
        verifiable_users.append(user.lower())
    new_users = ["User1", "user4", "user5", "admIn"]

    for user in new_users:
        if user.lower() in verifiable_users:
            print(f"You will need to use another user id, '{user}' has been already taken")
        else:
            print(f"The user '{user}' is available")


def practice_5_11():
    print("=========================\nPractice 5.11\n-------------------------")
    number_list = [*range(1, 10)]
    for number in number_list:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")


practice_5_1()
practice_5_2()
practice_5_3()
practice_5_4()
practice_5_5()
practice_5_6()
practice_5_7()
practice_5_8()
practice_5_9()
practice_5_10()
practice_5_11()
