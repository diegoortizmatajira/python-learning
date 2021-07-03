import string


# Practice 7.1

def string_length(value):
    return len(value)


def practice_7_1():
    print("=========================\nPractice 7.1\n-------------------------")
    value = 'String to calculate the length'
    length = string_length(value)
    print(f"The length of '{value}' is {length}")


# Practice 7.2

def character_frequency(value):
    result = {}
    for character in value:
        result[character] = result.get(character, 0) + 1
    return result


def practice_7_2():
    print("=========================\nPractice 7.2\n-------------------------")
    value = 'String to calculate character frequency'
    print(value)
    result = character_frequency(value)
    print(result)

# Practice 7.3

def practice_7_3():
    print("=========================\nPractice 7.3\n-------------------------")
    fmt = string.Formatter()
    custom_string = "The items are {}, {} and {}"
    print("string.Formatter.format:\n - ", fmt.format(custom_string, 1, 2, 3))
    custom_string = "lorem ipsum dolor sit amet, consectetur adipiscing elit."
    line_jump = '\n'
    print(f"Original string:   {custom_string:>70}")
    print(f"string.capitalize: {custom_string.capitalize():>71}")
    print(f"string.casefold:   {custom_string.casefold():>70}")
    print(f"string.center:     {custom_string.center(70, '-')}")
    print(f"string.ljust:     {custom_string.ljust(70, '-')}")
    print(f"string.rjust:     {custom_string.rjust(70, '-')}")
    print(f"string.replace:     {custom_string.replace('ipsum', 'IPSUM'):>70}")
    print(f"string.rpartition:     {custom_string.rpartition('ipsum')}")
    print(f"string.splitlines:     {custom_string.replace(',', line_jump).splitlines()}")


def celsius_to_fahrenheit(celsius_input):
    return celsius_input * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit_input):
    return (fahrenheit_input - 32) * 5 / 9


def practice_7_4():
    print("=========================\nPractice 7.4\n-------------------------")
    for fahrenheit in [0, 32, 46.4, 212]:
        print(f"- {fahrenheit} Fahrenheit equals {fahrenheit_to_celsius(fahrenheit):.2f} Celsius")
    print("-------------------------")
    for celsius in [-17.77778, 0, 8, 100]:
        print(f"- {celsius} Celsius equals {celsius_to_fahrenheit(celsius):.2f} Fahrenheit")


practice_7_1()
practice_7_2()
practice_7_3()
practice_7_4()
