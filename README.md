# DGBMICalculator App

Built by Darshan Gadkari

App:
1. Calculates the BMI (Body Mass Index) using Formula 1, BMI Category and Health risk
from Table 1 of the person and add them as 3 new columns
2. Count the total number of overweight people using ranges in the column BMI Category
of Table 1
3. Supports: Creation build, tests to make sure the code is working as expected and 
this can later be added to an automation build / testing / deployment pipeline
4. solid production-grade Python3 Program
5. is a stand-alone backend application
6. github url: https://github.com/gadkaridarshan/DGBMICalculator
7. Code is linted
8. Code built using Flask Blueprints for good code structuring
9. Code built using Flask-restplus to build REST APIs using best practices and minimal setup
10. setup.py provided for code packaging
11. When code is ran, the API documentation and manual testing can be viewed
at http://localhost:8888/api

python-packages:
   pip install -r requirements.txt

install: python-packages

tests:
   pytest

run:
   python DGBMICalculator/app.py

all: install tests run
