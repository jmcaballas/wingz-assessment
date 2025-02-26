from django.db import connection


def get_long_trips_report():
    sql = """
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
    """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()

    return [
        {"month": row[0], "driver": row[1], "count_of_trips_over_1_hr": row[2]}
        for row in results
    ]


report = get_long_trips_report()
for row in report:
    print(row)
