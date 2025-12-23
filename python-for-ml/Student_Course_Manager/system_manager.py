class system_manager:
    
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def add_student(self, name):
        student = Student(name)
        self.students[student.student_id] = student
        print("Student added successfully")
        return student.student_id
    
    def remove_student(self, student_id):
        if student_id in self.students:
            Student = self.students[student_id]
            if not Student.enrolled_courses:
                del self.students[student_id]
                print("Student removed")
            else:
                print("Student had enrolled courses. Cannot remove.")
        else:
            print("Invalid student ID.")
    
    def add_course(self, name):
        course = Course(name)
        self.courses[course.course_id] = course
        print("Course added successfully")
        return course.course_id
    
    def remove_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            if not course.enrolled_students:
                del self.courses[course_id]
                print("Course removed")
            else:
                print("Course has enrolled students. Cannot remove.")
        else:
            print("Invalid course ID.")