students = []
courses = []
marks = {}


def input_students():
    number = int(input("Number of students: "))

    for i in range(number):
        print("\nStudent", i + 1)
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        student_dob = input("Date of birth: ")
        student = (student_id, student_name, student_dob)
        students.append(student)


def input_courses():
    number = int(input("\nNumber of courses: "))

    for i in range(number):
        print("\nCourse", i + 1)
        course_id = input("Course ID: ")
        course_name = input("Course name: ")
        course = (course_id, course_name)
        courses.append(course)


def list_courses():
    print("\nList of courses:")
    for course in courses:
        print(course[0], "-", course[1])


def list_students():
    print("\nList of students:")
    for student in students:
        print(student[0], "-", student[1], "-", student[2])


def course_exists(course_id):
    for course in courses:
        if course[0] == course_id:
            return True
    return False


def input_marks():
    list_courses()
    course_id = input("\nEnter course ID to input marks: ")

    if not course_exists(course_id):
        print("Course not found.")
        return

    marks[course_id] = {}

    for student in students:
        student_id = student[0]
        student_name = student[1]
        mark = float(input("Enter " + student_name + "'s mark: "))
        marks[course_id][student_id] = mark


def show_marks():
    list_courses()
    course_id = input("\nEnter course ID to show marks: ")

    if course_id not in marks:
        print("No marks found for this course.")
        return

    print("\nStudent marks:")
    for student in students:
        student_id = student[0]
        student_name = student[1]
        if student_id in marks[course_id]:
            print(student_id, "-", student_name, "-", marks[course_id][student_id])


def main():
    input_students()
    input_courses()

    list_students()
    list_courses()

    input_marks()
    show_marks()


if __name__ == "__main__":
    main()
