[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berrondo/saec)

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

### endpoint 1

Receber uma solicitação de agendamento de envio de comunicação (SAEC) com as informações:

 - Data/Hora para o envio,
 - Destinatário,
 - Mensagem a ser entregue

1. Assumiremos que o "Destinatário" é uma Pessoa (um Cliente) pré-cadastrada e será desse cadastro que obteremos:
  - endereço de email,
  - número do telefone, para SMS e whatsapp

2. Assumiremos que uma mensagem pode ser enviada para um destinatário único (personalizada) ou para vários destinatários (por exemplo, uma campanha)

3. Assumiremos que o serviço solicitador do agendamento tem acesso à base de Clientes, sendo capaz de selecionar aquele(s) que será(ão) alvo(s) de uma dada comunicação. E responsabilidade dele fornecer o(s) id(s) de Cliente para o(s) qual(is) queira agendar comunicação(ões).

4. Assumiremos que o serviço de envio das comunicações será capaz de lidar com cada um dos meios de envio previstos (emal, sms, push e whatsapp) e gerenciar o fluxo e os status peculiares de cada meio.

5. Assumiremos um serviço de push em *broadcast*, ou seja, não individualizado.
