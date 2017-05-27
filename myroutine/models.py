from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from account.models import User
from ohmyroutine.models import Routine

class Calender(models.Model):
    activist = models.ForeignKey(User, null=True)
    routine_name = models.ForeignKey(Routine, null=True)
    active_time = models.IntegerField()
    active_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % self.activist