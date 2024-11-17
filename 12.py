# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f'Имя: {self.name} , Возраст: {self.age}'
#         def greet(self):
#          f'Имя: {self.name} , Возраст: {self.age}'
#     def greet1(self):
#         print(f'Имя: {self.name} , Возраст: {self.age}')

# person1 = Person("Anna", 25)
# person2 = Person("Bob", 54)
# # person2.greet1()
# # person1.greet1()
# # #print(person1.name)
# # #print(person1.age)cle
# # print(person1.greet())

# # class Triangle:
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #         pass

# #     def get_area(self):
# #         return f'Площадь треугольника: {self.width * self.height}'
# #         pass

# # tri1 = Triangle(10, 20)

# # print(tri1.get_area())


# class Triangle:
#     def set_attr(self, width, height):
#         self.width = width
#         self.height = height
#         pass

#     def get_area(self):
#         return f'Площадь треугольника: {self.width * self.height}'
#         pass

# tri1 = Triangle()
# tri1.set_attr(10, 20)

# #print(tri1.get_area())

# class Employee():
    
#     def get_vaules(self, name, surname, age, salary):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.salary = salary
#     def get_sex(self, sex):
#         self.sex = sex
    

#     def output(self):
#         return f'Имя: {self.name}\nФамилия: {self.surname}\nВозраст: {self.age}\nЗарплата: {self.salary}\nПол: {self.sex}'


# Ivan = Employee()
# Ivan.get_sex("Мужской")
# Ivan.get_vaules("Иван", "Иванов", 25, 35000)
# print(Ivan.output())
# print(Ivan.surname)

# class MyClass:
#     class_attr = 10

#     def __init__(self, value):
        
#         self.inst_attr = value

#     @classmethod

#     def mod_class_sttr(cls, n_value):

#         cls.class_attr = n_value

#     #def update(self, value):

        
# obj1 = MyClass(42)
# obj1 = MyClass(50)
# obj1.mod_class_sttr(15)

# print(obj1.inst_attr)

class LiteChecker:

    @staticmethod
    def has_dup(input_list):
        if len(set(input_list)) != len(input_list):
            return True
        return False

spis = [5, 3, 6]
result = LiteChecker.has_dup(spis)
#print(result)

class String:
    @staticmethod
    def line(string):
        string = reversed(string)
        return ''.join(string)

old_str = "Hello, world!"
new_str = String.line(old_str)
#print(new_str)

class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return print(f'{self.name} говорит привет')

Dima = Student("Дима")
Dima.greet()