# WMATA Train Positions Project

This project provides two ways to access WMATA (Washington Metropolitan Area Transit Authority) train position data, filtered for yellow line trains headed to Huntington Station that are taking passengers.

## Setup

### Prerequisites

- Python 3.x (Recommended)
- Pip (Python package manager)

### Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage project dependencies. Here's how to create and activate a virtual environment:

```bash
# Create a virtual environment (you can choose a different name if desired)
python -m venv myenv

# Activate the virtual environment (use the appropriate command for your shell)
# On macOS and Linux:
source myenv/bin/activate
# On Windows (Command Prompt):
myenv\Scripts\activate
# On Windows (PowerShell):
myenv\Scripts\Activate.ps1
```


### Install Dependencies

To run the simple.py script, you need to install the requests library:

```bash
pip install requests
```

To run the trains.py Flask application, you need to install the following libraries:

```bash
pip install flask
pip install flask-bootstrap
```


## Usage
### simple.py

simple.py is a Python script that retrieves train positions and prints filtered data to the console. To run it, use the following command:

```bash
python simple.py
```


### trains.py (Flask Application)

trains.py is a Flask application that provides a dedicated web page for viewing filtered train positions. To run the application, use the following command:

```bash
python trains.py
```
Once the application is running, open a web browser and navigate to http://localhost:5000 to access the train positions in a more user-friendly format.
