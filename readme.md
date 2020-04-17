# Create cron job to run python (using pandas library) script inside flask app in background

1. create python script to run
run.py

2. install requirements.txt to install dependencies
python install -r requirements.txt

3. Create app.py flask app

4. Run flask server (Bydefault it will run on http://localhost:5000)
python app.py

5. Check if server works - Visit http://localhost:5000/test
You will see message on GET Request - 'Flask Background Scheduler Cron Job'

6. Check if cron is working in background
check time (it should update every minute) creation of pop.csv file
