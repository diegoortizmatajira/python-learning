# Part 1) The simplest encryption algorithm!

def caesar_cypher(text, delta):
    result = ''
    for character in text:
        if character.isalpha():
            base = ord('a')
            if character == character.upper():
                base = ord('A')
            position = ord(character) - base
            new_position = (position - delta) % 26
            result += chr(base + new_position)
        else:
            result += character
    return result


# Unit test to make sure the function works correctly.
def test_caesar_cypher(text, expected, delta):
    result = caesar_cypher(text, delta)
    print(f"Original text:  {text}")
    print(f"Encrypted text: {result}")
    print(f"Expected text:  {expected}")
    print(f"Result matched the expected value: {result == expected}")
    print("-----------------------------")


def part_1():
    print(
            '*************************************************\n Part 1 \n*************************************************')
    text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    expected = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'
    delta = 3
    test_caesar_cypher(text.upper(), expected.upper(), delta)
    test_caesar_cypher(text.lower(), expected.lower(), delta)
    test_caesar_cypher(text.title(), expected.title(), delta)


part_1()


# Part 2) Binary Search Algorithm Implementation in Python

def binary_search(sorted_list, value):
    if not sorted_list:
        return False
    else:
        size = len(sorted_list)
        guess = size // 2
        if value == sorted_list[guess]:
            return True
        elif value > sorted_list[guess]:
            return binary_search(sorted_list[guess + 1:], value)
        else:
            return binary_search(sorted_list[:guess], value)


def part_2():
    print(
            '*************************************************\n Part 2 \n*************************************************')
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print("Full list of prime numbers: ", primes)
    for item in [2, 97, 25, 5]:
        exists = binary_search(primes, item)
        print(f"Looking for the value {item}, Exists: {exists}")


part_2()

# Part 3) Formula Implementation

from math import factorial, sqrt


def estimate_pi():
    accumulated_sum = 0
    limit_reached = False
    k = 0
    while not limit_reached:
        term = factorial(4 * k) * (1103 + 26390 * k) / ((factorial(k) ** 4) * (396 ** (4 * k)))
        accumulated_sum += term
        limit_reached = term < 1e-15
        k += 1
    return 2 * sqrt(2) * accumulated_sum / 9801


def part_3():
    print(
            '*************************************************\n Part 3 \n*************************************************')
    reverse_of_pi = estimate_pi()
    print(f"The result of the calculation is: {reverse_of_pi}")
    print(f"Therefore the estimation of Pi is: {1 / reverse_of_pi}")


part_3()
