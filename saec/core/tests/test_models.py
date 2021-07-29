from datetime import timedelta

from django.utils import timezone

from saec.core.models import ComunicacaoAgendada


def test_model_comunicacao_agendada():
    ComunicacaoAgendada.objects.create(
        data=timezone.now() + timedelta(days=1),
        mensagem="Bom dia!",
        via=ComunicacaoAgendada.Via.WHATSAPP,
        para='5521987654321',
        status=ComunicacaoAgendada.Status.AGENDADA
    )

    assert ComunicacaoAgendada.objects.count() == 1
