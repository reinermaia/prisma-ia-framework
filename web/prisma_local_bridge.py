# -*- coding: utf-8 -*-
"""
Bridge local HTTP para permitir que o Front-End Web do PRISMA-IA execute
o pipeline diretamente no disco e gere os arquivos fisicamente em output_v2/.
Escuta em http://127.0.0.1:8765
"""
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import run_prisma_pipeline

PORT = 8765
BASE_DIR = r"C:\Users\franc\Downloads\lixo\Bizagi Automate\Case Anne Linkedin"
OUTPUT_V2_DIR = os.path.join(BASE_DIR, "output_v2")

class PrismaBridgeHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Accept')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == '/status':
            files = os.listdir(OUTPUT_V2_DIR) if os.path.exists(OUTPUT_V2_DIR) else []
            data = {
                "status": "online",
                "output_v2_count": len(files),
                "is_clean": len(files) == 0,
                "files": files
            }
            body = json.dumps(data).encode('utf-8')
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            msg = b"PRISMA-IA Local Bridge Online"
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)

    def do_POST(self):
        if self.path == '/run':
            try:
                result = run_prisma_pipeline.execute_pipeline()
                body = json.dumps(result).encode('utf-8')
                self.send_response(200)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except Exception as e:
                err_body = json.dumps({"success": False, "error": str(e)}).encode('utf-8')
                self.send_response(500)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(err_body)))
                self.end_headers()
                self.wfile.write(err_body)
        else:
            self.send_response(404)
            self._send_cors_headers()
            self.end_headers()

    def log_message(self, format, *args):
        pass

def run_server():
    server = HTTPServer(('127.0.0.1', PORT), PrismaBridgeHandler)
    print(f"[OK] PRISMA-IA Local Bridge escutando em http://127.0.0.1:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
