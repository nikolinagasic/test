# GitHub Application

## Team 3

Milana Tucakov\
Nikola Zejak\
Nikolina Gašić

## Requirements

[Django](https://docs.djangoproject.com/en/4.0/) >=3.0,<4.0 \
[psycopg2](https://pypi.org/project/psycopg2/) >=2.8\
[Docker](https://www.docker.com/get-started)

## Set environment variables

Rename the `dotenv` file to the `.env`. And fill your values

```shell
SECRET_KEY=your_secret_key
POSTGRES_NAME=your_postgres_name
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
```

## To run local database (needed for docker compose):

```
docker run --name NAME -e POSTGRES_PASSWORD=PASSWORD -d postgres
```

## To run manage.py commands:

```
docker-compose run django $COMMAND
```

## To run docker images:

```
docker-compose up --build
```
