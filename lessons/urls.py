from django.urls import path

from . import views


app_name = 'lessons'

urlpatterns = [
    path('list/', views.lesson_list, name='list'),
    path('create/', views.lesson_create, name='create'),
    path('detail/<int:pk>/', views.lesson_view, name='detail'),
    path('edit/<int:pk>/', views.lesson_edit, name='edit'),
    path('edit/<int:pk>/', views.lesson_edit, name='edit'),
    path('delete/<int:pk>/', views.lesson_delete, name='delete'),
]