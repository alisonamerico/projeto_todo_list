from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PasswordResetForm(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'password_reset_form.html'


class PasswordResetConfirm(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('password_reset_confirm')
    template_name = 'password_reset_done.html'
