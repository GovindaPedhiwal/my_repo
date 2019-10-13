from django import forms
from testapp.models import Contact,Employee,Attendance

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)

class EmployeeForm(forms.Form,forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),initial='Male')
    class Meta:
        model=Employee
        fields=('eid','first_name','last_name','salary','gender','contactno','email','country','city','pincode','address')


class AttendanceForm(forms.ModelForm) :
    class Meta:
        model=Attendance
        fields='__all__'

class PasswordChangeForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
