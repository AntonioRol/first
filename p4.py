def pay_raise(current_salary;
    new_salary = 0
    if current_salary < 200000:
        new_salary = current_salary * 1.10
    else:
        new_salary = current_salary * 1.07
    return new_salary

pete_salary = 19000
bob_salary = 40000

print 'new2 pete salary -', pay_raise(pete_salary)
print 'new bob salary - ', pay_raise(bob_salary)

