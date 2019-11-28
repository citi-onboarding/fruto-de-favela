from django.contrib import admin
from .models import NossosProgramasModel

# Register your models here.

class NossosProgramasModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(NossosProgramasModel, NossosProgramasModelAdmin)
