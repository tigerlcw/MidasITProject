from django.db import models
from django.core.urlresolvers import reverse

from account.models import User


class Meal(models.Model):
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    menu = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meal', default='default.jpg')
    kcal = models.IntegerField(default=100)
    favor = models.IntegerField(default=0)
    check = models.BooleanField(default=False)

    def __str__(self):

        return self.date + '-' + self.time

    def get_absolute_url(self):

        return reverse('meal:detail', args=(self.pk,))

    def get_full_url(self):

        return 'http://127.0.0.1:8000' + self.get_absolute_url()

    def get_facebook_url(self):

        return 'https://www.facebook.com/sharer/sharer.php?u=' + self.get_full_url()

    def get_twitter_url(self):

        return 'https://twitter.com/intent/tweet?url=' + self.get_full_url() + '&text=hi'


class MealCheck(models.Model):
    user = models.ForeignKey(User, null=True)
    meal = models.ForeignKey(Meal, null=True)
    meal_date = models.CharField(max_length=100, default="2017-01-01")
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


class HonbabGroup(models.Model):
    user = models.ForeignKey(User, null=True)
    meal = models.ForeignKey(Meal, null=True)
    title = models.CharField(max_length=100)
    limit = models.IntegerField(default=1)

    def __str__(self):

        return self.title
class GroupJoin(models.Model):
    group = models.ForeignKey(HonbabGroup, null=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):

        return self.group

class Food(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):

        return self.name