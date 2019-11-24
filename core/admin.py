from django.contrib import admin
from .models import Instagram, Formulario, Banner

# Register your models here.

class InstagramAdmin(admin.ModelAdmin):
    list_display = ('nomeUsuario', 'telefone')

admin.site.register(Instagram, InstagramAdmin)
admin.site.register(Formulario)
admin.site.register(Banner)