def binary_search_test(sorted_list, value, initial=0):
    if not sorted_list:
        return False
    else:
        size = len(sorted_list)
        guess = size // 2
        print(f"({initial},{initial + size - 1}) {sorted_list[guess]} vs {value} in {guess + initial}")
        if value == sorted_list[guess]:
            print(f"Found in position {initial + guess}")
            return True
        elif value > sorted_list[guess]:
            return binary_search_test(sorted_list[guess + 1:], value, initial + guess + 1)
        else:
            return binary_search_test(sorted_list[:guess], value, initial)


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


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for item in [2, 97, 25, 5]:
    # exists = binary_search(primes, item)
    exists = binary_search_test(primes, item)
    print(exists)
