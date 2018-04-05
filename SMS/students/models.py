from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=20, primary_key=True)
    class_details = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.class_name+': '+str(self.class_details)


class Section(models.Model):
    class_code = models.CharField(max_length=20, primary_key=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.CharField(max_length=5)
    class_Teacher = models.CharField(max_length=20, null=True, blank=True)  # This Will be update when Teachers Tables are created

    def __str__(self):
        return 'Class code : '+self.class_code


class Student(models.Model):
    Roll_Num = models.CharField(max_length=20,primary_key=True)
    Name = models.CharField(max_length=150)
    Address = models.CharField(max_length=200,default='')
    class_code = models.ForeignKey(Section,  on_delete=models.CASCADE)
    #parent_code = models.CharField(max_length=20)

    def __str__(self):
        return self.Roll_Num+', '+self.Name


class Subjects(models.Model):
    subject_code = models.CharField(max_length=20, primary_key=True)
    class_name = models.ForeignKey(Class, db_column='class_name', on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.subject_code+', '+self.subject_name


class SubjectEnroll(models.Model):
    Roll_Num = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def validate_subject_class(self):

        if SubjectEnroll.objects.filter(Roll_Num=self.Roll_Num, subject_code=self.subject_code).exists():
            raise ValidationError('This Course Is Already Enrolled')

    def save(self, *args, **kwargs):
        self.validate_subject_class()
        super(SubjectEnroll, self).save(*args, **kwargs)
    '''
    def validate_subject_class(self):
        student = Student.objects.get(Roll_Num=self.Roll_Num)
        sec = Section.objects.filter(class_code=str(student.class_code))
        if Subjects.objects.filter(subject_code=self.subject_code, class_name=sec.class_name).exists():
            raise ValidationError('Invalid Assignment Please check course and student class')

    def save(self, *args, **kwargs):
        self.validate_subject_class()
        super(SubjectEnroll, self).save(*args, **kwargs)
    '''

    def __str__(self):
        return str(self.Roll_Num)+', '+str(self.subject_code)


class Parents(models.Model):
    Roll_Num = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact =  models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=(('m','Male'), ('f', 'Female')), blank=True, null=True)
    relation = models.CharField(max_length=50)

    def __str__(self):
        return self.name+', '+self.relation+', '+self.gender

