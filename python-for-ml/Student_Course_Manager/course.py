class Course:
   
    _id_counter = 1
   
    def __init__(self, name):
        self.course_id = Course._id_counter
        Course._id_counter += 1
        self.name = name
        self.enrolled_students = []

    def __repr__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Enrolled Students: {[len(self.enrolled_students)]}"
    
    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.enroll_student(self)
            print("Student enrolled successfully")
        else:
            print("Student is already enrolled in this course")
            
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.enrolled_courses.remove(self)
            print("Student removed successfully")
        else:
            print("Student is not enrolled in this course")