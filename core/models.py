from django.db import models
from solo.models import SingletonModel

# Create your models here.
class NossosProgramasModel(models.Model):
    titulo = models.CharField('Título', max_length=100, blank=False, null=False)
    descricao = models.TextField('Descrição', blank=False, null=False)
    imagem = models.ImageField(upload_to='nossosProgramas/', verbose_name='Imagem')

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Nossos Programas'
        verbose_name_plural = 'Nossos Programas'

    def __str__(self):
        return self.titulo

class SobreNosModel(SingletonModel):
    quemSomos = models.TextField('Quem Somos?', blank=False, null=False)
    acolher = models.TextField('Acolher', blank=False, null=False)
    desenvolver = models.TextField('Desenvolver', blank=False, null=False)
    encaminhar = models.TextField('Encaminhar', blank=False, null=False)

    class Meta:
        verbose_name = 'Sobre Nós'

    def __str__(self):
        return "Sobre Nós"

class BannerModel(SingletonModel):
    imagemBanner = models.ImageField(upload_to='banner/', verbose_name='Banner')

    class Meta:
        verbose_name = 'Banner'

    def __str__(self):
        return "Banner"