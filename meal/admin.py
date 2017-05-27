from django.contrib import admin
from .models import Meal, MealCheck, MealLike, Comment


admin.site.register(Meal)
admin.site.register(MealCheck)
admin.site.register(MealLike)
admin.site.register(Comment)
