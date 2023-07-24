# Project Name: Ami Coding Pari Na

[EVIDENT BD LTD : JUNIOR SOFTWARE ENGINEER DEMO PROJECT]

## Description

[As per instruction provided by the send link, I build the application by using Django(python framework)]

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
## Installation

To install and run this Django project on your local machine, follow these steps:

### Clone the repository:
- $ `git clone https://github.com/mehedi-softdev/python_project_evidentbd`
- $ `cd python_project_evidentbd`

### Set up a virtual environment (optional but recommended)::
- $ `virtualenv venv`
- $ `source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

### Install the project dependencies:
- $ `pip install -r requirements.txt`

### Apply database migrations:
- $ `python manage.py makemigrations`
- $ `python manage.py migrate`


### If css style not work then run the following command:
- $ `python manage.py collectstatic`

### Run the development server:
- $ `python manage.py runserver`




## Usage

### Section 1
User Authentication:
- Users must log in to use the application. If not registered, they can create a new account.

### Section 2
Input Data:
- Users have to enter comma-separated integer values and a search key in the respective input fields.

### Section 3
API Call:
- To make an API call, users must be logged in.
- Add the following URL after the root URL of the server:
- `/api/get_input_values/?start_datetime=2023-01-01 00:00:00&end_datetime=2023-07-24 23:59:59&user_id=1`

- The response should be in the following format:
```json
{
    "status": "success",
    "user_id": 1,
    "payload": [
        {
            "timestamp": "2012-01-01 00:00:00",
            "input_values": "11, 10, 9, 7, 5, 1, 0"
        },
        {
            "timestamp": "2013-01-01 01:00:00",
            "input_values": "13, 11, 10, 7, 5, 2, 1"
        }
    ]
}


*Note: This project is developed by Mehedi Hasan. As for company requirements as a demo project. 

