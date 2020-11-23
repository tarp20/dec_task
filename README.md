# dec_task
Deployed:
https://dec-task.herokuapp.com
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

GET /comments:
Show all created comments or only comments attached to specific movie

GET movies/top:
Show movie ranking based on number of comments
and comments quantity for each movie
Required query params date_from, date_to
