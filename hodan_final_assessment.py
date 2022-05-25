# Exam 2- SPECIALISM 25/05/2022 - Hodan Omar
"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""

import random


class CFGStudent:

    def __init__(self, first_name, surname, age, email):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id(self)
        # i tried to pass student id when a new class object is generated, and then if no id is passed,
        # then student_id should be automatically generated and assigned to the class.
        # i tried this using a if statement so if not student_id = student_id then generated_student_id
        # but this caused errors so i just left it as student id allows a random generated id every time it's run

    @staticmethod
    def generate_id(self):
        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "
        self.student_id = str(random.randint(1000, 10000))
        return self.student_id

    def get_student_id(self):
        'your code goes here'
        'fetch student id'
        return self.student_id

    def get_fullname(self):
        "Expected outcome should be 'Name Surname' "
        'your code goes here'
        return self.first_name + self.surname


class NanoStudent(CFGStudent):

    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.student_id = self.generate_id(self)
        self.specialization = specialization
        self.course_grades = dict()

    @staticmethod
    def generate_id(self):
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "
        self.student_id = "NANO" + str(random.randint(1000, 10000))
        return self.student_id

    def add_new_grade(self, course, grade):
        'your code goes here'
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"
        self.course_grades = {course: grade}
        return self.course_grades

    # ^ does not add both courses and grades only one and that is the last one added meaning (project, 78), need to fix!
    # dictionary requires .update on add_new_grade function however whenever I do this i run into errors
    # so for now i left it as it is but in future i would work on making .update work to show both entries into dict

    def get_course_grades(self):
        'your code goes here'
        'fetch course grades container and its values'
        return self.course_grades


############################################

# Example run

s = CFGStudent('Anna', ' Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', first_name='Mia', surname=' Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_student_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}

"""
should return {'theory': 95, 'project': 78}


# # """

"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""


def sum_fib(limit):
    # where all fibonacci sequence will be stored
    fib_seq = []

    # nested functions
    # this function gets the fibonacci sequence
    # 1. Start with writing a stand alone function that can return n’th Fibonacci number -
    #    # this function gets the fibonacci sequence
    def get_fib_sequence(n):
        if n < 0:
            return False
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return get_fib_sequence(n - 1) + get_fib_sequence(n - 2)

    # get all fibonacci numbers up to the limit I set
    for x in range(limit):
        y = get_fib_sequence(x)
        fib_seq.append(y)
    # list to store all fibonacci even numbers
    get_fib_even = []
    # then the function to get all fibonacci even numbers and then sum them
    for z in fib_seq:
        if z % 2 == 0:
            get_fib_even.append(z)
    sum_of_fib_even = sum(get_fib_even)

    return sum_of_fib_even


# #### TESTS ####

print(sum_fib(10))  # should be 44
print(sum_fib(15))  # should be 188
print(sum_fib(1))  # should be 0

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""


def is_valid_subsequence(array, sequence):
    # list to store the now compared and confirmed numbers from both lists
    list1 = []
    # for loop to check both lists to determine whether the second array called sequence is a subsequence of the first
    # one.
    # this for loop also works as an iterator over both the iterables - array and sequence
    for x in sequence:
        for y in array:
            if x == y:  # only if i find first integer then continue iterating if not function returns False

                list1.append(y)  # here it appends, adding the now compared number from sequence in array to empty list
                # if it matches the number in array
    if list1 == sequence:
        return True
    else:
        return False
    # NOTE: A subsequence of an array in this case is a set of numbers that are not necessarily
    # adjacent in the array, but are in the same order as they appear in the array.

    # only if all the numbers in the second array have been compared to first array after for loop iterates
    # over iterables does it return- requires it to match and be a subsequence of first array
    # True and if only some or one numbers are the same then it will return False


array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, -2]
# as 1 6 and -1 in sequence 1 is the same as array 1 that will render it True but as -2 is not in array 1 but only in
# sequence1 then the whole function renders False as all numbers in sequence 1 need to match all numbers in array1
# in order for it to return True. If first number check in sequence does not match array it will stop and render False
# immediately as they need to appear in same order.

print(is_valid_subsequence(array1, sequence1))  # FALSE

array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [1, 6, -1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE

array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE

"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

"""
Following SOLID principles starting with single responsibility- it is important to make your program easy to implement. 
This means it is important to make it prepare for future changes. Ensure that each class only has one single
responsibility. As this is what single responsibility principle is in the case of the class employee it has too many
responsibilities. It does not follow this principle. In this class alone it updates_status and updates_department
and even removes employees. This is not effective and does not follow the principle it instead should have other classes
and subclasses using inheritance. Even the save_employee is an object which would be better if created in a new class 
for employee. It is confusing and not simple and too many things to change.

Secondly the Open Closed principle this principle describes how you should be able to add and extend but not modify.
This means you should be able to add functionality to classes and methods. But you should not change the code in the 
class. Do not touch the existing code and always write code that can be easily added to. Creating more functionality. 
In this case for employee class abstract classes or interfaces can help. The update_status in the class employee does
not follow the open close principle as it modifies the code instead of adding to it.
Some of the methods do not do what maybe they are expected to do and are not used. So the interface principle
in the SOLID principle is not followed in employee class as should not depend on methods you do not use or work.
Employee class has methods such as update_status.
Also for this employee class it does not follow the Liskov principle as this principle works so that a sub-class 
can work in place of its superclass without errors. So child class in place of parent class.
But there are no subclasses in this class employee it does not follow single responsibility so all the responsibility
lies in the only class the parent class employee.
Lastly the dependency principle, just works on high level modules not depending on low level modules. But in the class 
employee db.engine does a lot it saves, deletes. So for example, the delete depends on db.engine which shows
dependency principle is not being followed. 
Also there are a few errors- the init constructor shows is_active is declared but then self takes 
self.active_status = is_active but it needs to be self.is_active=is_active.
- self.id needs to be self.id_ as again the init constructor is self.id = id_
- similar in the update_status method, self.active_status = new_is_active but parameter passed is new_is_active 
- therefore it needs to be self.new_is_active = new_is_active.
- same in save_employee self.active_status needs ot be to self.is_active and self.id to self.id_ and the same self.id 
needs to be self.id_ in remove_employee and print_employee_report


"""
