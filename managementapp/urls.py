from django.urls import path
from . import views
app_name='managementapp'
urlpatterns=[
    path('project/',views.project,name='project'),
    path('project_list/',views.project_list,name='project_list'),
    path('enter_new_task/',views.enter_new_task,name='enter_new_task'),
    path('tasks/', views.task_list, name='task_list'),
    
]