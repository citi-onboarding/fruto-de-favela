from django.shortcuts import render
from django.views import generic
from .models import NossosProgramasModel, SobreNosModel, BannerModel, ParceirosModel, BannerContatoModel
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.

class HomeViews(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nossosProgramas"] = NossosProgramasModel.objects.all()
        context["parceiros"] = ParceirosModel.objects.all()
        context["sobreNos"] = SobreNosModel.objects.first()
        context["banner"] = BannerModel.objects.first()
        context["contatos"] = BannerContatoModel.objects.first()
        return context

def index(request):
    return render(request, 'home.html')

def email(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    assunto = request.POST.get('assunto')
    mensagem = request.POST.get('mensagem')

    subject = assunto
    body = f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}'
    mail = EmailMessage(subject, body, 'frutodefavela.citi@gmail.com', ['frutodefavela.citi@gmail.com', 'alysonrenan99@gmail.com'])
    result = mail.send()