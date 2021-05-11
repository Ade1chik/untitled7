from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import reverse


#Create your models here.
#class Homework(models.Model):
 #   homework=models.TextField()
  #  data_deposit=models.DateTimeField()
#    code_subject=models.IntegerField()
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100)

class Marks(models.Model):
    mark=models.IntegerField()
    data=models.DateTimeField()


class Pass(models.Model):
    data=models.DateTimeField()


class Schedule(models.Model):
    day=models.TextField()
    lesson_number=models.IntegerField()
    class_number=models.IntegerField()
    letter=models.TextField()
  #  schedule_homework=models.OneToOneField(Homework)


class Teachers(models.Model):
    code_teacher = models.IntegerField()
    surname = models.TextField()
    name = models.TextField()
    middle_name = models.TextField()
    teacher_schedule=models.ForeignKey('Schedule',on_delete=models.CASCADE)


class Pupil(models.Model):
    surname=models.TextField()
    name=models.TextField()
    middle_name=models.TextField()
    class_number=models.IntegerField()
    letter=models.TextField()
    pupil_marks = models.ForeignKey('Marks', on_delete=models.SET_NULL, null=True)
    pupil_pass = models.ForeignKey('Pass', on_delete=models.SET_NULL, null=True)


class Users(models.Model):
    type=models.TextField()
    password=models.CharField(max_length=50)
    login=models.TextField()
    code=models.OneToOneField('Pupil',on_delete=models.CASCADE)
    mod = models.OneToOneField('Teachers', on_delete=models.CASCADE)


class Subjects(models.Model):
    code_subject=models.IntegerField()
    name=models.TextField()
    subject_marks = models.ForeignKey('Marks', on_delete=models.SET_NULL, null=True)
    subject_schedule=models.ForeignKey('Schedule', on_delete=models.SET_NULL, null=True)
   # subject_homework = models.OneToOneField('Homework',on_delete=models.CASCADE)

class Subscriber(models.Model):
   email = models.EmailField()
   name = models.CharField(max_length=128)
   def __str__(self):
       return "Пользователь %s %s" % (self.name, self.email)


# class Homework(models.Model):
#     homework=models.TextField()
#     data_deposit=models.DateTimeField()
# #    code_subject=models.IntegerField()
#
# class Marks(models.Model):
#     mark=models.IntegerField()
#     data=models.DateTimeField()
#
# class Pass(models.Model):
#     data=models.DateTimeField()
#
# class Users(models.Model):
#     type=models.TextField()
#     pupils=models.TextField()
#     login=models.TextField()
#
# class Pupil(models.Model):
#     surname=models.TextField()
#     name=models.TextField()
#     middle_name=models.TextField()
#     clas=models.IntegerField()
#     letter=models.TextField()
#     code_children=models.OneToOneField(Users)



#class Houses(models.Model):
#    har = models.CharField(max_length=64)
#    http = models.URLField()
#    price = models.IntegerField()
#    image = models.URLField(default='https://img2.freepng.ru/20180520/qfl/kisspng-2d-computer-graphics-tile-based-video-game-buildin-5b02137bc384c6.3814977715268627158009.jpg', null=True, blank=True)
#    geo = models.CharField(max_length=64, default='Местоположение не указано')
 #   average_price = models.IntegerField(default='2500000')
 #   favourites = models.ManyToManyField(User)

#class Users(models.Model):
 #   email = models.EmailField()
  #  password = models.CharField(max_length=32)
  #  def __str__(self):
 #       return "Пользователь %s %s" % (self.email, self.password)
