class EmployeePayroll:
    def __init__(self):
        self.employees = {}
    def add_employee(self, employeeID,name, position, salary):
        self.employees[employeeID] = {"name": name, "position": position, "salary": salary}
    def update_salary(self, employeeID, new_salary):
        if employeeID in self.employees:
            self.employees[employeeID]["salary"] = new_salary
    def calculate_total_payroll(self):
        return sum(emp['salary'] for emp in self.employees.values())
    def display(self):
        for emp, info in self.employees.items():
            print(f"EMP_ID: {emp}, Name: {info['name']}, Position: {info['position']}, Salary: {info['salary']} ")
empl = EmployeePayroll()
empl.add_employee("E001","JOHN", "PROGRAMMER", 20000)
empl.update_salary("E001", 25000)
empl.add_employee("E002","JOY", "HR", 15000)
empl.display()
print("Total Payroll:", empl.calculate_total_payroll())



