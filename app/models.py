from django.db import models

# Create your models here.

class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=500)

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    date_of_joining = models.DateField(auto_now_add=True, blank=True)
    photo_filename = models.CharField(max_length=500, blank=True)