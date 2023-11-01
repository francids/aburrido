class Person:
    def __init__(self, name: str, lastname: str, age: int, country: str):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.country = country

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country}'

    def __repr__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country}'

    def work(self):
        print(f'{self.name} is working...')

    def play(self):
        print(f'{self.name} is playing...')


class Student(Person):
    def __init__(self, name: str, lastname: str, age: int, country: str, school: str):
        super().__init__(name, lastname, age, country)
        self.school = school

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.school}'

    def __repr__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.school}'

    def study(self):
        print(f'{self.name} is studying...')


class Teacher(Person):
    def __init__(self, name: str, lastname: str, age: int, country: str, school: str):
        super().__init__(name, lastname, age, country)
        self.school = school

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.school}'

    def __repr__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.school}'

    def teach(self):
        print(f'{self.name} is teaching...')
