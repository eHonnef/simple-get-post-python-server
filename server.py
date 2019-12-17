from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
import urllib.parse
import time


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

  def _set_headers(self):
    self.send_response(200)
    # Set the header as a json type and using utf-8 enconding
    self.send_header("Content-type", "application/json; charset=utf-8")
    self.end_headers()

  def do_HEAD(self):
    self._set_headers()

  def do_GET(self):
    self._set_headers()
    # parsed = urllib.parse.urlparse(self.path)
    # Parse the URL to check the GET requests
    parsed = urllib.parse.parse_qs(self.path)

    # Only respond if the token request is given
    if "token" in parsed.keys():
      # And only if is the correct token
      if parsed["token"][0] == "xD":
        # open json file and then send it encoded (wfile.write wants a byte object)
        j = json.load(open("./logs.json"))
        j = json.dumps(j)
        self.wfile.write(j.encode("utf-8"))

  def do_POST(self):
    content_length = int(self.headers["Content-Length"])
    body = self.rfile.read(content_length)
    self.send_response(200)
    self.end_headers()

    # Uncomment those lines to see/send the full message
    response = BytesIO()
    # response.write(b"This is POST request. ")
    response.write(b"Request received")
    # response.write(body)

    # If the "correct" data is received (a.k.a. a token) then it'll write to the json file
    if body == b":)":
      self.log_to_json()

    # Returns a response to the sender
    self.wfile.write(response.getvalue())

  def log_to_json(self):
    # Just logging to the json file
    j = json.load(open("./logs.json"))
    j.append({"date": time.time(), "message": self.random_message()})
    json.dump(j, open("./logs.json", "w"))
    print("Logged new message")

  def random_message(self):
    # A truly "random" message
    return ""


# Keep the server alive and defines the port and the address
httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
