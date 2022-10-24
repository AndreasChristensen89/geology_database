@classmethod
def refresh_view(cl):
    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY field_missions_view")