from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('todo_list/', views.TodoListPageView.as_view(), name='todo_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('registration/login/', views.LoginPageView.as_view(), name='login'),
]
