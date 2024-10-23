class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Имя: {self.name} , Возраст: {self.age}'
        def greet(self):
         f'Имя: {self.name} , Возраст: {self.age}'
    def greet1(self):
        print(f'Имя: {self.name} , Возраст: {self.age}')

person1 = Person("Anna", 25)

person1.greet1()
#print(person1.name)
#print(person1.age)
#print(person1.greet())

