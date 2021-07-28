class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def can_move(self):
        print(f'{self.name} can walk on 4 feet')

    def can_eat(self):
        print(f'{self.name} can eat anything')

    def can_make_sound(self):
        print(f'{self.name} can bark')

    def get_human_age(self):
        print(f'{self.name} has {self.age * 7} human years equivalence')


milu = Dog('Milu', 2)
print(f"The dog's name is {milu.name}")
milu.can_eat()
milu.can_move()
milu.can_make_sound()
milu.get_human_age()
