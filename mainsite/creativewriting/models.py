from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
### The user is commented as we want to use django inbuilt user system
#class User(models.Model):
    #user_name = models.CharField(max_length=10)
    #email = models.EmailField(max_length=254,default = '')
    #password = models.CharField(max_length = 12,default = '')
    #num_articles = models.IntegerField(default=0)

    #def __str__(self):
        #return self.user_name


class Articles(models.Model):
    author = models.CharField(max_length = 50,default = "")
    title = models.CharField(max_length = 50,default = "")
    description = models.CharField(max_length = 200, default = 'NONE')
    content = models.TextField()
    likes = models.IntegerField(default = 0)
    datecreated = models.DateTimeField(auto_now_add = True)
    datemodified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


