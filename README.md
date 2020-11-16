# Interview scheduler Using Django Rest framework

## Introduction

Scheduling interviews is a burden in most of the companies. When you want to schedule multiple interviews in a single day, It depends on the availability of the interviewer and candidate. This application help user to register their interview slot and the interviewer can get the available time slots 


## To run the application

make sure that docker and python are installed on your system and correctly configured to run this application.

run `docker-compose up --build` to rebuild and run the application

### Create a superuser

run `docker-compose run app sh -c "python manage.py createsuperuser"` 

log in to `http://127.0.0.1:8000/admin/` 

## API List
1. create/update/delete interviewer or candidate `http://127.0.0.1:8000/api/user`  
2. create/update/delete interview slot `http://127.0.0.1:8000/api/interview-slots`
3. List spefic interview slots `http://127.0.0.1:8000/api/active-slots?interviewer_id=1&candidate_id=2`

### Create interview slots

##### Avilable slot choices

10AM-11AM, 11AM-12PM, 12PM-1PM, 1PM-2PM, 2PM-3PM, 3PM-4PM, 4PM-5PM, 5PM-6PM

##### Date format 

Year-Month-Date , ex: 2020-12-2


## API Documentation

##### postman collection    

`https://github.com/arjunsunil/interview-scheduler-api/blob/main/interview-scheduler-api_postman_collection.json`

##### swagger

`http://127.0.0.1:8000/api/swagger/`
