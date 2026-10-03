from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs

class ChatHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/say":

            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length)

            message = parse_qs(data.decode())["message"][0]

            print(f"Message received: {message}")

            self.send_response(200)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8080), ChatHandler)

print("ChatChafa running on port 8080")

server.serve_forever()

#HOST = "0.0.0.0"
#PORT = 8080

#server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

#print(f"ChatChafa running at http://{HOST}:{PORT}")

#server.serve_forever()
