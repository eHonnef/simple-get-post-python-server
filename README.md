# Simple HTTP python server

A simple python server that handles GET and POST requests.

## Usage

Just start `server.py` and then send a request using `client.py`.

## Some notes

I do not recommend to use in a real world application since it just serves as an example application and to do some homework :).  
The GET responses returns a JSON type object (yup, all of it).  
The POST returns a "OK I received your request and data" and then it writes a log to the JSON file.  
The JSON file contains a timestamp in UTC and a random message (blank for now).
