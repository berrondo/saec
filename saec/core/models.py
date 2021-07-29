from django.db import models


class ComunicacaoAgendada(models.Model):
    data = models.DateTimeField()
    mensagem = models.TextField()

    class Via(models.TextChoices):
        EMAIL = 'email', 'Email'
        SMS = 'sms', 'SMS'
        PUSH = 'push', 'Push'
        WHATSAPP = 'whatsapp', 'WhatsApp'

    via = models.CharField(
        max_length=10,
        choices=Via.choices,
    )

    # email, telefone, token...
    para = models.CharField(max_length=255)

    class Status(models.TextChoices):
        AGENDADA = 'AGENDADA', 'Agendada'
        ENVIADA = 'ENVIADA', 'Enviada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.AGENDADA
    )

    class Meta:
        unique_together = [
            'data',
            'mensagem',
            'via',
            'para',
            'status',
        ]
