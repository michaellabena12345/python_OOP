class StudentGradesSystem:
    def __init__(self):
        self._students = {}

    def add_grade(self, name, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        if name not in self._students:
            self._students[name] = []

        self._students[name].append(grade)

    def average(self, name):
        if name not in self._students:
            raise ValueError("Student not found")

        grades = self._students[name]

        if not grades:
            return 0.0

        return sum(grades) / len(grades)

    def display_all(self):
        for name, grades in self._students.items():
            avg = self.average(name)
            print(f"Student: {name}")
            print(f"Grades: {grades}")
            print(f"Average: {avg}")
            
system = StudentGradesSystem()
system.add_grade("Rhav", 70)
system.add_grade("Val", 75)
system.display_all()
