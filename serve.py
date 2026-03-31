import http.server, socketserver, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8789
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.js'] = 'application/javascript'

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
