# API REST com GUnicorn + Flask + Psycopg

CRUDE de uma API REST com os endpoints implementados com aiohttp e acesso à base de dados com aiopg.

## Requisitos

- docker
- docker-compose

## Docker

### Instalação

Para instalar Docker, executar o comando abaixo:

```shell
curl -fsSL https://get.docker.com | sh;
```

> O script identificará a plataforma de sistema operacional e irá instalar o pacote de acordo com a mesma.

### Configuração

Para configurar o ambiente, executar os comandos abaixo:

```shell
# Adicionar o usuário no grupo Docker
sudo groupadd docker && sudo usermod -aG docker $USER

# Habilitar a inicialização do serviço no boot
sudo systemctl enable docker

# Inicializar o serviço
sudo systemctl start docker
```

> É provável que seja necessário um logoff e login para carga de configurações dos grupos de usuários.

## Docker Composer

### Instalação

Executar os comandos abaixo:

```shell
# Download do pacote
sudo curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

# Permissão para execução
sudo chmod +x /usr/local/bin/docker-compose

# Teste
docker-compose -v
```

## Banco de Dados

A plataforma de banco de dados utilizada foi `PostgreSQL` em sua versão `11.0`. A instância de banco de dados utilizada foi criada com a utilização de contêiner Docker.

A estrutura de dados para execução do CRUDE está contemplada no script `db/db.sql`. Consta, também, comandos para inserção de três registros iniciais.

## Aplicação

A aplicação foi construída com a plataforma `Python3.7`.

- `backend`: aplicação construída com o aiohttp server, que fornece uma api integrada ao banco de dados com uso do `aiopg`

## Execução

A execução da aplicação depende, unicamente, da criação de três contêineres, por meio do `docker-compose.yml` fornecido. Os comandos são:

```shell
# Verificar os contêineres em execução
docker ps

# Verificar todos os contêineres criados - em execução ou não
docker ps -a

# Criar todos os contêineres com seus respectivos volumes
docker-compose up -d

# Criar um contêiner específico do docker-compose.yml

docker-compose up -d $SERVICE_NAME # SERVICE_NAME = database | backend | client

# Verificar os logs de um contêiner
docker logs -f $CONTAINER_NAME # CONTAINER_NAME = postgres | backend | client

# Destruir os contêineres com os volumes
docker-compose down -v
```

## Requisições

Segue exemplos de requisições aos endpoints disponibilizados com o uso do `curl`

```shell
# Obter os dados de todos os autores
curl -X GET 'http://localhost:8080/api/v1/authors'

# Obter os dados de um autor específico
curl -X GET 'http://localhost:8080/api/v1/authors?id=3'

# Cadastrar um novo autor
curl -X POST 'http://localhost:8080/api/v1/authors' \
-H "Content-Type: application/json" \
-d '{"first_name": "Joao", "last_name": "GRILO", "email": "joao.grilo@mail.com"}'

# Atualizar os dados de um autor
curl -X PUT 'http://localhost:8080/api/v1/authors' \
-H "Content-Type: application/json" \
-d '{"id": 4, "first_name": "Chico", "last_name": "H", "email": "chico.h@mail.com"}'

# Remover os dados de um autor específico
curl -X DELETE 'http://localhost:8080/api/v1/authors?id=4'
```
