gross_salary = float(input("Enter Gross Salary: "))

allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary

net_salary = gross_salary + allowance - deduction

print("Net Salary:", net_salary)

# Output:
# Enter Gross Salary: 10000
# Net Salary: 10700.0