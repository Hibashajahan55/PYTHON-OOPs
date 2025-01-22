# Question 1: (5 Marks)
"""
Build a program to manage a university's course catalog. You want to define a base class Course that has the following properties:
course_code: a string representing the course code (e.g., "CS101")
course_name: a string representing the course name (e.g., "Introduction to Computer Science")
credit_hours: an integer representing the credit hours for the course (e.g., 3)
You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major.
ElectiveCourse should have an additional property elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").
"""

class Course:
    def __init__(self,course_code,course_name,credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display(self):
        print(f"course_code: {self.course_code}\ncourse_name: {self.course_name}\ncredit_hours: {self.credit_hours}")
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display(self):
        super().display()
        print("required_for_major:",self.required_for_major,"\n")


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display(self):
        super().display()
        print("elective_type:",self.elective_type,"\n")


CoreCourse_1= CoreCourse("CS101", "Introduction to Computer Science", 3, True)
ElectiveCourse_1 = ElectiveCourse("CS300", "Artificial Intelligence", 2, "Technical")
CoreCourse_1.display()
ElectiveCourse_1.display()


#
# Question 2: (5 Marks)
"""
Create a Python module named employee that contains a class Employee with attributes name, salary
and methods get_name() and get_salary().
Write a program to use this module to create an object of the Employee class and display its name and salary.
"""

import employee
emp= employee.Employee("Ananyaa", 50000)
emp.get_name()
emp.get_salary()


