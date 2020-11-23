# dec_task
Deployed:
https://dec-task.herokuapp.com

Installation Instructions:

1. Clone the project.
git clone git@github.com:tarp20/dec_task.git

2. cd intro the project directory

cd dec_task

3.Create a new virtual environment using Python 3.9 and activate it.

$ python3 -m venv env
$ source env/bin/activate

4.Install dependencies from requirements.txt:
(env)$ pip install -r requirements.txt

5.Migrate the database.
(env)$ python manage.py migrate

6.Run the local server via:
(env)$ python manage.py runserver

DONE!
The local application will be available at http://localhost:8000, and the browsable api will be available at http://localhost:8000/api/movies


Install Postgres Database:

1.Make sure that everything is working properly by entering postgres's command line interface with psql postgres. You should see you enter a shell that looks like postgres=#
2.Once in the interface, create a new database named movies with the command CREATE DATABASE movies; If creating the database succeeds, you will see the response CREATE DATABASE. 
3.For anyone to connect and access the database we created, they need a valid postgres username and password combination. This means that we need to create a dedicated user for django to interact with our new database. We create it with CREATE USER dec_task WITH PASSWORD 'dec_task';
4.Our new postgres user needs explicit permission to have read and write capabilities on our newly created database. We can do that with the command GRANT ALL PRIVILEGES ON DATABASE "movies" to dec_task; 
exit postgres



Functionality of the application:


​POST api/movies:
Download movie data from external api and save it in database.
Required json body fields: 
title
additionally
year

GET api/movies:
Display all movies in database
DELETE api/movies/<movie-id>/:
Delete movie

UPDATE api/movies/<movie-id>/:
Update Movie
Json body should contain field names and values which supposed to be updated

POST api/comments:
Create comment attached to movie
Json body requires body and movie_id fields.

GET api/comments:
Show all created comments or only comments attached to specific movie

GET api/movies/top:
Show movie ranking based on number of comments
and comments quantity for each movie
Required query params date_from, date_to
