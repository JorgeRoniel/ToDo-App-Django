from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasksList),
    path('task/<int:id>/', views.taskView),
    path('newtask/', views.newTask),
    path('edit/<int:id>/', views.editTask),
    path('status/<int:id>/', views.change_status),
    path('delete/<int:id>/', views.deleteTask),
]