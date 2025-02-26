# Wingz Python/Django Developer Test

## Django Setup

0. Setup `postgresql` database (`DB_NAME`, `DB_USER`, and `DB_PASSWORD` are needed in `.env`)
1. Create and define `.env` in `api/` (use `.env.example` as guide)
2. `poetry install`
3. `cd api/`
4. `poetry run python manage.py migrate`
5. `poetry run python manage.py createsuperuser`
6. `poetry run python manage.py runserver`
7. To test, `poetry run pytest`

## Bonus - SQL

```SQL
WITH RideDurations AS (
    SELECT
        r.id_ride,
        r.id_driver_id,
        DATE_TRUNC('month', pickup_event.created_at) AS month,
        EXTRACT(EPOCH FROM (dropoff_event.created_at - pickup_event.created_at)) / 3600 AS duration_hours
    FROM rides_ride r
    JOIN rides_rideevent pickup_event
        ON pickup_event.id_ride_id = r.id_ride
        AND pickup_event.description = 'Status changed to pickup'
    JOIN rides_rideevent dropoff_event
        ON dropoff_event.id_ride_id = r.id_ride
        AND dropoff_event.description = 'Status changed to dropoff'
)
SELECT
    TO_CHAR(month, 'YYYY-MM') AS month,
    u.first_name || ' ' || LEFT(u.last_name, 1) AS driver,
    COUNT(*) AS count_of_trips_over_1_hr
FROM RideDurations rd
JOIN users_user u ON u.id_user = rd.id_driver_id
WHERE rd.duration_hours > 1
GROUP BY month, driver
ORDER BY month, driver;
```

To run in Django, run the reports file as:

```python
from apps.rides.reports import get_long_trips_report
```
