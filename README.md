![Vodafone Logo](https://assets.vodafone.co.uk/cs/groups/public/documents/webcontent/img_vodafone__icon.png)

# Vodafone Employee Tracker

![Python 3.11.3](https://img.shields.io/badge/Python%203.11.3-20232A?style=for-the-badge&logo=python&logoColor=4584b6)
![Flask](https://img.shields.io/badge/Flask-20232A?style=for-the-badge&logo=flask&logoColor=4584b6)
![Pandas](https://img.shields.io/badge/Pandas-20232A?style=for-the-badge&logo=pandas&logoColor=ffde57)

Employee Tracking App written in Python &amp; Flask for the BF&amp;C Hons. Degree Course (Distributed Collaborative Environments).

## Requirements

- Python 3.11.3 (You can download Python for any system [here](https://www.python.org/downloads/release/python-3113/).)

## Installing dependencies

### Python virtual environment setup

####  Installing virtual environment package (Linux)

```shell
sudo apt install python3.11-venv
python3 -m pip install --user virtualenv
```

####  Installing virtual environment package (Windows)

Python virtual environment should come pre-installed with Windows.

####  Installing the required libraries

```shell
python3 -m venv .venv
python3 -m pip install -r requirements.txt

```

####  Installing the required libraries (Windows)

```shell
py -m venv .venv
.venv\Scripts\activate.bat
py -m pip install -r requirements.txt
```

 If you are unable to download the virtual environments package, you can just install the packages listed in requirements.txt. 

## Running the Application

### Terminal Client and Server

Run the below command to run the main socket application. You will be prompted to either start it as a Client (C) or Server (S).

```shell
python3 run.py
```

Follow the prompts.

### Web-based Interface

Run the below command to run the web-based interface. Please ensure that the port "8000" is free on your machine. You may wish to run `npx kill-port 8000` if the port is taken, or manually close the task via your terminal.
The web-server will fetch data from the `.csv` file automatically on each page refresh, so you are welcome to run both applications simultaneously.

```shell
cd web
python3 web.py
```

The web-based interface will then run on the following URL: http://127.0.0.1:8000/
