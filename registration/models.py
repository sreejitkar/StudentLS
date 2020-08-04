from django.db import models
SEX_CHOICES =( 
    ("M", "Male"), 
    ("F", "Female"), 
    ("O","Other")
) 
# Create your models here
class Classroom(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.c_name)

class Student(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=100)
    s_class=models.ForeignKey(Classroom,on_delete=models.CASCADE,default=None)
    s_sex=models.CharField(choices=SEX_CHOICES,max_length=3)
    s_att=models.FloatField(default=0)
    def __str__(self):
        return str(self.s_name)

class Subjects(models.Model):
    sub_id=models.AutoField(primary_key=True)
    sub_name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.sub_name)  

class SubToClassMap(models.Model):
    map_id=models.AutoField(primary_key=True)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE,default=None)
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE,default=None)

class SubtoStudentMap(models.Model):
    att_id=models.AutoField(primary_key=True)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE,default=None)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
    att_value=models.FloatField(default=0.0)
    total_score=models.FloatField(default=0.0)
    end_sem_score=models.FloatField(default=0.0)
    mid_sem_score=models.FloatField(default=0.0)
    cia1_score=models.FloatField(default=0.0)
    cia2_score=models.FloatField(default=0.0)
    cia3_score=models.FloatField(default=0.0)
    
    def __str__(self):
        return str(self.att_id)
        