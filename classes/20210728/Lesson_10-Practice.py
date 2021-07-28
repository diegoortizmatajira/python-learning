import datetime


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('------------------------------------------------')
        print(f'Restaurant name: {self.restaurant_name}')
        print(f'Cuisine type: {self.cuisine_type}')
        print(f'Clients served: {self.number_served}')
        print('------------------------------------------------')
        print()

    def open_restaurant(self):
        print('------------------ NOW OPEN --------------------')
        print(f'{self.restaurant_name:^48s}')
        print('------------------------------------------------')
        print()

    def set_number_served(self, value):
        self.number_served = value

    def increment_number_served(self, increment):
        self.number_served += increment


def task01():
    print("=========================\nTask 1\n-------------------------")
    restaurant = Restaurant('Colombian Express', 'Typical colombian food')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


def task02():
    print("=========================\nTask 2\n-------------------------")
    restaurants = [
        Restaurant('Colombian Express', 'Typical colombian food'),
        Restaurant('Sushi bar', 'Japanese food'),
        Restaurant('Canadian Hub', 'Poutine and Canadian food'),
    ]
    for restaurant in restaurants:
        restaurant.describe_restaurant()
        restaurant.open_restaurant()


class User:
    instance_count = 0

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.created_on = datetime.date(2019, 11, 15)
        self.last_login_date = datetime.date(2020, 10, 28)
        self.active = True
        self.login_attempts = 0
        User.instance_count += 1

    def summary(self):
        print(f'User id: {self.user_id}')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Last login: {self.last_login_date}')
        print(f'Login attempts: {self.login_attempts}')
        print(f'Status: {"Active" if self.active else "Inactive"}')
        print(f'Created on: {self.created_on.isoformat()}')
        print('------------------------------------------------')

    def greet(self):
        time_from_last_login = datetime.date.today() - self.last_login_date
        print(f'Welcome back {self.first_name} {self.last_name}')
        print(f'Has been {time_from_last_login.days} days since your last login.')
        print('------------------------------------------------')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


def task03():
    print("=========================\nTask 3\n-------------------------")
    users = [
        User('diegoortizmatajira', 'Diego', 'Ortiz'),
        User('mr_robot', 'Elliot', 'Alderson'),
        User('neo', 'Thomas', 'Anderson'),
    ]
    for user in users:
        print('\n************************************************')
        user.summary()
        user.greet()


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()  # titleCased value

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it. ")

    def drive_distance(self, distance):
        self.odometer_reading += distance


def task_odometer():
    print("=========================\nTask Odometer\n-------------------------")
    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.drive_distance(50)
    my_new_car.read_odometer()
    my_new_car.drive_distance(140)
    my_new_car.read_odometer()


def task04():
    print("=========================\nTask 4\n-------------------------")
    restaurant = Restaurant('Colombian Express', 'Typical colombian food')
    restaurant.describe_restaurant()
    print('Set number served = 150')
    restaurant.set_number_served(150)
    restaurant.describe_restaurant()
    print('Increment number served by 10')
    restaurant.increment_number_served(10)
    restaurant.describe_restaurant()


def task05():
    print("=========================\nTask 5\n-------------------------")
    user = User('diegoortizmatajira', 'Diego', 'Ortiz')
    user.summary()
    print('Perform one login attempt\n')
    user.increment_login_attempts()
    user.summary()
    print('Perform one login attempt\n')
    user.increment_login_attempts()
    user.summary()
    print('Perform reset to login attempts counter\n')
    user.reset_login_attempts()
    user.summary()


def task06():
    print("=========================\nTask 6\n-------------------------")
    users = [
        User('diegoortizmatajira', 'Diego', 'Ortiz'),
        User('mr_robot', 'Elliot', 'Alderson'),
        User('neo', 'Thomas', 'Anderson'),
    ]
    print(f'Number of instances: {users[0].instance_count}')


task01()
task02()
task03()
task_odometer()
task04()
task05()
task06()