# Descrição do projeto.

Projeto criado usando Django e Django Rest Framework. A API fornece endpoints para gerenciar informações sobre profissionais da área da saúde e consultas médicas. </br>
Ele foi essencialmente pensado para que eu pudesse aplicar conceitos que eu já conhecia junto a novos conhecimentos que eu adquiri através da documentação do DRF. Portanto, há muitas coisas no código que DEVEM ser melhoradas. 

## Base URL

`/api/`

## Endpoints Disponíveis

- **Profissionais**
  - `/profissional/`
    - `GET`: Obter lista de todos os profissionais.
    - `POST`: Criar um novo profissional.
  - `/data/profissional/`
    - `GET`: Obter detalhes de um profissional por ID.
    - `POST`: Criar um novo profissional.
    - `PUT`: Atualizar detalhes de um profissional existente.
    - `DELETE`: Excluir um profissional existente.
    
- **Consultas**
  - `/consulta/`
    - `GET`: Obter lista de todas as consultas.
    - `POST`: Criar uma nova consulta.
  - `/data/consulta/`
    - `GET`: Obter detalhes de uma consulta por ID.
    - `POST`: Criar uma nova consulta.
    - `PUT`: Atualizar detalhes de uma consulta existente.
    - `DELETE`: Excluir uma consulta existente.

## Parâmetros de Requisição

- **GET**
  - `profissional`: ID do profissional desejado.
  - `consulta`: ID da consulta desejada.

## Exemplos

### Obter Lista de Profissionais

```http
GET /api/profissional/?profissional=1
```


# Instalação e Configuração

Siga estas instruções para configurar e executar o projeto em seu ambiente local.

## Pré-requisitos

Certifique-se de ter o Python e o Django instalados em seu sistema. Você também pode usar um ambiente virtual para isolar as dependências do projeto. </br>

### Clone o repositório

   1. Clone este repositório para o seu ambiente local usando o seguinte comando:

   ```bash
   git clone https://github.com/luizawander/api-django-drf
   ```
 ### Ativar o Ambiente Virtual (venv)

2. Antes de executar os comandos relacionados ao projeto Django, ative o ambiente virtual `venv`. Dependendo do seu sistema operacional e do método de criação do ambiente virtual, os comandos podem variar. 

#### Windows

```bash
.\venv\Scripts\activate
````

   ### Instale as Dependências

3. Navegue até o diretório do projeto e instale as dependências listadas no arquivo `requirements.txt` usando o pip:

```bash
cd api-django-drf
pip install -r requirements.txt
```
### Migrar Banco de Dados

4. Execute as migrações para criar as tabelas do banco de dados:

```bash
python manage.py migrate
```
### Executar o Servidor de Desenvolvimento

5. Para iniciar o servidor de desenvolvimento Django, utilize o seguinte comando:

```bash
python manage.py runserver
