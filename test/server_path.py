import http.server
import socketserver
import threading
import sys
from time import sleep
import os

PORT = 8098

web_dir = os.path.join(os.path.dirname(__file__), '/')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
# httpd.serve_forever()

server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()


while True:
    try:
        sleep(1)
        print("NON BLOCKING!")
    except KeyboardInterrupt:
        sys.exit()
