# Wingz Python/Django Developer Test

## Django Setup

0. Setup `postgresql` database
1. Create and define `.env` in `api/` (use `.env.example` as guide)
2. `poetry install`
3. `cd api/`
4. `poetry run python manage.py migrate`
5. `poetry run python manage.py createsuperuser`
6. `poetry run python manage.py runserver`
7. To test, `poetry run pytest`
