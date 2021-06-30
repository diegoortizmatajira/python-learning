def string_length(value):
    return len(value)


def practice_7_1():
    print("=========================\nPractice 7.1\n-------------------------")
    value = 'String to calculate the length'
    length = string_length(value)
    print(f"The length of '{value}' is {length}")


def character_frequency(value):
    result = {}
    for character in value:
        result[character] = result.get(character, 0) + 1
    return result


def practice_7_2():
    print("=========================\nPractice 7.2\n-------------------------")
    value = 'String to calculate character frequency'
    result = character_frequency(value)
    print(result)


def practice_7_3():
    print("=========================\nPractice 7.3\n-------------------------")


practice_7_1()
practice_7_2()
