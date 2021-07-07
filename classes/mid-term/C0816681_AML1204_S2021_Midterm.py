# Part 2

def mark_assigner(student_number, final_grade):
    mark = ''
    if final_grade > 97:
        mark = 'A+'
    elif final_grade > 93:
        mark = 'A'
    elif final_grade > 90:
        mark = 'A-'
    elif final_grade > 87:
        mark = 'B+'
    elif final_grade > 83:
        mark = 'B'
    elif final_grade > 80:
        mark = 'B-'
    elif final_grade > 77:
        mark = 'C+'
    elif final_grade > 73:
        mark = 'C'
    elif final_grade > 70:
        mark = 'C-'
    elif final_grade > 67:
        mark = 'D+'
    elif final_grade > 63:
        mark = 'D'
    elif final_grade > 60:
        mark = 'D-'
    else:
        mark = 'F'
    return mark


# Part 1 and Part 3

def final_grade_calculator(student_number, aml_grade, big_data_grade, networking_grade, cloud_computing_grade,
                           python_grade):
    grades = [
        {'grade': aml_grade, 'weight': 100},
        {'grade': big_data_grade, 'weight': 100},
        {'grade': networking_grade, 'weight': 100},
        {'grade': cloud_computing_grade, 'weight': 100},
        {'grade': python_grade, 'weight': 100},
    ]
    weight_sum = 0
    grades_sum = 0
    for grade in grades:
        weight_sum += grade['weight']
        grades_sum += grade['grade'] * grade['weight']
    final_grade = grades_sum / weight_sum
    final_mark = mark_assigner(student_number, final_grade)
    print(
        f"Student number {student_number} has achieved the final grade of {final_grade:.2f} which is equivalent to {final_mark}")


# Test

final_grade_calculator("c123456-perfect", 100, 100, 100, 100, 100)
print("---------------------")
final_grade_calculator("c123456-bad", 0, 0, 0, 0, 0)
print("---------------------")
final_grade_calculator("c123456-average", 80, 90, 75, 45, 85)
