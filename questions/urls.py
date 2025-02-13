from django.urls import path

from . import views


app_name = 'questions'

urlpatterns = [
    path('list/', views.test_list, name='list'),
    path('create/', views.test_create, name='create'),
    path('delete/<int:pk>/', views.test_delete, name='delete'),
    path('edit/<int:pk>/', views.test_edit, name='edit'),

]