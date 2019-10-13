from django.db import models
from django.urls import reverse

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    contactno=models.CharField(max_length=10)
    message=models.TextField()

    def get_absolute_url(self):
        return reverse('contactus')

class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    salary=models.IntegerField()
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,default=1)
    contactno=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    pincode=models.IntegerField()
    address=models.CharField(max_length=60)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Attendance(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,default=1)
    attendancedate=models.DateField()
    in_time=models.TimeField()
    out_time=models.TimeField()
    description=models.TextField()

    def get_absolute_url(self):
        return reverse('detailsattendance')
