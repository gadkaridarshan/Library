# Library App

Built by Darshan Gadkari

Requirements:
You are required to build the backend of a web app that handles book loans for a small local library. As part of the 
exercise, you will need to setup and populate a database and create an API that meets the criteria outlined below. The 
API needs to be built using Python with SQLite used for the database. You are recommended to spend around 5 hours on 
the assessment. Submissions that do not implement all the functionality will still be accepted so be sure to adhere to 
best practices during development.
You have been provided with a CSV file containing the initial book inventory data and should design the table 
structure as you see appropriate.

The API requires endpoints that allow the library staff to perform the following operations: 

For Library Website Users:
a. An endpoint that allows the database searching by title and by author, returning books and their availability.
b. Add/remove unavailable books to/from a wishlist such that they are notified when they become available

For Library Staff:
c. Change the rental status (available/borrowed) for a book (which should also trigger the email notifications to 
users with the book in their wishlist)
d. Generate a report on the number of books being rented and how many days they’ve been rented for.
e. The frontend of the library website displays affiliate links to copies of the book available on Amazon for each 
book. The Amazon book IDs can be retrieved from the OpenLibrary API (no developer key required). An endpoint is 
required that will update the Amazon IDs stored in the database for all the books.

The function in endpoint (c) that requires emails to be sent out should be implemented by printing the email text 
to the output or logging to a file.

To submit your assessment, return a zip file via email with all the files as necessary. Please include your source 
code, database and any other relevant files (e.g. shell scripts, config files, etc.). Also include brief documentation 
that lists the endpoint URL, HTTP method and data to be submitted to the endpoint for each of the tasks above.

App:
1. Satisfies the above 5 requirements
2. App is implemented using Flask Restplus, Blueprints
3. Blueprints help separate out the functionality for the Users and the Staff
4. The models are kept as common because they are shared between Users and the Staff
5. The documentation and manual testing is accessible using swagger
6. Test cases are written using pytest and all run successfully
7. The test cases cover all the functionalities except for Loading Data from csv and retrieving Amazon Ids
8. All the required functionalities are implemented and run successfully
9. The code can be dockerized for use in docker-compose or kubernetes environment
10. Further automation to be used in deployment pipeline can be done
11. is a solid production-grade Python3 Program
12. is a stand-alone backend application
13. github url: https://github.com/gadkaridarshan/Library
14. Code is linted using pydocstyle
15. Code built using Flask Blueprints for good code structuring
16. Code built using Flask-restplus to build REST APIs using best practices and minimal setup
17. setup.py provided for code packaging
18. When code is ran, the API documentation and manual testing can be viewed
at http://localhost:8888/api
19. Migration has been built but not fully tested
20. venv is used for packaging the python libraries

![alt text](https://github.com/gadkaridarshan/Library/blob/main/LibraryAPIDocumentation.png)

python-packages:
   pip install -r requirements.txt

install: python-packages

tests:
   pytest

run:
   python Library/app.py

