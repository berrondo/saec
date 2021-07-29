from django.core.validators import EmailValidator
from django.utils import timezone
from rest_framework import serializers

from saec.core.models import ComunicacaoAgendada


class ComunicacaoAgendadaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'data', 'mensagem', 'via', 'para', 'status')
        read_only_fields = ('status', )
        model = ComunicacaoAgendada

    def validate_data(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("A data de agendamento precisa ser futura!")
        return value

    def validate(self, data):
        para = data.get('para')
        via = data.get('via')

        if para and via:
            if via == 'email':
                try:
                    EmailValidator(message="Endereço de email inválido")(para)
                except:
                    raise

            if via in ('sms', 'whatsapp'):
                try:
                    int(para)
                except:
                    raise serializers.ValidationError("Telefone deve ser apenas números")
        return data
