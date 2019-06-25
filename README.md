# Project-Litter-Bug-Web

Front end component to display current status and archival data of Project Litter Bug script

# To Run Locally:

1. `~/cloud_sql_proxy -instances=litter-bug:us-central1:plb-db=tcp:3306`
2. `docker run -p 6379:6379 -d redis:2.8`
3. `python manage.py runserver`