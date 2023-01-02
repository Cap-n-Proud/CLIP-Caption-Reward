import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import sys
from time import sleep

MyRequestHandler = SimpleHTTPRequestHandler

server = ThreadingHTTPServer(("0.0.0.0", 8001), MyRequestHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

while True:
    try:
        sleep(1)
        print("NON BLOCKING!")
    except KeyboardInterrupt:
        sys.exit()
