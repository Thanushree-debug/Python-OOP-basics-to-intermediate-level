class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no = roll_no
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def get_marks(self):
        return self.__marks
    
    def add_marks(self,subject , marks):
        self.__marks[subject]=marks

    def calculate_avg(self):
        total=0
        for marks in self.__marks.values():
            total += marks
            average = total/len(self.__marks)
            #print(f"{self.name}'s average:{average}") # should not be used
            return average
        

    def is_pass(self):
        has_passed = all(mark<35 for mark in self.__marks.values()) #any and all functins 
        if has_passed:
            print(f"{self.name} has cleared all subjects")
        else:
            print(f"{self.name} has failed")

    def calculate_grade(self):
        print("grade : " , end=" ") 
        percentage=self.calculate_avg()
        if percentage>=90:
            print("grade A")

        elif percentage>=75 and percentage<=90:
            print("grade B")

        else:
            print("C")

class report_card:
    @staticmethod #static method 
    def generate(student:Student):
        student_marks = student.get_marks()
        print(f"\n name = {student.name} \t roll no:{student.roll_no}")
        print("-----MARKS-----")
        for subject , marks in student_marks.items():
            print(f"{subject} = {marks}")
        print("-----------")
        print(f"Average: {student.calculate_avg()}")
        student.is_pass()
        student.calculate_grade()
        print("\n")

a = Student("akash" , 1 , {}) #creating a empty dict
a.add_marks("maths" , 95)
a.add_marks("science" , 13)
a.add_marks("physics" , 32)

report_card.generate(a)

