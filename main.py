import random
import os
import csv
from lib import Classrooms
from lib import Students

cwd = os.getcwd()

student_list = []

with open(cwd + r'\StudentList\students.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        student_list.append(Students.Student(*row))
    # delete header row
    del student_list[0]

# list of grades
grades = {
    'K': [],
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
}

for student in student_list:
    for grade in ['K', '1', '2', '3', '4', '5', '6', '7']:
        if student.grade == grade:
            grades[grade].append(student)


classrooms = []
for counter, grade in enumerate(grades.keys()):
    classrooms.append(Classrooms.Division(grade, 5))
    males = 0
    females = 0
    for student in grades[grade]:
        if student.gender == 'M':
            males += 1
        elif student.gender == 'F':
            females += 1

    if males+females != 0:
        chance_of_males = males/(males+females)
        chance_of_females = females/(males+females)
        # sorting students into classes based on chance
        for _ in range(len(grades[grade])):
            if random.randint(1, 100)/100 < chance_of_males:
                for _ in range(len(grades[grade])):
                    index = random.randint(0, len(grades[grade])-1)
                    if grades[grade][index].gender == 'M':
                        classrooms[counter].add_student(
                            grades[grade].pop(index))
                        break
                else:
                    pass
                    # add a female
            else:
                for _ in range(len(grades[grade])):
                    index = random.randint(0, len(grades[grade])-1)
                    if grades[grade][index].gender == 'F':
                        classrooms[counter].add_student(
                            grades[grade].pop(index))
                        break
                else:
                    pass
                # add a male

for classroom in classrooms:
    print(classroom)
