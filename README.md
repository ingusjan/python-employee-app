# python-employee-app

Employee Tracking App written in Python &amp; Flask for BF&amp;C

## Requirements

- Python 3.11.3

## Installing dependencies


### Python virtual environment setup

####  Installing virtual environment package (Linux)

```shell
sudo apt install python3.10-venv
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

```shell
python3 run.py
```

Follow the prompts.

### Web-based Interface

```shell
cd web
python3 web.py
```
