import json
import os
import urllib.request
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

OLLAMA = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return
        try:
            n = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(n)
            req = urllib.request.Request(
                OLLAMA + "/api/chat",
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=600) as r:
                data = r.read()
                self.send_response(r.status)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            payload = json.dumps({"error": str(e)}, ensure_ascii=False).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(payload)

    def do_GET(self):
        if self.path == "/api/tags":
            try:
                with urllib.request.urlopen(OLLAMA + "/api/tags", timeout=10) as r:
                    data = r.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                payload = json.dumps({"error": str(e)}, ensure_ascii=False).encode()
                self.send_response(503)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(payload)
            return
        super().do_GET()

os.chdir(ROOT)
print("IA LIVRE local: http://127.0.0.1:8765")
print("Ollama:", OLLAMA)
ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
