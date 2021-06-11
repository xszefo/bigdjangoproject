from django.views import generic
from django.urls import reverse
from .forms import CustomUserForm

class Base(generic.TemplateView):
    template_name = 'core/base.html'

class SignUp(generic.CreateView):
    form_class = CustomUserForm
    template_name = 'registration/signup.html'
    success_url = '/login'
