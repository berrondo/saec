from django.db import models


class Cliente(models.Model):
    usuario = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)


class ComunicacaoAgendada(models.Model):
    data = models.DateTimeField()
    mensagem = models.TextField()


class ComunicacaoAgendada_Cliente(models.Model):
    destinatario = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    comunicacao = models.ForeignKey(ComunicacaoAgendada, on_delete=models.PROTECT)

    class Via(models.IntegerChoices):
        EMAIL = 0
        SMS = 1
        PUSH = 2
        WHATSAPP = 3

    via = models.IntegerField(
        choices=Via.choices,
    )

    class Status(models.IntegerChoices):
        AGENDADA = 0
        ENVIADA = 1
        CANCELADA = 2

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.AGENDADA
    )
