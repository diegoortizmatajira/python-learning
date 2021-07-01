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


print(1 / estimate_pi())
