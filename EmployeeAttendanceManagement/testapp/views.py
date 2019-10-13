from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView
from testapp.models import Contact,Employee,Attendance
from testapp.forms import EmployeeForm,AttendanceForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.
class Counter:
    count=1
    def increment(self):
        self.count=self.count+1
        return ' '

class index(TemplateView):
    template_name='testapp/index.html'

class contactus(CreateView):
    model=Contact
    template_name='testapp/contactus.html'
    fields=('name','email','contactno','message')

class about(TemplateView):
    template_name='testapp/about.html'

@method_decorator(login_required,name='dispatch')
class dashboard(TemplateView):
    template_name='testapp/dashboard.html'

@login_required
def addemployee(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            eid_value=form.cleaned_data['eid']
            gender_value=form.cleaned_data['gender']
            employee=Employee.objects.get(eid=eid_value)
            employee.gender=gender_value
            employee.save()
            return redirect('detailsemployee/')

    return render(request,'testapp/addemployee.html',{'form':form})

@login_required
def detailsemployee(request):
    emp_list=Employee.objects.all()
    counter=Counter()
    return render(request,'testapp/detailsemployee.html',{'emp_list':emp_list,'counter':counter})

@login_required
def deleteemployee(request,eid):
    employee=Employee.objects.get(eid=eid)
    employee.delete()
    return redirect('/detailsemployee')

@login_required
def updateemployee(request,eid):
    employee=Employee.objects.get(eid=eid)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/detailsemployee')

    return render(request,'testapp/updateemployee.html',{'employee':employee})

@login_required
def addattendance(request):
    form=AttendanceForm()
    emp_list=Employee.objects.all()
    if request.method=='POST':
        form=AttendanceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/detailsattendance')

    return render(request,'testapp/addattendance.html',{'form':form,'emp_list':emp_list})

@login_required
def detailsattendance(request):
    attendance_list=Attendance.objects.all()
    counter=Counter()
    return render(request,'testapp/detailsattendance.html',{'attendance_list':attendance_list,'counter':counter})

@login_required
def deleteattendance(request,id):
    attendance=Attendance.objects.get(id=id)
    attendance.delete()
    return redirect('/detailsattendance')

@method_decorator(login_required,name='dispatch')
class updateattendance(UpdateView):
    model=Attendance
    fields=('employee','attendancedate','in_time','out_time','description')
    template_name='testapp/updateattendance.html'


def passwordchange(request):
    form=PasswordChangeForm()
    if request.method=='POST':
        form=PasswordChangeForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                    u=User.objects.get(username__exact=username)
                    u.set_password(password)
                    u.save()
                    return render(request,'testapp/passwordchange.html',{'form':PasswordChangeForm(),'message':'Password change successfully!','class':'alert alert-success'})
            except:
                return render(request,'testapp/passwordchange.html',{'form':PasswordChangeForm(),'message':'Username Does not exist !','class':'alert alert-success'})
    return render(request,'testapp/passwordchange.html',{'form':form})
