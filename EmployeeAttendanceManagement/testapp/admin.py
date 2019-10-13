from django.contrib import admin
from testapp.models import Contact,Employee,Attendance

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','contactno','message']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','first_name','last_name','salary','gender','contactno','email','country','city','pincode','address']

class AttendanceAdmin(admin.ModelAdmin):
    list_display=['employee','attendancedate','in_time','out_time','description']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Attendance,AttendanceAdmin)
