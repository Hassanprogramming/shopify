from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    writer = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='static/images')
    
    def __str__(self):
        return self.first_name


class Blogs(models.Model):
    name = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    min_tilte = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='static/images')
    text = models.CharField(max_length=200, null=True)
    favorite = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return str(self.name)

class New(models.Model):
    name = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.CharField(max_length=300, null=True)
    preview = models.CharField(max_length=400, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return str(self.name)