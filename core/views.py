from django.shortcuts import render
from django.views import generic
from .models import NossosProgramasModel, SobreNosModel

# Create your views here.

class HomeViews(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nossosProgramas"] = NossosProgramasModel.objects.all()
        context["sobreNos"] = SobreNosModel.objects.first()
        return context
        