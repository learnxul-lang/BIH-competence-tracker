from django.urls import path
from . import views

app_name = 'learning'

urlpatterns = [
    path('learning/content_list/', views.content_view, name='content_list'),
    path('learning/task_list/', views.task_view, name='task_list'),
    path('learning/set_lab_estimate/', views.set_lab_estimate_view, name='set_lab_estimate'),
    path('learning/create_task/', views.create_task_view, name='create_task'),
    path('learning/update_progress/', views.update_progress_view, name='update_progress'),
    path('learning/add_comment/', views.add_comment_view, name='add_comment'),

]