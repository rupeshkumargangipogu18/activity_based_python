# Employee Payroll and Deduction Analysis
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime amount: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

gross = basic + allowances + overtime + incentives

if gross <= 15000:
    tax = gross * 0.05
elif gross <= 30000:
    tax = (15000 * 0.05) + ((gross - 15000) * 0.10)
else:
    tax = (15000 * 0.05) + (15000 * 0.10) + ((gross - 30000) * 0.15)

pf = basic * 0.12

total_deductions = tax + pf
net_salary = gross - total_deductions

print("\n===== SALARY STATEMENT =====")
print("Employee Name:", name)
print("Basic Salary: Rs.", basic)
print("Allowances: Rs.", allowances)
print("Overtime: Rs.", overtime)
print("Incentives: Rs.", incentives)
print("Gross Salary: Rs.", round(gross, 2))
print("Tax Deduction: Rs.", round(tax, 2))
print("PF Deduction: Rs.", round(pf, 2))
print("Total Deductions: Rs.", round(total_deductions, 2))
print("Net Salary: Rs.", round(net_salary, 2))