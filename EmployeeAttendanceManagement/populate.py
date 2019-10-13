import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','EmployeeAttendanceManagement.settings')

import django
django.setup()

from testapp.models import Employee
from faker import Faker
fake=Faker()

def populate(n):
    for i in range(n):
        feid=fake.random_int(min=1,max=100)
        ffirst_name=fake.first_name()
        flast_name=fake.last_name()
        fsalary=fake.random_number(5)
        fgender=fake.random_choices(elements=('Male','Female'))[0]
        fcontactno=fake.random_number(10)
        femail=fake.email()
        fcountry=fake.country()
        fcity=fake.city()
        fpincode=fake.random_number(6)
        faddress=fake.address()
        emp_record=Employee.objects.get_or_create(eid=feid,first_name=ffirst_name,last_name=flast_name,salary=fsalary,gender=fgender,contactno=fcontactno,email=femail,country=fcountry,city=fcity,pincode=fpincode,address=faddress)

populate(10)
