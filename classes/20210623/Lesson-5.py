def practice_4_1():
    print("=========================\nPractice 4.1\n-------------------------")
    pizzas = ["Pepperoni", "Hawaiian", "Chicken-Bacon"]
    print("Only names:")
    for pizza in pizzas:
        print("-", pizza)
    print("Modified to print a statement:")
    for pizza in pizzas:
        print(f"- I love pizzas, {pizza} is one of my favorites")
    print("I love pizza with lots of cheese")
    print("I love pizza with meat")
    print("I love pizza when it is still hot, but also when it comes from the fridge")


def practice_4_2():
    print("=========================\nPractice 4.2\n-------------------------")
    animals = ["Cat", "Tiger", "Panther"]
    print("Only names:")
    for animal in animals:
        print("-", animal)
    print("Modified loop")
    for animal in animals:
        print(f"- A {animal} loves being pet, just be careful with their claws")
    print("Any of those animals is potentially dangerous!!!")


def practice_4_3():
    print("=========================\nPractice 4.3\n-------------------------")
    print("Printing numbers from 1 to 20")
    for i in range(1, 21):
        print("-", i)


def practice_4_4():
    print("=========================\nPractice 4.4\n-------------------------")
    number_list = [*range(1, 1000001)]
    count = len(number_list)
    # prints the first 50 elements
    for i in range(50):
        print(f"The item in the position {i} is: {number_list[i]}")
    print(f"And so it continues..")
    # prints the last 50 elements
    for i in range(50):
        print(f"The item in the position {count - 50 + i} is: {number_list[count - 50 + i]:,}")


def practice_4_5():
    print("=========================\nPractice 4.5\n-------------------------")
    number_list = [*range(1, 1000001)]
    print(f"The minimum value is: {min(number_list):,}")
    print(f"The maximum value is: {max(number_list):,}")
    print(f"The sum value is: {sum(number_list):,}")


def practice_4_6():
    print("=========================\nPractice 4.6\n-------------------------")
    print("Odd numbers:")
    for i in range(1, 50, 2):
        print(f"- {i}")


def practice_4_13():
    print("=========================\nPractice 4.13\n-------------------------")
    foods = ("Rice", "Fries", "Chicken breast", "Steak", "Ratatouille")
    for food in foods:
        print(f"- {food}")
    # foods[0] = "Spaghetti" # Does not work
    print("The menu has changed")
    foods = (foods[0], "Chips", foods[2], foods[3], "Caesar salad")
    for food in foods:
        print(f"- {food}")


def make_shirt(size='L', text='I love Python'):
    print(f"- The requested shirt is of size '{size}' with the text '{text}'")


def practice_8_3():
    print("=========================\nPractice 8.3\n-------------------------")
    make_shirt('L', 'I love Star Wars')
    make_shirt(size='M', text='I love Game of Thrones')


def practice_8_4():
    print("=========================\nPractice 8.4\n-------------------------")
    make_shirt()
    make_shirt('M')
    make_shirt(text='I love C#')


def describe_city(city, country='Canada'):
    print(f"- {city} may be found in {country}")


def practice_8_5():
    print("=========================\nPractice 8.5\n-------------------------")
    describe_city('Quebec')
    describe_city('Toronto')
    describe_city('Bogotá', 'Colombia')


def city_country(city, country):
    return f"{city}, {country}"


def practice_8_6():
    print("=========================\nPractice 8.6\n-------------------------")
    print(f"- {city_country('Bogotá', 'Colombia')}")
    print(f"- {city_country('Panamá', 'Panamá')}")
    print(f"- {city_country('Rome', 'Italy')}")


def make_album(artist_name, album_title, number_of_songs=None):
    if number_of_songs:
        return {'artist': artist_name, 'title': album_title, 'songs': number_of_songs}
    else:
        return {'artist': artist_name, 'title': album_title}


def practice_8_7():
    print("=========================\nPractice 8.7\n-------------------------")
    print(make_album("AC/DC", "The Razors Edge"))
    print(make_album("The Rolling Stones", "Let it Bleed"))
    print(make_album("Queen", "A Night At The Opera"))
    print(make_album("Lynyrd Skynyrd", "Second Helping", 10))


def practice_8_8():
    print("=========================\nPractice 8.8\n-------------------------")
    again = True
    while again:
        artist = input("Who is the artist?")
        album = input("What is the album's name?")
        print(make_album(artist, album))
        option = input("Do you want to continue? (y/n)")
        again = option.lower() == 'y'


practice_4_1()
practice_4_2()
practice_4_3()
practice_4_4()
practice_4_5()
practice_4_6()
practice_4_13()
practice_8_3()
practice_8_4()
practice_8_5()
practice_8_6()
practice_8_7()
practice_8_8()
