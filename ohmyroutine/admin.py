from django.contrib import admin
from .models import Routine, Exercise, ExerciseInRoutine

admin.site.register(Routine)
admin.site.register(Exercise)
admin.site.register(ExerciseInRoutine)