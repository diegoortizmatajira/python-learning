def validate_student_id(text_to_validate):
    if len(text_to_validate) < 6:
        return False, 'The id is too short, should be exactly 6 characters long'
    if len(text_to_validate) > 6:
        return False, 'The id is too long, should be exactly 6 characters long'
    if not text_to_validate[:2].isalpha():
        return False, 'Some of the first 3 characters are not alphabetic characters'
    if text_to_validate[:2].upper() != text_to_validate[:2]:
        return False, 'Some of the first 3 characters are not uppercase alphabetic characters'
    if not text_to_validate[-3:].isdigit():
        return False, 'Some of the last 3 characters are not numerical digits'
    return True, f"The Student Id '{text_to_validate}' you have provided is valid."


print('*********************************\nPerforming some tests\n---------------------------------')
tests = ['ABC123', 'abc123', 'abC1596', 'abc12', 'A1C123', 'ABC1D3']
for test in tests:
    result, message = validate_student_id(test)
    print(f'Validating "{test}" ==> Result: {result}, Message: "{message}"')

print('*********************************\nUser Input tests\n---------------------------------')
repeat = True
while repeat:
    value = input("Please write a Student ID (3 capital letters and 3 digits): ")
    result, message = validate_student_id(value)
    print("The result of the validation is: {}".format(message))
    if result:
        break
    repeat = input("Do you want to retry (y/n)? ").lower() == 'y'

print('Ok, Good bye')
