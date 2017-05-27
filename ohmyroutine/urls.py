from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^routine_detail/(?P<routineid>.+)/$', views.routine_detail),
    url(r'^timer/$', views.exercise_timer),
]