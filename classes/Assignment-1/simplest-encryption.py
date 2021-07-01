character_ranges = [
    (ord('A'), ord('Z')),
    (ord('a'), ord('z')),
]


def caesar_cypher_character(character_code, case_range, delta):
    if character_code < case_range[0] or character_code > case_range[1]:
        return False, None
    position = character_code - case_range[0]
    new_position = (position - delta) % (case_range[1] - case_range[0] + 1)
    return True, chr(case_range[0] + new_position)


def caesar_cypher(text, delta):
    result = ''
    for character in text:
        character_code = ord(character)
        ok = False
        for character_range in character_ranges:
            ok, new_character = caesar_cypher_character(character_code, character_range, delta)
            if ok:
                result += new_character
                break
        if not ok:
            result += character
    return result


def test_caesar_cypher():
    text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    expected = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'
    cypher = caesar_cypher(text, 3) == expected
    cypher_lower = caesar_cypher(text.lower(), 3) == expected.lower()
    cypher_title = caesar_cypher(text.title(), 3) == expected.title()
    return cypher and cypher_lower and cypher_title


print(test_caesar_cypher())
