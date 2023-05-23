![Vodafone Logo](https://assets.vodafone.co.uk/cs/groups/public/documents/webcontent/img_vodafone__icon.png)

# Vodafone Employee Tracker

![Python 3.11.3](https://img.shields.io/badge/Python%203.11.3-20232A?style=for-the-badge&logo=python&logoColor=4584b6)
![Flask](https://img.shields.io/badge/Flask-20232A?style=for-the-badge&logo=flask&logoColor=4584b6)
![Pandas](https://img.shields.io/badge/Pandas-20232A?style=for-the-badge&logo=pandas&logoColor=ffde57)

Employee Tracking App written in Python &amp; Flask for the BF&amp;C Hons. Degree Course (Distributed Collaborative Environments).

## Requirements

- Python 3.11.3 (You can download Python for any system [here](https://www.python.org/downloads/release/python-3113/).)

## Installing dependencies

The web application uses a few Python dependencies to run, such as Flask for the API web-server and Pandas for file reading.
Run the below commands line-by-line in order to install the dependencies.

```shell
cd web
pip3 install flask
pip3 install pandas
```

## Running the Application

### Terminal Client and Server

Run the below command to run the main socket application. You will be prompted to either start it as a Client (C) or Server (S).

```shell
python3 run.py
```

### Web-based Interface

Run the below command to run the web-based interface. Please ensure that the port "8000" is free on your machine. You may wish to run `npx kill-port 8000` if the port is taken, or manually close the task via your terminal.
The web-server will fetch data from the `.csv` file automatically on each page refresh, so you are welcome to run both applications simultaneously.

```shell
cd web
python3 web.py
```

The web-based interface will then run on the following URL: http://127.0.0.1:8000/
