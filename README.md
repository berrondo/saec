[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berrondo/saec)

# SAEC - Solicitação de Agendamento de Envio de Comunicação

Uma plataforma de comunicação para agendar o envio de mensagens por vários meios.

## Para executar, desenvolver e/ou testar...

### Gitpod

Clicando no botão [Gitpod | ready-to-code], você pode rodar e interagir com a aplicação na nuvem (rodando com postgres!), no https://gitpod.io , além de ter acesso ao código, aos testes e tudo o mais através de um vscode e do terminal! é só clicar:

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berrondo/saec)

### Usando apenas Docker e docker-compose:

Certifique-se de ter o Git, Docker e docker-compose instalados:

1. Clone o repositório
2. Crie a imagem e suba o conteiner da aplicação e do banco \o/

```console
git clone git@github.com:berrondo/saec.git saec
cd saec
docker-compose up --build -d
```

Voce poderá acessar a aplicação em http://localhost:8000

### Usando docker-compose apenas para o banco de dados:

Para a aplicação, certifique-se de ter o Git e o Python 3.8 instalado:

1. Clone o repositório
2. Crie um *virtualenv* com Python 3.8
3. Ative o *virtualenv*
4. Instale as dependências do projeto
5. Configure a instância da aplicação com o .env
6. Suba a instância do Postgres com o docker-compose
7. Execute as migrações de banco de dados   
8. Execute os testes
9. Rode o servidor da aplicação

```console
git clone git@github.com:berrondo/saec.git saec

cd saec
python -m venv env
source env/bin/activate

pip install -r requirements-dev.txt
cp contrib/env_sample .env

docker-compose up --build -d db

python manage.py migrate
pytest
python manage.py runserver
```

### Postgres (docker-compose):

Para levantar e parar apenas a instância do banco de dados, voce não precisa ter o *postgres* instalado se tiver o *docker-compose*:

```console
# para executar o banco de dados postgres
docker-compose up --build -d db

# para parar o banco de dados:
docker-compose down
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
    
    dados = {
        "data": UMA_DATA_FUTURA,
        "mensagem": "Bom dia!",
        "via": "email",
        "para": "e@mail.com"
    }
```

 5. “**via**“ pode ser **email**, **sms**, **whatsapp** ou **push**.
    
 6. “**para**” será informado em função da “**via**” escolhida, respetivamente: **endereço de email**, **número de telefone**, **número de telefone**, **token id** ou informação pertinente ao serviço de “*push notification*” utilizado.

 7. A flexibilidade para o envio é bastante grande. A mesma mensagem pode ser enviada por qualquer combinação das quatro opções de “**via**” e a mesma mensagem pode ser enviada “**para**” vários destinos diferentes, permitindo a utilização do agendamento também para “campanhas”.

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

Não será permitida a atualização dos dados de qualquer agendamento. Se realmente necessário, é preciso CANCELAR (DELETE) o agendamento e enviar a nova versão desejada.
