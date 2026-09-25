"""Procesamiento de pagos contra una pasarela externa."""

import logging

logger = logging.getLogger(__name__)


class PagoRechazado(Exception):
    pass


def procesar_pago(gateway, pedido_id, monto, tarjeta_token):
    """Cobra un pedido usando la pasarela y registra el resultado.

    Si la pasarela no responde con estado "aprobado" se lanza PagoRechazado.
    Ante un timeout se reintenta una sola vez.
    """
    try:
        respuesta = gateway.cobrar(tarjeta_token, monto, referencia=pedido_id)
    except TimeoutError:
        logger.warning("Timeout en pedido %s, reintentando", pedido_id)
        respuesta = gateway.cobrar(tarjeta_token, monto, referencia=pedido_id)

    if respuesta["estado"] != "aprobado":
        raise PagoRechazado(respuesta.get("motivo", "sin motivo"))

    logger.info("Pedido %s cobrado", pedido_id)
    return respuesta["id_transaccion"]
