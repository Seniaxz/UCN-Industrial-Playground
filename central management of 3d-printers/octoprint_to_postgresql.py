import datetime
import json
from psycopg2 import connect, sql
from octoprint_api import OctoPrintApiClient

# Set up connection to OctoPrint API
octoprint_url = 'http://localhost:8080'
octoprint_api_key = 'YOUR_API_KEY'
client = OctoPrintApiClient(octoprint_url, octoprint_api_key)

# Set up connection to PostgreSQL database
db_host = 'localhost'
db_port = 5432
db_name = 'your_database_name'
db_user = 'your_database_user'
db_password = 'your_database_password'
conn = connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
cur = conn.cursor()

# Define SQL query to insert data into database
create_table_query = sql.SQL("""
CREATE TABLE IF NOT EXISTS prints (
    id SERIAL PRIMARY KEY,
    print_id VARCHAR(255),
    print_state VARCHAR(255),
    print_start TIMESTAMP WITH TIME ZONE,
    print_duration INTERVAL,
    print_filename TEXT,
    print_extruder_temperature INTEGER,
    print_bed_temperature INTEGER,
    print_progress FLOAT
)
""")
cur.execute(create_table_query)
insert_data_query = sql.SQL("""
INSERT INTO prints (print_id, print_state, print_start, print_duration, print_filename, print_extruder_temperature, print_bed_temperature, print_progress)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

# Get list of completed and printing 3D prints from OctoPrint API
jobs = client.jobs()
for job in jobs:
    state = job['state']
    if state == 'Operational' or state == 'Printing':
        print_id = job['job']['id']
        print_state = job['state']
        print_start = datetime.datetime.fromisoformat(job['job']['timestamp'])
        print_duration = datetime.timedelta(seconds=int(job['job']['estimatedPrintTime'])) if 'estimatedPrintTime' in job['job'] else None
        print_filename = job['job']['file']['name']
        print_extruder_temperature = int(job['temperature']['current']) if 'temperature' in job and 'current' in job['temperature'] else None
        print_bed_temperature = int(job['bedTemperature']['current']) if 'bedTemperature' in job and 'current' in job['bedTemperature'] else None
        print_progress = float(job['job']['progress']['completion']) if 'progress' in job and 'completion' in job['job']['progress'] else 0

        # Insert data into PostgreSQL database
        values = (print_id, print_state, print_start, print_duration, print_filename, print_extruder_temperature, print_bed_temperature, print_progress)
        cur.execute(insert_data_query, values)

# Commit changes to PostgreSQL database
conn.commit()
cur.close()
conn.close()



# Content of requrements.txt
# Install octoprint-api library
# pip install octoprint-api
# Install PostgreSQL adapter for Python by running:
# pip install psycopg2-binary

