from django.db import models
from django.conf import settings
from django.db.models.deletion import SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Advisor(models.Model):
    name  = models.CharField(max_length=30,null=False,blank=False)
    photo = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class Call(models.Model):

    userid = models.ForeignKey(to=User,null=True,on_delete=SET_NULL)
    advid = models.ForeignKey(to=Advisor,null=True,on_delete=SET_NULL)
    time  = models.DateTimeField()












@receiver(post_save,sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
