"""
TASK 1
Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class EachItem(object):
    def __init__(self, item, price, amount):
        self.item = item
        self.price = price
        self.amount = amount


class CashRegister:
    def __init__(self):
        self.total_items = dict()
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        self.total_items.update(item)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, amount):
        total = self.get_total()
        discounted = total * ((100 - amount) / 100)
        return 'The price after discount is: ', discounted

    def display_items(self):
        return self.total_items

    def get_total(self):
        total = 0
        for item in self.total_items:
            total += self.total_items[item]
        return total

    def show_items(self):
        for x in self.total_items:
            print(x)

    def reset_register(self):
        self.total_price = {}
        self.total_items = 0
        self.discount = 0

#
# EXAMPLE code run:
# ADD


C = CashRegister()
print(C.display_items())
C.add_item({'Tie': 10})
C.add_item({'Bag': 18})
C.add_item({'Shirt': 20})
C.add_item({'Tights': 5})
print(C.display_items())
C.remove_item('Tie')
print(C.display_items())
C.show_items()
print(C.get_total())
print(C.apply_discount)




"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""

#


class Student:

    def __init__(self, name, age, id, year, overall_mark):
        self.name = name
        self.age = age
        self.id = id
        self.year = year
        self.subjects = dict()
        self.overall_mark = overall_mark


class Specialization(Student):
    def __init__(self, specialization, name, age, id, year):
        super().__init__(name, age, id, year)
        self.specialization = specialization

    def add_student(self, name, age, specialization):
        self.name.update(name)
        self.age.update(age)
        self.specialization.update(specialization)


#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class CFGStudent(Student):
    def __init__(self, name, age, id, year, overall_mark):
        super().__init__(name, age, id, year, overall_mark)

    def add_subject(self, subject):
        self.subjects.update(subject)

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        return self.subjects

    def add_mark(self, subjects):
        marks = []
        for subject in subjects:
            marks += self.subjects[subject]
        return marks

    def overall_mark(self, mark):
        pass


# Attempted objects below but they have some errors I couldn't quite figure out yet

# S = Student()
# S.add_student("Hodan", "23", "Software Student")
# print(S.view_subjects())
# S.add_subject("Maths")
# S.add_subject("English")
# S.add_subject("Science")
# S.add_subject("French")
# print(S.view_subjects())
# S.remove_subject("French")
# print(S.view_subjects())
# S.add_mark(60)
# S.overall_mark()

