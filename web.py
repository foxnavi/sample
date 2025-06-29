import http.server
import socketserver
import webbrowser
import time

PORT = 8000

HTML_CONTENT = b"""<html><body><h1>Hello, world!</h1></body></html>"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_CONTENT)


def main() -> None:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except Exception as exc:
            print(f"Could not open browser: {exc}")
        httpd.timeout = 1
        start = time.time()
        while time.time() - start < 5:
            httpd.handle_request()
        print("Server stopped")


if __name__ == "__main__":
    main()
