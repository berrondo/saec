from datetime import timedelta

from django.utils import timezone

import pytest
from model_bakery import baker

from saec.core.models import (
    Cliente,
    ComunicacaoAgendada,
    ComunicacaoAgendada_Cliente
)


def test_model_cliente():
    Cliente.objects.create(
        usuario="ana",
        email="ana@ana.com",
        telefone="5521998765432",
    )

    assert Cliente.objects.count() == 1


@pytest.fixture
def ana():
    return baker.make('Cliente', usuario='ana')


def test_model_comunicacao_agendada(ana):
    ComunicacaoAgendada.objects.create(
        data=timezone.now() + timedelta(days=1),
        mensagem="Bom dia!",
    )

    assert Cliente.objects.count() == 1
    assert ComunicacaoAgendada.objects.count() == 1



@pytest.fixture
def bob():
    return baker.make('Cliente', usuario='bob')


@pytest.fixture
def comunicacao():
    return baker.make('ComunicacaoAgendada', mensagem='Oi')


def test_comunicacao_agendada(bob, comunicacao):
    cac = ComunicacaoAgendada_Cliente.objects.create(
        destinatario=bob,
        comunicacao=comunicacao,
        via=ComunicacaoAgendada_Cliente.Via.WHATSAPP,
    )

    assert Cliente.objects.count() == 1
    assert ComunicacaoAgendada.objects.count() == 1
    assert ComunicacaoAgendada_Cliente.objects.count() == 1
    assert cac.status == ComunicacaoAgendada_Cliente.Status.AGENDADA