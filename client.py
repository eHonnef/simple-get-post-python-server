import urllib, http.client

# Connecting to server
c = http.client.HTTPConnection("localhost", 8000)

# GET request
c.request("GET", "token=xD")
doc = c.getresponse().read()
print(doc)

# POST request
c.request("POST", "", ":)")
doc = c.getresponse().read()
print(doc)
