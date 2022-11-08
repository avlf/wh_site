from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, SignUpForm


class SignUpView(generic.View):
    form_class = SignUpForm
    template_name = 'registration/login.html '
    success_url = 'main'


class UserCreationView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html '
    success_url = reverse_lazy('wh_info:signup')
