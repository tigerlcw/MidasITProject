from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^meal_detail/(?P<pk>.+)/$', views.routine_detail, name='detail'),
    url(r'^comment_add/(?P<pk>.+)/$', views.comment_add),
    url(r'^meal_check/(?P<pk>.+)/$', views.meal_check),
    url(r'^meal_check_not/(?P<pk>.+)/$', views.meal_check_not),
    url(r'^meal_like/(?P<pk>.+)/$', views.meal_like),
    url(r'^meal_like_not/(?P<pk>.+)/$', views.meal_like_not),
    url(r'^timer/$', views.exercise_timer),
    url(r'^search/$', views.search),
    url(r'^routine/$', views.chart),
    url(r'^excel/$',views.ExcelUploadFormView.as_view()),
    url(r'^today/$', views.today),
    url(r'^group/$', views.group, name='group'),
    url(r'^group/create/$', views.group_create, name='group_create'),
    url(r'^group/(?P<pk>.+)/$', views.group_join, name='group_join')
    ]
