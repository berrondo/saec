from rest_framework import routers

from saec.core.views import ComunicacaoAgendadaViewSet

router = routers.DefaultRouter()
router.register(r'agendamento', ComunicacaoAgendadaViewSet)