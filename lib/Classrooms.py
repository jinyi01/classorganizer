class Division:
    def __init__(self, grade, size):
        # ell = false means no special needs assistant, off by default
        self.grade = grade
        self.size = size
        self.ell = False
        self.student_list = []

    def __str__(self):
        return "{} ".format(str(self.grade)) + ", ".join([student.first_name for student in self.student_list])

    def add_student(self, student):
        if len(self.student_list) >= self.size:
            return False
        self.student_list.append(student)
