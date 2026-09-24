from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/participant/', views.participant_view, name='participant'),
    path('dashboard/admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('dashboard/approve_participant/', views.approve_participant_view, name='approve_participant'),
    path('dashboard/admin_participant_detail/', views.admin_participant_detail_view, name='admin_participant_detail'),

]