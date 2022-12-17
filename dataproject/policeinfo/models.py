from django.db import models
from django.contrib import admin
class Police(models.Model):
    policeid = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    email = models.EmailField()
# Create your models here.
class PoliceAdmin(admin.ModelAdmin):
    list_display = ('policeid','name','age','salary','email')
