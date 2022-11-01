from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class UserCreationView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html '
    success_url = reverse_lazy('accounts/login')
