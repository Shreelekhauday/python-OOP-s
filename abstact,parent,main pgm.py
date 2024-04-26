#abstract
from studentdetails import studentdetails
class Student(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
class Student1(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
class Student2(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
class Student3(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)

#parent pgm
from abc import ABC
class studentdetails(ABC):
    def __init__(self,sem,name,usn,rollno):
        self.sem=sem
        self.name=name
        self.usn=usn
        self.rollno=rollno
def display_details(self):
    pass


#main pgm
from student_details import Student, Student1, Student2, Student3

def main():
    student = Student( sem=3,name='shifa', usn='3b2r22ec149', rollno=44)
    student1 = Student1(sem=3,name='shobha', usn='3b2r22ec153', rollno=45)
    student2 = Student2(sem=3,name='shree', usn='3b2r22ec154', rollno=46)
    student3 = Student3(sem=3,name='shabbu',usn='3br22ec147', rollno=47)
    student.display_details()
    print("\n")
    student1.display_details()
    print("\n")
    student2.display_details()
    print("\n")
    student3.display_details()
    print("\n")


if __name__ == "__main__":
    main()