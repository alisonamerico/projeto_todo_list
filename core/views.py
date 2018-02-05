from django.views.generic import TemplateView, ListView
from . models import Todo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


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
    fields = ['title', 'deadline', 'priority']


class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo_list')
    fields = ['title', 'deadline', 'priority', 'completed']


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo_list')


class GeneratePDF(TemplateView):

    def some_view(request):
        # Create the HttpResponse object with the appropriate PDF headers.
        if 'pdf' in request.POST:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

            buffer = BytesIO()

            # Create the PDF object, using the BytesIO object as its "file."
            p = canvas.Canvas(buffer)

            # Draw things on the PDF. Here's where the PDF generation happens.
            # See the ReportLab documentation for the full list of functionality.
            p.drawString(100, 100, "Hello world.")

            # Close the PDF object cleanly.
            p.showPage()
            p.save()

            # Get the value of the BytesIO buffer and write it to the response.
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
