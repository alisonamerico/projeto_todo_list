from django.urls import path

from . import views


urlpatterns = [
    path('todo/todo_list/', views.TodoList.as_view(), name='todo_list'),
    path('new', views.TodoCreate.as_view(), name='todo_new'),
    path('edit/<int:pk>/', views.TodoUpdate.as_view(), name='todo_edit'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='todo_delete'),
]
