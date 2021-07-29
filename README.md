[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berrondo/saec-1)

# SAEC - Solicitação de Agendamento de Envio de Comunicação

Desenvolvimento de uma plataforma de comunicação

## Para executar, desenvolver e/ou testar...

Levante primeiro o banco de dados. Voce não precisa ter o *postgres* instalado se tiver o *docker-compose*:

### Postgres (docker-compose):

```console
# para executar o banco de dados postgres
docker-compose up --build -d

# para parar o banco de dados:
docker-compose down
```

Para a aplicação, certifique-se de ter o Git e o Python 3.9.6 instalado:

1. Clone o repositório
2. Crie um *virtualenv* com Python 3.9.6
3. Ative o *virtualenv*
4. Instale as dependências do projeto
5. Configure a instância da aplicação com o .env
6. Execute as migrações de banco de dados   
7. Execute os testes
8. Rode o servidor da aplicação

```console
git clone git@github.com:berrondo/ca.git ca

cd ca
python -m venv env
source env/bin/activate

pip install -r requirements-dev.txt
cp contrib/env_sample .env

python manage.py migrate
python manage.py test
python manage.py runserver
```

## O Problema

### (1) Primeiro endpoint, o agendador:
#### POST /agendamento

Este *endpoint* vai receber uma solicitação de agendamento de envio de comunicação (SAEC) com as seguintes informações:

 - Data/Hora para o envio,
 - Destinatário,
 - Mensagem a ser entregue,

 1. Assumiremos que o serviço solicitador do agendamento tem acesso à base de Clientes, sendo capaz de selecionar aquele(s) que será(ão) alvo(s) de uma dada comunicação e suas informações de contato.

 2. é responsabilidade do solicitador do agendamento a formatação definitiva das mensagens, considerando limites do meio escolhido, *place holders* para eventual substituição, formatação, etc.

 3. O agendador não fará qualquer validação ou tratamento da mensagem.

 4. A solicitação de agendamento será feita assim:

```
    POST /agendamento
    {
        "data": UMA_DATA_FUTURA,
        "mensagem": "Bom dia!",
        "via": "email",
        "para": "e@mail.com"
    }
```

 5. “**via**“ pode ser **email**, **sms**, **whatsapp** ou **push**.
    
 6. “**para**” será informado em função da “**via**” escolhida, respetivamente: **endereço de email**, **número de telefone**, **número de telefone**, **token id** ou informação pertinente ao serviço de “*push notification*” utilizado.

 7. A flexibilidade para o envio é bastante grande. A mesma mensagem pode ser enviada por qualquer combinação das quatro opções de “**via**” e a mesma mensagem pode ser enviada “**para**” vários destinos diferentes, permitindo a utilização do agendamento também para “campanhas”.

 8. Espera-se que o responsável pelo *envio* das comunicações seja capaz de lidar com cada “**via**” prevista (email, sms, push e whatsapp) e gerenciar fluxo e status peculiares de cada “**via**”.

### (2) Segundo endpoint, consulta ao status do agendamento:
#### GET /agendamento/{id}

A consulta pelo id do agendamento retornará:

```
    GET /agendamento/1234567
    {
        "id": '1234567',
        "data": UMA_DATA_FUTURA,
        "mensagem": "Bom dia!",
        "via": "email",
        "para": "e@mail.com"
        "status": "AGENDADA",
    }
```

### (3) Terceiro endpoint, cancelando um agendamento:
#### DELETE /agendamento/{id}

Assumiremos um DELETE “lógico”, não “físico”.

Para ser cancelada, uma comunicação agendada deverá estar em status **AGENDADA**, ou seja, não ter sido ainda **ENVIADA**. Assim, o cancelamento deve ser solicitado antes da data agendada para o envio.

O cancelamento não terá nenhum efeito sobre os status **PROCESSADA** ou **CANCELADA**.

O retorno desta requisição será:

```
    DELETE agendamento/1234567
    GET agendamento/1234567
    {
        "id": '1234567',
        "data": UMA_DATA_FUTURA,
        "mensagem": "Bom dia!",
        "via": "email",
        "para": "e@mail.com"
        'status': "CANCELADA",
    }
```
