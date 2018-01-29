from django.urls import path

from . import views


urlpatterns = [
    path('todo_list/', views.TodoListPageView.as_view(), name='todo_list'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
