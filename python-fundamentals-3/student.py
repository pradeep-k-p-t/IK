class Student: 

    def __init__(self,name,age,gpa):
        self.name = name 
        self.age = age
        self.gpa = gpa

class Course: 
    
    def __init__(self,course_name):
        self.course_name = course_name
        self.student_list = []

    def add_student(self, student : Student)->None: 
        self.student_list.append(student)

    def find_top(self)->Student:
       max_gpa = 0 
       current_top_student = None
       for student in self.student_list:
            if student.gpa > max_gpa:
                max_gpa = student.gpa
                current_top_student = student
       return current_top_student
    
    
Student1 = Student("Alice",20,3.5)
Student2 = Student("Bob",22,3.8)
Student3 = Student("Charlie",19,3.2)
Course1 = Course("Math")
Course1.add_student(Student1)
Course1.add_student(Student2)
Course1.add_student(Student3)
top_student = Course1.find_top()
print(f"The top student is {top_student.name} with a GPA of {top_student.gpa}")

