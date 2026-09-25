from unittest.mock import Mock

import pytest

from src.seguridad import enviar, hash_clave, verificar_clave


def test_clave_correcta_se_verifica():
    sal, digest = hash_clave("secreta")

    assert verificar_clave("secreta", sal, digest)


def test_clave_incorrecta_no_se_verifica():
    sal, digest = hash_clave("secreta")

    assert not verificar_clave("otra", sal, digest)


def test_misma_clave_genera_hashes_distintos_por_la_sal():
    assert hash_clave("secreta")[1] != hash_clave("secreta")[1]


def test_enviar_sin_token_falla(monkeypatch):
    monkeypatch.delenv("API_TOKEN", raising=False)

    with pytest.raises(RuntimeError):
        enviar("https://api.test/x", {})


def test_enviar_usa_token_y_timeout(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "tok123")
    sesion = Mock()

    enviar("https://api.test/x", {"a": 1}, sesion=sesion)

    sesion.post.assert_called_once_with(
        "https://api.test/x",
        json={"a": 1},
        headers={"Authorization": "Bearer tok123"},
        timeout=10,
    )
