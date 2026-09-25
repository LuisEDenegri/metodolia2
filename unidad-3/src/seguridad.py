"""Hash de claves y envio autenticado (reemplazo seguro del codigo legacy)."""

import hashlib
import hmac
import os

import requests

ITERACIONES = 240_000
TIMEOUT_SEGUNDOS = 10


def hash_clave(clave, sal=None):
    """Devuelve (sal, hash) usando PBKDF2-HMAC-SHA256 con sal aleatoria."""
    sal = sal or os.urandom(16)
    derivado = hashlib.pbkdf2_hmac("sha256", clave.encode(), sal, ITERACIONES)
    return sal, derivado


def verificar_clave(clave, sal, esperado):
    _, derivado = hash_clave(clave, sal)
    return hmac.compare_digest(derivado, esperado)


def enviar(url, payload, sesion=requests):
    """Envia un POST con el token tomado de la variable de entorno API_TOKEN."""
    token = os.environ.get("API_TOKEN")
    if not token:
        raise RuntimeError("Falta la variable de entorno API_TOKEN")
    return sesion.post(
        url,
        json=payload,
        headers={"Authorization": f"Bearer {token}"},
        timeout=TIMEOUT_SEGUNDOS,
    )
