from django.db import models

# Create your models here.


class Class( models.Model ):
    class_code = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=5)
    class_Teacher = models.CharField(max_length=20, null=True, blank=True) # This Will be update when Teachers Tables are created

    def __str__(self):
        return self.class_code+', '+self.class_name+', '+self.section


class Student(models.Model):
    Roll_Num = models.CharField(max_length=20,unique=True)
    Name = models.CharField(max_length=150)
    Address = models.CharField(max_length=200,default='')
    class_code = models.ForeignKey(Class, on_delete=models.CASCADE)
    parent_code = models.CharField(max_length=20)

    def __str__ (self):
        return self.Roll_Num+', '+self.Name


class Subjects(models.Model):
    subject_code = models.CharField(max_length=20,unique=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.subject_code+', '+self.subject_name


class SubjectEnroll(models.Model):
    Roll_Num = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_code = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.Roll_Num+', '+self.subject_code


class Parents(models.Model):
    Roll_Num = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact =  models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=(('m','Male'), ('f', 'Female')), blank=True, null=True)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.Roll_Num+', '+self.name+', '+self.relation+', '+self.gender

