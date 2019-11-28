from django.contrib import admin
from .models import NossosProgramasModel, SobreNosModel
from solo.admin import SingletonModelAdmin

# Register your models here.

class NossosProgramasModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(NossosProgramasModel, NossosProgramasModelAdmin)
admin.site.register(SobreNosModel, SingletonModelAdmin)