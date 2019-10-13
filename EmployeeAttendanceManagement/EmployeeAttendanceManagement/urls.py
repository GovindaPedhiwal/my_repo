"""EmployeeAttendanceManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index.as_view()),
    path('contactus/',views.contactus.as_view(),name='contactus'),
    path('about/',views.about.as_view()),
    path('dashboard/',views.dashboard.as_view()),
    path('accounts/',include('django.contrib.auth.urls')),
    path('addemployee/',views.addemployee),
    path('detailsemployee/',views.detailsemployee),
    path('deleteemployee/<int:eid>',views.deleteemployee),
    path('updateemployee/<int:eid>',views.updateemployee),
    path('addattendance/',views.addattendance),
    path('detailsattendance/',views.detailsattendance,name='detailsattendance'),
    path('deleteattendance/<int:id>',views.deleteattendance),
    path('updateattendance/<int:pk>',views.updateattendance.as_view()),
    path('passwordchange/',views.passwordchange)
]
