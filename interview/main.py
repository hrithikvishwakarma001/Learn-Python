employees = [
{"name":"John","Salary":3000,"designation":"developer"},
{"name":"Emma","Salary":4000,"designation":"manager"},
{"name":"Kelly","Salary":3500,"designation":"tester"}
]

def max_salary_employee(employees):
    max_salary = 0
    max_employee={}
    for x in employees:
     if x["Salary"]>max_salary:
        max_salary = x["Salary"]
        max_employee = x
    return max_employee


print(max_salary_employee(employees))