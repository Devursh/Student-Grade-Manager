import re

students = {}

with open("students.txt") as file:
    file_content = file.read()
    if not(len(file_content) < 1):
        file_content_lines = file_content.split("\n")
        for line in file_content_lines:
            name = line.split(":")[0]
            grades = (line.split(":")[1].split(","))
            new_grade_list = []
            for index, grade in enumerate(grades):
                grade = int(grades[index])
                new_grade_list.append(grade)
            students[name] = new_grade_list

def add_student(student):
    if not(student in students):
        students[student] = []
    else:
        print(student, " is already a student")

def remove_student(student):
    if student in students:
        students.pop(student, "None")
    else:
        print("There is no one named ", student, " in the dictionary.")

def add_grades(student, grades):
    if student in students:
        students[student].extend(grades)
    else:
        print("No student named ", student, " in the list", "\n")

def view_student(student):
    if student in students and len(students[student]) > 0:
        return students[student]
    elif student in students and len(students[student]) <= 0:
        print("The student ", student, " has no grades.")
    else:
        print("No student named ", student, " in the list", "\n")

def view_all():
    return students

def average_grade(student):
    if student in students and len(students[student]) > 0:
        print("The average grade of "+student+" is "+str(sum(students[student]) / len(students[student])))
    elif student in students and len(students[student]) <= 0:
        print(student + " does not have any grades.")
    else:
        print("No such student named "+student+"\n")

def highest_average():
    #find the average of each student, compare to find highest
    average_grades = []
    for student in students:
        average_grades.append(sum(students[student]) / len(students[student]))
    return max(average_grades)

def menu():
    condition_is_met = False
    while condition_is_met == False:
        menu_options = input("What would you like to do?\n1. Add students\n2. Remove students\n3. Add grades to students\n4. View grades of students\n5. View all students\n6. Calculate averages\n7. Find highest grade\n8. Exit the program\n")
        try:
            menu_int_value = int(menu_options)
            if not(9 > menu_int_value > 0):
                print("The value is not a integer between 1-8.")
                continue
            else:
                condition_is_met = True
                return menu_int_value          
        except:
            print("The value has to be an integer between 1-8.")
            continue

def get_student_name():
    student_name = input("What is the student's name?\n")
    return student_name

menu_int_value = menu()

exit = False

while exit == False:
    if menu_int_value == 1: #add a student by asking the students name and using the add_student() function
        name = get_student_name()
        add_student(name)
        menu_int_value = menu()
    elif menu_int_value == 2:
        name = get_student_name()
        remove_student(name)
        menu_int_value = menu()
    elif menu_int_value == 3: #add grades to a student by asking the students name
        name = get_student_name()
        student_grades = input("What is the student's grades?\n").split(",")
        for index, grade in enumerate(student_grades):
            student_grades[index] = int(grade)
        add_grades(name, student_grades)
        menu_int_value = menu()
    elif menu_int_value == 4: #view the grade of a student by asking the student name and then checking the students dict
        name = get_student_name()
        if view_student(name):
            print("The grades of ", name, " are: ", view_student(name), "\n")
        menu_int_value = menu()
    elif menu_int_value == 5: #view all of the students
        print(students)
        menu_int_value = menu()
    elif menu_int_value == 6: #calculate the averages of a student
        name = get_student_name()
        average = average_grade(name)
        menu_int_value = menu()
    elif menu_int_value == 7: #find the highest grade
        print(highest_average())
        menu_int_value = menu()
    elif menu_int_value == 8:
        with open("students.txt", "w") as file:
            for student in students:
                student_name = str(student)
                student_grades_packed = students[student]
                student_grades_unpacked = str()
                for index, value in enumerate(student_grades_packed):
                    if index != len(student_grades_packed) - 1: 
                        student_grades_unpacked = student_grades_unpacked + str(value) + ","
                    else:
                        student_grades_unpacked = student_grades_unpacked + str(value)
                file.write(str(student_name + ":" + student_grades_unpacked + "\n"))
        exit = True