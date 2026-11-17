def average_grade(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        result = cur.fetchone()[0]
    return float(result) if result is not None else None