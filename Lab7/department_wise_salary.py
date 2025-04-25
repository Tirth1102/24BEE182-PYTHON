employees = [
    {'dept_no': 10, 'emp_id': 1, 'salary': 25000},
    {'dept_no': 10, 'emp_id': 2, 'salary': 40000},
    {'dept_no': 20, 'emp_id': 3, 'salary': 30000},
    {'dept_no': 20, 'emp_id': 4, 'salary': 20000},
    {'dept_no': 30, 'emp_id': 5, 'salary': 50000}
]

dept_salaries = {}

for emp in employees:
    dept = emp['dept_no']
    salary = emp['salary']
    if dept not in dept_salaries:
        dept_salaries[dept] = {'min': salary, 'max': salary}
    else:
        dept_salaries[dept]['min'] = min(dept_salaries[dept]['min'], salary)
        dept_salaries[dept]['max'] = max(dept_salaries[dept]['max'], salary)

print("Department-wise Min and Max Salary:")
for dept, data in dept_salaries.items():
    print(f"Dept {dept}: Min Salary = {data['min']}, Max Salary = {data['max']}")

# Output:
# Department-wise Min and Max Salary:
# Dept 10: Min Salary = 25000, Max Salary = 40000
# Dept 20: Min Salary = 20000, Max Salary = 30000
# Dept 30: Min Salary = 50000, Max Salary = 50000