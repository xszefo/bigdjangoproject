from django.views import generic
# Create your views here.

class Base(generic.TemplateView):
    template_name = 'core/base.html'