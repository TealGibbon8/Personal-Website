from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('copyright/', views.copyright, name='copyright'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project, name='project'),
    path('projects/add/', views.add_project, name='add_project'),
    path('login/', views.user_login, name='login')
]