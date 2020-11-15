# Interview scheduler Django Rest framework

## Introduction

Scheduling interviews is a burden in most of the companies. When you want to schedule multiple interviews in a single day, It depends on the availability of the interviewer and candidate. This application help user to register their interview slot and the interviewer can get the available time slots 


## To run the application

make sure that doker and python are installed on your system and correctly configured to run this application.
run `docker-compose up --build` to rebuild and run the application

## Create super user

run `docker-compose run app sh -c "python manage.py createsuperuser"` and login -> http://127.0.0.1:8000/admin/
