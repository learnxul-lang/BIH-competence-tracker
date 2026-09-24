from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('login/',include('users.urls', namespace='users')),
    path('register/', include('users.urls', namespace='users')),
    path('logout/',include('users.urls', namespace='users')),
    path('content_list/', include('learning.urls',namespace='learning')),
    path('task_list/', include('learning.urls',namespace='learning')),
    path('set_lab_estimate/', include('learning.urls',namespace='learning')),
    path('create_task/', include('learning.urls',namespace='learning')),
    path('update_progress/', include('learning.urls',namespace='learning')),
    path('add_comment/', include('learning.urls',namespace='learning')),
    path('participant/',include('dashboard.urls',namespace='dashboard')),
    path('admin_dashboard/',include('dashboard.urls',namespace='dashboard')),
    path('approve_participant/', include('dashboard.urls',namespace='dashboard')),
    path('admin_participant_detail', include('dashboard.urls',namespace='dashboard')),


]
