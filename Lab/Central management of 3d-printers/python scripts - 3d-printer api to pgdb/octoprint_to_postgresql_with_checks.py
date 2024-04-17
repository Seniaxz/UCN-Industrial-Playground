# import datetime
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

# Define SQL query to check for existing print records
check_print_query = sql.SQL("""
SELECT * FROM prints
WHERE print_id = %s AND print_state = %s AND print_filename = %s
""")

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
insert_data_query = sql.SQL("""
INSERT INTO prints (print_id, print_state, print_start, print_duration, print_filename, print_extruder_temperature, print_bed_temperature, print_progress)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

# Create table in PostgreSQL database if it doesn't exist
cur.execute(create_table_query)
conn.commit()

# Retrieve information about completed and printing 3D prints from OctoPrint API
print_jobs = client.get('/api/job', params={'state': 'idle,printing'}).json()['jobs']
for print_job in print_jobs:
    # Skip if print has already been exported to database
    cur.execute(check_print_query, (print_job['id'], print_job['state'], print_job['file']['name']))
    if cur.rowcount > 0:
        continue
    
    # Extract information from OctoPrint API response
    print_start = datetime.datetime.fromisoformat(print_job['startTime']) if 'startTime' in print_job else None
    print_duration = (datetime.datetime.now() - print_start) if print_start else None
    print_extruder_temperature = int(print_job['temperature']['current']) if 'temperature' in print_job and 'current' in print_job['temperature'] else None
    print_bed_temperature = int(print_job['bedTemperature']['current']) if 'bedTemperature' in print_job and 'current' in print_job['bedTemperature'] else None
    print_progress = float(print_job['progress']['completion']) if 'progress' in print_job and 'completion' in print_job['progress'] else 0
    
    # Insert record into PostgreSQL database
    values = (print_job['id'], print_job['state'], print_start, print_duration, print_job['file']['name'], print_extruder_temperature, print_bed_temperature, print_progress)
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
