"""Hello server module"""
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    """class for handler the hello"""
    def do_GET(self):
        """GET verb for http"""
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())

if __name__ == '__main__':
    SERVER_ADDRESS = ('', 8000)  # Serve on all addresses, port 8000.
    HTTPD = HTTPServer(SERVER_ADDRESS, HelloHandler)
    HTTPD.serve_forever()
