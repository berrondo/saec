from django.contrib import admin

from saec.core.models import ComunicacaoAgendada


@admin.register(ComunicacaoAgendada)
class ComunicacaoAgendadaAdmin(admin.ModelAdmin):
    fields = ('data', 'mensagem', 'para', 'via', 'status')
    list_display = fields
