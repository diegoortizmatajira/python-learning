# Create a csv
# Write, Read and append data to a file.
# Employee
# Employee_FName  Employee_LName EmployeeID    Employee_Salary
# 1.
# 2.
# 3.
# 4.
# 5.

def task_create_csv(file_name):
    print("=========================\nTask 1: Write a csv file\n-------------------------")
    with open(file_name, "w", encoding="utf-8") as output_file:
        output_file.write(f'Employee_FName,Employee_LName,EmployeeID,Employee_Salary\n')
        for i in range(6):
            first_name = f'First{i}'
            last_name = f'First{i}'
            id = f'2021{i}'
            salary = 5000 * i
            output_file.write(f'{first_name},{last_name},{id},{salary}\n')
            print(f'Added line {i + 1}')
        output_file.close()


def task_read_csv(file_name):
    print("=========================\nTask 2: Read a csv file\n-------------------------")
    with open(file_name, "r", encoding="utf-8") as input_file:
        content = input_file.readlines()
        count = 0
        for line in content:
            count += 1
            print(f'Line {count}: {line.split(",")}')


def task_append_to_csv(file_name):
    print("=========================\nTask 3: Append data to a csv file\n-------------------------")
    with open(file_name, "a", encoding="utf-8") as output_file:
        for i in range(6, 11):
            first_name = f'First{i}'
            last_name = f'First{i}'
            id = f'2021{i}'
            salary = 5000 * i
            output_file.write(f'{first_name},{last_name},{id},{salary}\n')
            print(f'Added line {i + 1}')
        output_file.close()


filename = 'output.csv'
task_create_csv(filename)
task_read_csv(filename)
task_append_to_csv(filename)
task_read_csv(filename)
