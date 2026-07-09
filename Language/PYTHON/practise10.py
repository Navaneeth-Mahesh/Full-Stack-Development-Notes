gender = input("Enter the sex of employee (M or F) : ")
salary = int(input("Enter the salary of the employee : "))
if (gender == 'M'):
    bonus = 0.10 * salary
else:
    bonus = 0.5 * salary
amount_to_be_paid = salary + bonus
print("Salary = ", salary)
print("Bonus = ", bonus)
print("********************")

print("Amount to be paid : ", amount_to_be_paid)
