# Descrição do projeto.

Esse projeto foi criado usando Django e Django Rest Framework. A API fornece endpoints para gerenciar informações sobre profissionais da área da saúde e consultas médicas. </br>

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
