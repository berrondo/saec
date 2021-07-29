from rest_framework import serializers

from saec.core.models import ComunicacaoAgendada


class ComunicacaoAgendadaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'data', 'mensagem', 'via', 'para', 'status')
        read_only_fields = ('status', )
        model = ComunicacaoAgendada
