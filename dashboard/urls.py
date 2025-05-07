from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView 

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # Show login at root
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/new/', views.project_create, name='project_create'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
