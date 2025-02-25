import os
import psycopg2
import pandas as pd
from db import get_db_connection  # Import your DB connection function

DATA_FOLDER = "data/"

# Table mapping based on filename start
TABLE_MAPPING = {
    "e-auto": "e_auto",
    "ladesaeulen": "ladesaeulen",
    "strom": "strom"
}

# Define the table schema
TABLE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS {table_name} (
        Name TEXT,
        Bundesland TEXT,
        "2020" NUMERIC,
        "2021" NUMERIC
    );
"""


def create_table_if_not_exists(table_name):
    """
    Creates a table in PostGIS if it does not exist.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(TABLE_SCHEMA.format(table_name=table_name))
        conn.commit()
        print(f"Table `{table_name}` is ready!")

    except Exception as e:
        conn.rollback()
        print(f"Error creating table `{table_name}`: {e}")

    finally:
        cur.close()
        conn.close()


def import_csv_to_postgis(csv_file_path, table_name):
    """
    Reads CSV using pandas, formats it, and inserts into the PostGIS table.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # Read CSV with German formatting
        df = pd.read_csv(csv_file_path, sep=";", decimal=",")

        # Ensure column names match expected format
        expected_columns = ["Name", "Bundesland", "2020", "2021"]
        df = df[expected_columns]

        # Convert dataframe to list of tuples for insertion
        data_tuples = [tuple(x) for x in df.to_records(index=False)]

        # Insert data into the table
        insert_query = f"""
            INSERT INTO {table_name} (Name, Bundesland, "2020", "2021")
            VALUES (%s, %s, %s, %s)
        """
        cur.executemany(insert_query, data_tuples)

        conn.commit()
        print(f"📂 Imported {len(df)} rows into `{table_name}`!")

    except Exception as e:
        conn.rollback()
        print(f"Error importing `{csv_file_path}`: {e}")

    finally:
        cur.close()
        conn.close()


def process_all_csv_files():
    """
    Processes all CSV files, assigns them to the correct table, and imports data.
    """
    csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

    if not csv_files:
        print("No CSV files found in the 'data/' directory.")
        return

    for csv_file in csv_files:
        csv_path = os.path.join(DATA_FOLDER, csv_file)

        # Determine the correct table based on filename prefix
        matching_table = None
        for key in TABLE_MAPPING:
            if csv_file.startswith(key):
                matching_table = TABLE_MAPPING[key]
                break

        if not matching_table:
            print(f"Skipping `{csv_file}` (No matching table found).")
            continue

        print(f"Processing `{csv_file}` → Table: `{matching_table}`")

        # Ensure the table exists before inserting data
        create_table_if_not_exists(matching_table)

        # Import CSV into the database
        import_csv_to_postgis(csv_path, matching_table)


# Run the script
if __name__ == "__main__":
    process_all_csv_files()