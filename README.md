# GitHub Application

## Team 3

Milana Tucakov\
Nikola Zejak\
Nikolina Gašić

## Requirements

[Django](https://docs.djangoproject.com/en/4.0/) >=3.0,<4.0 \
[psycopg2](https://pypi.org/project/psycopg2/) >=2.8\
[django-enumfields](https://pypi.org/project/django-enumfield/)\
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

## Model

![bLHDRziy3BxxLnW-1YtmzjfJtpN642oBWxXRpuhDfbfboHFb5iMm_pvPZ5mQIhVcOaiaduVVka4dh1iwbO4Ukdo5E43jX8FyLvRdTzMokl3_rMQxgpxlohgcswxylYhln_EosfJPRmBlG3HE6dttsXDylVfI1gDLFHwZtLUf09tHp56rBJVbShIzNLSrdVvVhpsYKGBHK_S6fJFsDPWxwHHSv-Yir0T_Rm4RA_lHEPDAt5hv](https://user-images.githubusercontent.com/57504983/206870348-8fffc02f-7069-486e-be9b-e0f18f9ed55d.png)
