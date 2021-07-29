from rest_framework import viewsets

from saec.core.models import ComunicacaoAgendada
from saec.core.serializers import ComunicacaoAgendadaSerializer


class ComunicacaoAgendadaViewSet(viewsets.ModelViewSet):
    queryset = ComunicacaoAgendada.objects.all()
    serializer_class = ComunicacaoAgendadaSerializer
