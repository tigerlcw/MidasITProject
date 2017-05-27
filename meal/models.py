from django.db import models

from account.models import User


class Meal(models.Model):
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    menu = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meal', default='default.jpg')

    def __str__(self):

        return self.date + '-' + self.time


class MealCheck(models.Model):
    user = models.ForeignKey(User, null=True)
    meal = models.ForeignKey(Meal, null=True)

    def __str__(self):

        return '{0}, {1}'.format(self.meal, self.user)


class Comment(models.Model):
    user = models.ForeignKey(User, null=True)
    meal = models.ForeignKey(Meal, null=True)
    comment = models.TextField()

    def __str__(self):

        return '{0}, {1}'.format(self.meal, self.user)


class MealLike(models.Model):
    user = models.ForeignKey(User, null=True)
    meal = models.ForeignKey(Meal, null=True)

    def __str__(self):

        return '{0}, {1}'.format(self.meal, self.user)
