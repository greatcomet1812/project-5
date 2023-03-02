# UOCIS322 - Project 5

Author: Sewon Sohn\
Contact: ssohn@uoregon.edu

This project calculates the open and close times for each specified checkpoints of the brevet given its distance and the starting time.

## Docker
Run the program with Docker Compose so that we can have multiple containers running at the same time. In this case, we want the web and database to be executing simultaneously.
```
docker compose up --build -d
```
This will let Docker Compose build anything that has not already been installed previously based on the `docker-compose.yml` file.
The `-d` flag lets the container run in detached mode, as Mongo needs to be run the background. 

To stop the docker, run the command
```
docker compose down
```

To check if there are any running containers, run the command
```
docker compose ls
```


## Application 
On the web page showing ACP Brevet Times, Select the brevet distance and set the beginning date and time.\
Then in the table below, put in checkpoints from 0 to the brevet distance (or up to 20% beyond).\
These users inputs are taken by AJAX in the template and passed into a function in the python Flask (`flask_brevets.py`),
which passes the data as parameters into functions called from `acp_times.py`.\
The functions `open_time` and `close_time` are called, which calculate the open and close times of the checkpoint specified as a parameter.\
The functions each return an arrow object of the open/close time, which is converted to JSON data that is sent back to the AJAX. 
The times are displayed in the designated format in the table.\
When the user increments or decrements the control distance, the input values will change, hence the times displayed will as well.

`mondodb.py` contains all the pymongo functions - insert and fetch. 
`brevet_insert` stores data passed in from the flask in the database, and `brevet_fetch` fetches all the data stored in the database.

In the template file (`calc.html`), when the button "Submit" is clicked, all of the data that the user put in are stored in the database and cleared from the page.
This happens as AJAX transmits all of the input data as arguments to flask. Then, flask takes the data and calls the function `brevet_insert` to store them.
When the button `Display` is clicked, the server brings back all the data that have been saved. This is done by calling the function `brevet_fetch` from flask, which fetches all data stored from the database and jonsifies them back to the template. 
These data then populate the table in the corresponing fields. 