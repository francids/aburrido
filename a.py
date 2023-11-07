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


class Worker(Person):
    def __init__(self, name: str, lastname: str, age: int, country: str, company: str):
        super().__init__(name, lastname, age, country)
        self.company = company

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.company}'

    def __repr__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.company}'

    def work(self):
        print(f'{self.name} is working...')


class Player(Person):
    def __init__(self, name: str, lastname: str, age: int, country: str, team: str):
        super().__init__(name, lastname, age, country)
        self.team = team

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.team}'

    def __repr__(self):
        return f'{self.name} {self.lastname} ({self.age}): {self.country} - {self.team}'

    def play(self):
        print(f'{self.name} is playing...')
