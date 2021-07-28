class Address:
    def __init__(self, street_number, street_name, city, state, zip_code):
        self.street_number = street_number
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        return f'{self.street_number} {self.street_name}, {self.city} ({self.state}), {self.zip_code}'


class Student:
    def __init__(self, name, age, student_id, address):
        self.name = name
        self.age = age
        self.id = student_id
        self.address = address

    def student_information(self):
        print('------------------------------------------------')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Id: {self.id}')
        print(f'Address: {self.address}')
        print('------------------------------------------------')


diego = Student('Diego Ortiz', 39, 'C0816681',
                Address('550', 'Milicent St.', 'Toronto', 'ON', 'MXS I8S'))
diego.student_information()
