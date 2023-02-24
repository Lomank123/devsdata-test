# devsdata-test


## Docker setup

- If you have Docker run these commands (Caution: I didn't have time to test it properly so errors may occur):
```
cd path/to/root
docker-compose up -d --build
```

## Installation


- Create and activate venv using following commands:
```
cd path/to/project
mkdir venv
cd venv
python3 -m venv .
```

- Install requirements:
```
pip install -r requirements.txt
```

- Copy `.env.sample` to `.env`:
```
copy .env.sample .env
```

- Apply migrations:
```
python3 manage.py migrate
```

- Create superuser (creds located in `.env.sample`):
```
python3 manage.py createsuperuser --no-input
```

- Run server:
```
python3 manage.py runserver
```

- Log in and enjoy :)


## Description

- When click on "Attend" button you will receive reservation code, but if you update the page it won't display, so be cautious. To find this code visit `http://127.0.0.1:8000/admin`, login as admin and open "Reservation codes" page on the left.

Project uses Django and REST Framework, main logic is located in `main/views.py`. There you can expext 2 important view classes:

- `RegisterToEventView`
- `CancelRegistrationView`

DB models located in `main/models.py`. Actually there are 2 of them

- `Event`
- `ReservationCode` - client's code.

In `/templates` dir you may find all `.html` files and in `/static` all `.js` and `.css` files can be found.
