from unittest.mock import Mock

import pytest

from src.pagos import PagoRechazado, procesar_pago


class GatewayStub:
    """Stub: devuelve una respuesta fija, no verifica como se lo llama."""

    def __init__(self, respuesta):
        self.respuesta = respuesta

    def cobrar(self, token, monto, referencia):
        return self.respuesta


def test_pago_aprobado_devuelve_id_de_transaccion():
    gateway = GatewayStub({"estado": "aprobado", "id_transaccion": "TX-1"})

    assert procesar_pago(gateway, 7, 1500, "tok") == "TX-1"


def test_pago_rechazado_lanza_excepcion_con_motivo():
    gateway = GatewayStub({"estado": "rechazado", "motivo": "fondos"})

    with pytest.raises(PagoRechazado, match="fondos"):
        procesar_pago(gateway, 7, 1500, "tok")


def test_mock_verifica_protocolo_de_cobro():
    gateway = Mock()
    gateway.cobrar.return_value = {"estado": "aprobado", "id_transaccion": "TX-2"}

    procesar_pago(gateway, 9, 800, "tok-abc")

    gateway.cobrar.assert_called_once_with("tok-abc", 800, referencia=9)


def test_timeout_reintenta_una_sola_vez():
    gateway = Mock()
    gateway.cobrar.side_effect = [
        TimeoutError(),
        {"estado": "aprobado", "id_transaccion": "TX-3"},
    ]

    assert procesar_pago(gateway, 10, 500, "tok") == "TX-3"
    assert gateway.cobrar.call_count == 2
