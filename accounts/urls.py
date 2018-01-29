from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_reset_form/', views.PasswordResetForm.as_view(), name='password_reset'),
    path(
        'password_reset_done/', views.PasswordResetForm.as_view(), name='password_reset_done'
        ),
    path(
        'password_reset_confirm/',
        views.PasswordResetConfirm.as_view(), name='password_reset_confirm'
        ),
]
