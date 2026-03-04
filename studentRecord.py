class StudentRecords:
        def  __init__(self):
            self.record = {}
        def add_student(self, student_id, name):
            self.record[student_id] = name
        def edit_student(self, student_id, name):
            if student_id in self.record:
                self.record[student_id]= name
            else:
                print("student not found")
        def add_grade(self, student_id):
            return self.record.get(student_id, "student not found")
        def display_all(self):
            for sid, name in self.record.items():
                print(f"ID {sid}, Name: {name}" )
        
sr= StudentRecords()
sr.add_student("P01", "john")
sr.display_all()
