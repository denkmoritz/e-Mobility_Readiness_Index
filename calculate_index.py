import psycopg2
from db import get_db_connection

TABLE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS emri (
        ID TEXT,
        Name TEXT,
        Bundesland TEXT,
        "2020" DOUBLE PRECISION,
        "2021" DOUBLE PRECISION
    );
"""
def create_emri_table(table_name):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(TABLE_SCHEMA)
        conn.commit()
        print(f"Table emri is ready!")

    except Exception as e:
        conn.rollback()
        print(f"Error creating table emri: {e}")

    finally:
        cur.close()
        conn.close()


query = """
SELECT
    e.ID AS ID,
    e.Name AS Name,
    e.Bundesland AS Bundesland,
    0.33*e."2020" + 0.33*l."2020"+0.34*s."2020" AS emri_2020,
    0.33*e."2021" + 0.33*l."2021"+0.34*s."2021" AS emri_2021,
    g.geometry AS geometry
    
FROM e_auto e, ladesaeulen l, strom s, LK_geom g
ON e.ID = g.CC_2
"""
def create_emri_index(table_name):
    conn = get_db_connection()
    cur = conn.cursor()