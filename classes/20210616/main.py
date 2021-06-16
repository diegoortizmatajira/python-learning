invitees = ["Scarlet Johansson", "Freddie Mercury", "Jimmy Hendrix"]


def practice_3_4():
    print("=========================\nPractice 3.4\n-------------------------")
    print("The list has", len(invitees), "invitees")
    for invitee in invitees:
        print("- Dear " + invitee + ", you are invited to my dinner")


def practice_3_5():
    print("=========================\nPractice 3.5\n-------------------------")
    i = 1
    print("Sorry to hear that " + invitees[i] + " cannot make it to my dinner. Don't worry there will be a next time.")
    invitees[1] = "Gal Gadot"
    print("The new list has", len(invitees), "invitees")
    for invitee in invitees:
        print("- Dear " + invitee + ", you are invited to my dinner")


def practice_3_6():
    print("=========================\nPractice 3.6\n-------------------------")
    print("Hi guys, I found a bigger place... there will be more guests")
    invitees.insert(0, "Steve Rogers")
    invitees.insert(len(invitees) // 2, "King T'chala of Wakanda")
    invitees.insert(len(invitees), "Tony Stark")
    print("The new list has", len(invitees), "invitees")
    for invitee in invitees:
        print("- Dear " + invitee + ", you are invited to my dinner")


def practice_3_7():
    print("=========================\nPractice 3.7\n-------------------------")
    print("Hi guys, I got cancelled by the bigger place... I have to shrink the list to two people")
    uninvited = [0, 1, 2, 2]
    for i in uninvited:
        person = invitees.pop(i)
        print("- Sorry " + person + ", I had to cancel the event for you")
    print("The new list has", len(invitees), "invitees")
    for invitee in invitees:
        print("- Dear " + invitee + ", you are still invited to my dinner")
    print("Sorry ladies... I have to cancel the event for you too")
    del invitees[1]
    del invitees[0]
    print("The new list has", len(invitees), "invitees")
    if len(invitees) == 0:
        print("- The new list is empty :(")
    else:
        for invitee in invitees:
            print("- Dear " + invitee + ", you are still invited to my dinner")


def practice_3_8():
    print("=========================\nPractice 3.8\n-------------------------")
    places = ["Rome", "Tokio", "Maldive Islands", "Egypt", "New Zealand"]
    print("- - SORTING A COPY - -")
    sorted_places = sorted(places)
    print("Original List", places)
    print("Sorted List", sorted_places)
    print("- - REVERSING A COPY - -")
    reversed_places = reversed(places)
    print("Original List", places)
    print("Reversed List", reversed_places)
    print("- - SORTING THE SAME LIST - -")
    places.sort()
    print("Original List", places)
    print("- - REVERSING THE SAME LIST - -")
    places.sort(reverse=True)
    print("Original List", places)


def practice_3_9():
    print("=========================\nPractice 3.9\n-------------------------")
    print("The len() function was used on every step of the exercise from 3.4 to 3.7")


def practice_dictionaries():
    print("=========================\nPractice Dictionaries\n-------------------------")
    courses = {
        "Artificial Intelligence - A Canadian Perspective": "Farzad Amirjavid",
        "Python Programming In Canada": "Simrandeep Kaur",
        "Big Data Fundamentals - Data Storage Networking": "Aruna Dorai",
        "Professional Communication": "Mac Kite",
        "Data Science and Machine Learning In Canada": "Mohammad Islam",
    }
    for item in courses:
        print("Course name: ", item)
        print("Course teacher: ", courses[item])
        print("- - - - -")


practice_3_5()
practice_3_6()
practice_3_7()
practice_3_8()
practice_3_9()
practice_dictionaries()
