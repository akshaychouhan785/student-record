from django.db import models


class Student(models.Model):
    stu_name=models.CharField(max_length=30)
    email=models.CharField(max_length=35)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=35)
    branch=models.CharField(max_length=20)
    year=models.IntegerField()
    semester=models.IntegerField()
    honors=models.BooleanField(default=False)
    
    def __str__(self):
    	return self.stu_name+" "+self.branch
