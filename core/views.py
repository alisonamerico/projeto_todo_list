from django.views.generic import TemplateView, ListView
from . models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    model = Todo
    template_name = 'home.html'


class TodoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'


class TodoCreate(CreateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo_list')
    fields = ['title']


class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo_list')
    fields = ['title']


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo_list')
