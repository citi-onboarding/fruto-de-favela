from django.contrib import admin
from .models import NossosProgramasModel, SobreNosModel, BannerModel, ParceirosModel, BannerContatoModel
from solo.admin import SingletonModelAdmin

# Register your models here.

class NossosProgramasModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(NossosProgramasModel, NossosProgramasModelAdmin)
admin.site.register(ParceirosModel)
admin.site.register(SobreNosModel, SingletonModelAdmin)
admin.site.register(BannerModel, SingletonModelAdmin)
admin.site.register(BannerContatoModel, SingletonModelAdmin)