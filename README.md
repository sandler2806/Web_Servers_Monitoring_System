﻿# Web_Servers_Monitoring_System
 
In this project I supported all the required functions as:

1. Ability to add / edit / delete / list webservers.



2. Development of automated worker that will monitor the webservers status:
       
        a. Each webserver should be sampled at least 1 time per minute.
        b. Webserver success status is determined by two factors: (AND)
              i. Getting HTTP Response Code 2xx
              ii. HTTP Response Latency < 60 seconds
        c. Every monitor request should be saved in a dedicated requests table for later use (History)
        d. Server is defined as “Healthy” in case 5 consecutive requests are considered “Success” as defined above
        e. Server is defined as “Unhealthy” in case 3 consecutive requests aren’t considered “Success” as defined above


3. Development of a REST API including the following endpoints:
       
        a. Create Webserver – Endpoint that will allow creating a new Web Server
        b. Read (Get) Webserver – Should include all basic webserver details, current health status and last 10 requests objects
        c. Update Webserver – Endpoint that will allow updating Web Server
        d. Delete Webserver – Endpoint that will allow deleting Web Server
        e. Get list of all Web Servers and their current health-status
        f. Get list of a specific webserver requests history
        
<h3> How To Run: </h3> 



1. Install the needed packages:
       
        a. mysql.
        b. requests.

2. Create a database in mysql with the name "Monolith" and the username and the password will be "root".
3. Run first the AutomatedWorker.py file by writing in the terminal "python AutomatedWorker.py".
4. Now you can control the server in the main file through the API.
        
