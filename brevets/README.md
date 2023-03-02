# Brevets

Author: Sewon Sohn\
Contact: ssohn@uoregon.edu

## Application 
On the web page showing ACP Brevet Times, Select the brevet distance and set the beginning date and time.\
Then in the table below, put in checkpoints from 0 to the brevet distance (or up to 20% beyond).\
These users inputs are taken by AJAX in the template and passed into a function in the python Flask (`flask_brevets.py`),
which passes the data as parameters into functions called from `acp_times.py`.\
The functions `open_time` and `close_time` are called, which calculate the open and close times of the checkpoint specified as a parameter.\
The functions each return an arrow object of the open/close time, which is converted to JSON data that is sent back to the AJAX. 
The times are displayed in the designated format in the table.\
When the user increments or decrements the control distance, the input values will change, hence the times displayed will as well.
