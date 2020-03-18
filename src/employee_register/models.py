from django.db import models


#Postion Model
class Position(models.Model):
    title = models.CharField(max_length = 50)

#Employee Model
class Employee(models.Model):
    Fullname = models.CharField(max_length = 100 )
    emp_code = models.CharField(max_length = 3 )
    Mobile = models.CharField(max_length = 15 )
    Position = models.ForeignKey(Position , on_delete = models.CASCADE)
