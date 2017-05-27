from django.shortcuts import render
from .models import Routine, Exercise, ExerciseInRoutine
from account.models import User
def index(request):
    routines = Routine.objects.all()
    context = {
        'routines': routines
    }
    return render(request, 'main/index.html', context)

def  routine_detail(request, routineid):
    routine = Routine.objects.get(routine_id=routineid)
    exercises = ExerciseInRoutine.objects.filter(routine_name=routine)
    context = {
        'routine' : routine,
        'exercises' : exercises
    }
    print (routine)
    return render(request, 'main/routine_detail.html', context)

def exercise_timer(request):
    return render(request, 'main/exercise_timer.html')
  