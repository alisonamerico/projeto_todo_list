from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.views.generic import TemplateView
from . models import Todo


class HomePageView(TemplateView):
    model = Todo
    template_name = 'home.html'


class TodoListPageView(TemplateView):
    model = Todo
    template_name = 'todo_list.html'


class LoginPageView(TemplateView):
    model = Todo
    template_name = 'login.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
