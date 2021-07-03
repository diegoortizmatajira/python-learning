# Part 1) The simplest encryption algorithm!

# Provides the sets of alphabetical characters to be used, defined by the first and last code
character_sets = [
    (ord('A'), ord('Z')),
    (ord('a'), ord('z')),
]


# Provides the encryption of a single character with a given set of characters and delta value
# Returns two values
# - A boolean value indicating if the character is part of the character set defined by case_range.
# - The encrypted character
def caesar_cypher_character(character_code, case_range, delta):
    if character_code < case_range[0] or character_code > case_range[1]:
        return False, None
    position = character_code - case_range[0]
    new_position = (position - delta) % (case_range[1] - case_range[0] + 1)
    return True, chr(case_range[0] + new_position)


# Provides the encryption of an entire string value using a delta value.
# Returns the encrypted text.
def caesar_cypher(text, delta):
    result = ''
    for character in text:
        character_code = ord(character)
        ok = False
        for character_set in character_sets:
            ok, new_character = caesar_cypher_character(character_code, character_set, delta)
            if ok:
                result += new_character
                break
        if not ok:
            result += character
    return result


# Unit test to make sure the function works correctly.
def unit_test_caesar_cypher(text, expected, delta):
    print("-----------------------------")
    result = caesar_cypher(text, delta)
    print(f"Original text:  {text}")
    print(f"Encrypted text: {result}")
    print(f"Expected text:  {expected}")
    print(f"Result matched the expected value: {result == expected}")


def part_1():
    text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    expected = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'

    delta = 3
    unit_test_caesar_cypher(text.upper(), expected.upper(), delta)
    unit_test_caesar_cypher(text.lower(), expected.lower(), delta)
    unit_test_caesar_cypher(text.title(), expected.title(), delta)


part_1()


# Part 2) Binary Search Algorithm Implementation in Python

# Part 3) Formula Implementation
