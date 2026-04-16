from django.urls import path
from . import views


urlpatterns = [
    path('',views.project_one,name='project_one'),
    path('project_two/',views.project_two,name='project_two'),
]
