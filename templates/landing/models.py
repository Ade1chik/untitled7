from django.db import models


class Subscribers(models.Model):
    email= models.EmailFieled()
    name= models.CharField(max_lenght=128)