#!/usr/bin/env python3
"""
Servidor local simple para la Congregación Valle Hermoso
Ejecutar con: python server.py
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

# Cambiar al directorio del proyecto
os.chdir(Path(__file__).parent)

print("=" * 60)
print("🙏 Servidor local - Congregación Valle Hermoso")
print("=" * 60)
print(f"✅ Servidor iniciado en: http://localhost:{PORT}")
print(f"📁 Sirviendo desde: {os.getcwd()}")
print("\n💡 Abre tu navegador en: http://localhost:8000")
print("\n⚠️  Presiona CTRL+C para detener el servidor")
print("=" * 60 + "\n")

# Intentar abrir en el navegador automáticamente
try:
    webbrowser.open(f'http://localhost:{PORT}')
except:
    pass

try:
    with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n❌ Servidor detenido.")
