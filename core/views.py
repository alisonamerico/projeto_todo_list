from django.views.generic import TemplateView, ListView

from . models import Todo


class HomePageView(TemplateView):
    model = Todo
    template_name = 'home.html'


class TodoListPageView(ListView):
    model = Todo
    template_name = 'todo_list.html'
