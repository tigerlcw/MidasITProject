from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from account.models import User

class Routine(models.Model):
    routine_id = models.AutoField(primary_key=True)
    routine_name = models.CharField(max_length=40)
    routine_detail = models.CharField(max_length=40)
    routine_time = models.CharField(max_length=20)
    write_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, null=True)
    def __str__(self):
        return '%s' % self.routine_name

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=40)
    exercise_movie = models.FileField(upload_to='uploads/')
    exercise_detail = models.CharField(max_length=200)
    def __str__(self):
        return '%s' % self.exercise_name

class ExerciseInRoutine(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    routine_name = models.ForeignKey(Routine, null=True)
    exercise_movie = models.ForeignKey(Exercise, null=True)
    exercise_count = models.CharField(max_length=20)
    add_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % self.routine_name
