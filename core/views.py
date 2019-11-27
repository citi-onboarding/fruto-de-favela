from django.shortcuts import render
from django.views import generic
from .models import Banner, Formulario, Instagram

# Create your views here.

class HomeViews(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Banner'] = Banner.objects.all()
        context['Formulario'] = Formulario.objects.all()
        context['Instagram'] = Instagram.objects.all()
        return context
        