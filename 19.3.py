import Employee
import os 
from datetime import datetime
from time import strftime
environment_items = dict(**os.environ)
print (environment_items['HOMEDRIVE'] + environment_items['HOMEPATH'])
now = datetime.now()
print (f"Lab 19.3: {now.strftime('%x %H:%M:%S')}")
print()

def main():
    name = input('Enter the name: ')
    number = input('Enter the ID number: ')
    salary = float(input('Enter the annual salary: '))
    bonus = float(input('Eenter the bonus: '))

    emp = Employee.Shiftsupervisor(name, number, salary, bonus)

    print('Shift Supervisor worker information:')
    print('Name:', emp.get_name())
    print('ID number', emp.get_number())
    print('Annual Salary: $', \
        format(emp.get_annual_salary(), ',.2f'),\
        sep='')
    print('Annual Bonus: $', \
        format(emp.get_annual_bonus(), ',.2f'), \
        sep='')

main()