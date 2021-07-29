from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from saec.core.models import ComunicacaoAgendada

URL = reverse('agendamento-list')

UMA_DATA_FUTURA = (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S.%f')
UMA_DATA_PASSADA = (timezone.now() - timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S.%f')


@pytest.fixture
def agendamento():
    return {
            "data": UMA_DATA_FUTURA,
            "mensagem": "Bom dia!",
            "para": "ana@ana.com",
            "via": "email",
        }


def test_post_agendamento(api_client, agendamento):
    resp = api_client().post(
        URL,
        agendamento,
        format='json',
    )

    assert resp.status_code == status.HTTP_201_CREATED


def test_delete_cancela_agendamento(api_client, agendamento):
    # given:
    resp = api_client().post(URL, agendamento, format='json')
    detail_url = reverse('agendamento-detail', kwargs={'pk': str(resp.data['id'])})

    # when
    resp = api_client().delete(detail_url)

    # then
    assert resp.status_code == status.HTTP_204_NO_CONTENT

    # and
    resp = api_client().get(detail_url)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data['status'] == ComunicacaoAgendada.Status.CANCELADA


def test_data_de_agendmento_nao_futura(api_client, agendamento):
    # given
    agendamento = agendamento.copy()
    agendamento['data'] = UMA_DATA_PASSADA

    # when
    resp = api_client().post(
        URL,
        agendamento,
        format='json',
    )

    # then
    assert resp.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.parametrize('para,via', (
        ("nao é um endereço de email!", "email"),
        ("não é um telefone", "sms"),
        ("não é um telefone", "whatsapp"),
        # ("", "push"),  # existe um formato? pode ser qualquer coisa??
))
def test_destino_correspondente_deve_ser_informado(api_client, agendamento, via, para):
    # given
    agendamento = agendamento.copy()
    agendamento['para'] = para
    agendamento['via'] = via

    # when
    resp = api_client().post(
        URL,
        agendamento,
        format='json',
    )

    # then
    assert resp.status_code == status.HTTP_400_BAD_REQUEST


def test_atualizacao_do_agendaento_nao_eh_permitida(api_client, agendamento):
    """Se relamente necessário, CANCELE (DELETE) o agendamento e envie um novo"""

    # given
    agendamento = agendamento.copy()
    mensagem_corrigida = 'mensagem corrigida'
    agendamento['name'] = mensagem_corrigida

    # when
    resp = api_client().put(
        URL,
        agendamento,
        format='json',
    )

    # then
    assert resp.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
