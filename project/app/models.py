from django.db import models
class Aadhar(models.Model):
    aadhar_no=models.IntegerField(unique=True)
    created_data=models.DateTimeField()
    created_by=models.CharField(max_length=40)
    def __str__(self):
        return str(self.aadhar_no)
    

class Student(models.Model):
    stu_name=models.CharField(max_length=40)
    stu_city=models.CharField(max_length=40)
    stu_email=models.EmailField()
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)    