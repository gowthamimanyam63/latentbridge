from django.db import models

# Create your models here.
class Class(models.Model):
    Cname=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.Cname
    
class Subject(models.Model):
    subname=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.subname
     
class Student_details(models.Model):
    id=models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=60)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    class_id=models.OneToOneField(Class,on_delete=models.CASCADE)

class Student_subjects(models.Model):
    id=models.IntegerField(primary_key=True)
    student_id=models.ForeignKey(Student_details,on_delete=models.CASCADE)
    subject_id=models.OneToOneField(Subject,on_delete=models.CASCADE)