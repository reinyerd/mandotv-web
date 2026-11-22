#!/usr/bin/env python3
"""Envía las URL de mandotv.app al servicio IndexNow (Bing, Yandex, Seznam, Naver) para indexación rápida.

Uso:
  python -I herramientas/indexnow.py              Lee sitemap.xml y envía todas las URL.
  python -I herramientas/indexnow.py --urls U1 ... Envía solo las URL indicadas.
  python -I herramientas/indexnow.py --simular     Imprime cuántas URL se enviarían y el JSON, sin enviar.
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


# Constantes del protocolo IndexNow
INDEXNOW_API = "https://api.indexnow.org/indexnow"
DOMINIO = "mandotv.app"
ESQUEMA = "https://"
RAIZ = Path(__file__).resolve().parent.parent
CLAVE_ARCHIVO = RAIZ / "39669e795b27187d81b484e104572c40.txt"
MAX_URLS = 10000

# Mensajes de códigos HTTP IndexNow
MENSAJES_HTTP = dict()
MENSAJES_HTTP[200] = "Aceptado"
MENSAJES_HTTP[202] = "Aceptado (procesamiento asíncrono)"
MENSAJES_HTTP[400] = "Formato inválido"
MENSAJES_HTTP[403] = "Clave no encontrada o no coincide"
MENSAJES_HTTP[422] = "URL de otro host o clave inválida"
MENSAJES_HTTP[429] = "Demasiadas peticiones"


def leer_clave():
    """Lee y valida el archivo de clave IndexNow desde la raíz del repo."""
    if not CLAVE_ARCHIVO.exists():
        print("Error: el archivo de clave no existe en la raíz del repo.", file=sys.stderr)
        sys.exit(1)
    contenido = CLAVE_ARCHIVO.read_text(encoding="utf-8").strip()
    # IndexNow exige que el archivo publicado contenga exactamente la clave que se envía.
    if contenido != CLAVE_ARCHIVO.stem:
        print("Error: el archivo de clave no contiene la clave " + CLAVE_ARCHIVO.stem + ".", file=sys.stderr)
        sys.exit(1)
    return contenido


def leer_urls_sitemap():
    """Extrae las URLs <loc> del sitemap.xml en la raíz del repo."""
    sitemap = RAIZ / "sitemap.xml"
    if not sitemap.exists():
        print("Error: no se encontró sitemap.xml en la raíz del repo.", file=sys.stderr)
        sys.exit(1)
    tree = ET.parse(sitemap)
    root = tree.getroot()
    urls = []
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    url_tag = "{" + ns + "}url"
    loc_tag = "{" + ns + "}loc"
    for url_elem in root.findall(".//" + url_tag):
        loc_elem = url_elem.find(loc_tag)
        if loc_elem is not None and loc_elem.text:
            urls.append(loc_elem.text)
    return urls


def validar_urls(urls, clave):
    """Valida las URL antes de enviarlas. Termina con código 1 si algo falla."""
    if not urls:
        print("Error: no hay URLs para enviar.", file=sys.stderr)
        sys.exit(1)
    if len(urls) > MAX_URLS:
        msg = "Error: se enviaron " + str(len(urls)) + " URL, el máximo permitido es " + str(MAX_URLS) + "."
        print(msg, file=sys.stderr)
        sys.exit(1)
    for url in urls:
        if not url.startswith("https://mandotv.app/"):
            msg = "Error: la URL '" + url + "' no empieza con 'https://mandotv.app/'."
            print(msg, file=sys.stderr)
            sys.exit(1)


def construir_cuerpo(clave, urls):
    """Construye el cuerpo JSON del request IndexNow."""
    keyLocation = ESQUEMA + DOMINIO + "/" + CLAVE_ARCHIVO.name
    return dict(host=DOMINIO, key=clave, keyLocation=keyLocation, urlList=urls)


def enviar(urls):
    """Envía las URL al servicio IndexNow e imprime el resultado."""
    clave = leer_clave()
    validar_urls(urls, clave)
    cuerpo = construir_cuerpo(clave, urls)
    data = json.dumps(cuerpo).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_API,
        data=data,
        headers=dict([("Content-Type", "application/json; charset=utf-8")]),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            codigo = resp.status
    except urllib.error.HTTPError as e:
        codigo = e.code
    except urllib.error.URLError:
        print("Error: no se pudo conectar con el servicio IndexNow.", file=sys.stderr)
        sys.exit(1)
    mensaje = MENSAJES_HTTP.get(codigo, "Desconocido (código %d)" % codigo)
    print("Código HTTP: %d - %s" % (codigo, mensaje))
    if codigo not in (200, 202):
        sys.exit(1)


def main():
    # La consola de Windows no usa UTF-8 por defecto: sin esto las tildes salen mal.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Enviar URLs de mandotv.app al servicio IndexNow."
    )
    parser.add_argument(
        "--urls",
        nargs="+",
        help="URLs individuales a enviar (en lugar del sitemap)",
    )
    parser.add_argument(
        "--simular",
        action="store_true",
        help="Simular envío: imprime la cantidad y el JSON sin enviar nada.",
    )
    args = parser.parse_args()
    if args.urls:
        urls = args.urls
    else:
        urls = leer_urls_sitemap()
    clave = leer_clave()
    validar_urls(urls, clave)
    cuerpo = construir_cuerpo(clave, urls)
    if args.simular:
        print("Se enviarían %d URL(s):" % len(urls))
        print(json.dumps(cuerpo, indent=2, ensure_ascii=False))
        return
    enviar(urls)


if __name__ == "__main__":
    main()
