# Coding Challenge
Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the json format.

## Setup
1.**Clone this Repo**

  ```
    git clone https://github.com/sandhya-ch/FullThrottle-Labs-coding-Challange.git
  ```
2.**Install Python version 3.8 or greater**
  ```
    https://www.python.org/downloads/
  ```
3.**Create virtual environment and activate it**
   ```
      python3 -m venv myvenv
      myvenv/Scripts/active
   ```
4.**Install requirements**
   ```
      pip install -r requirements.txt
  ```
5.**Dump the Data from Sample CSV File**
  ```
    python manage.py my_custom_command
    
    This will insert the sample dummy data into the database
  ```
6.**To run server**
  ```
    python manage.py runserver
  ```
7.**after that open Browser and call the following url**
  ```
    http://127.0.0.1:8000/activity
  ```
  This will show the result in the json format.
