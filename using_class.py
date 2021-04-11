class StudentInfo():

    roll_no = 0
    name = ''
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def print_student_info(self):
        print(self.roll_no, self.name)

class StudentMarks(StudentInfo):

    def __init__(self,roll_no, name, marks_in_maths, marks_in_english, marks_in_science):
        super().__init__(name, roll_no)
        self.marks_in_maths = marks_in_maths
        self.marks_in_english = marks_in_english
        self.marks_in_science = marks_in_science

    def print_marks(self):
        super().print_student_info()
        print( self.marks_in_english, self.marks_in_maths, self.marks_in_science)



# student_info = StudentInfo('Raj', 1)
# student_info.print_student_info()

student_marks = StudentMarks(1, 'Raj', 78, 22, 44)
student_marks.print_marks()