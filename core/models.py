from django.db import models

# Create your models here.
class Instagram(models.Model):
    nomeUsuario = models.CharField('Nome de Usuário', max_length=255, null=False, blank=False)
    telefone = models.CharField('Telefone', max_length=20, blank=True)

    class Meta:
        ordering = ['nomeUsuario']
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagram'

        def __str__(self):
            return self.nomeUsuario

class Formulario(models.Model):
    titulo = models.CharField('Título', max_length=100, blank=False, null=False)
    texto = models.TextField('Descrição', null=True, blank=True)
    url = models.URLField('Link', max_length=1000)
    imagem = models.ImageField(upload_to='formulario/', verbose_name='Imagem')

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Formulário'
        verbose_name_plural = 'Formulários'

    def __str__(self):
        return self.titulo

class Banner(models.Model):
    titulo = models.CharField('Título', max_length=100, blank=False, null=False)
    imagem = models.ImageField(upload_to='banner/', verbose_name='Imagem')

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Imagem Banner'
        verbose_name_plural = 'Imagens Banner'

    def __str__(self):
        return self.titulo