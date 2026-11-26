"""Servidor local de prueba que envía la CSP de herramientas/csp.txt (como lo hará Cloudflare).
Uso: python -I herramientas/servidor_csp.py [puerto]   (por defecto 8766; solo escucha en 127.0.0.1)"""
import functools, http.server, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSP = open(os.path.join(RAIZ, 'herramientas', 'csp.txt'), encoding='utf-8').read().strip()
# En local no hay HTTPS: upgrade-insecure-requests rompería las peticiones a http://127.0.0.1
CSP = CSP.replace('; upgrade-insecure-requests', '')


class Manejador(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Security-Policy', CSP)
        super().end_headers()


puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 8766
http.server.ThreadingHTTPServer(('127.0.0.1', puerto), functools.partial(Manejador, directory=RAIZ)).serve_forever()
