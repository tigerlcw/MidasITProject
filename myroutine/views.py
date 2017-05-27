from django.shortcuts import render
from ohmyroutine.models import Routine
# Create your views here.
def index(request):
    routines = Routine.objects.filter(writer=request.user)
    context = {
    'routines' : routines,
    }
    return render(request, 'main/myroutine.html', context)
  