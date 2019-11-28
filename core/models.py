from django.db import models

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