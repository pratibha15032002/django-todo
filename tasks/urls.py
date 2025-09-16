from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.task_create, name='create'),
    path('edit/<int:pk>/', views.task_update, name='edit'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
    path('toggle/<int:pk>/', views.task_toggle, name='toggle'),

    # auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
