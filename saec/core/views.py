from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from saec.core.models import ComunicacaoAgendada
from saec.core.serializers import ComunicacaoAgendadaSerializer


class ComunicacaoAgendadaViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        # se for realmente necessário atualizar,
        # CANCELA (DELETE) e envia um nova!
        # mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):

    queryset = ComunicacaoAgendada.objects.all()
    serializer_class = ComunicacaoAgendadaSerializer

    def destroy(self, request, *args, **kwargs):
        if pk := kwargs.get('pk'):
            ag = ComunicacaoAgendada.objects.get(pk=pk)
            if ag.status == ComunicacaoAgendada.Status.AGENDADA:
                ag.status = ComunicacaoAgendada.Status.CANCELADA
                ag.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
