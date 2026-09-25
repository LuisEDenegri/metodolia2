"""Reporte de ventas por region (version refactorizada)."""

import json

FACTOR_USD = 1000
IVA = 1.21


def _convertir(monto, moneda, incluir_iva):
    """Aplica IVA y conversion de moneda a un monto individual."""
    if moneda not in ("USD", "ARS"):
        return monto
    if incluir_iva:
        monto = monto * IVA
    if moneda == "USD":
        monto = monto / FACTOR_USD
    return monto


def _filtrar(datos, region):
    return [v for v in datos if v["region"] == region]


def _render_lineas(ventas, total, detalle, separador):
    lineas = []
    if detalle:
        lineas = [f"{v['cliente']}{separador}{v['monto']}" for v in ventas]
    lineas.append(f"TOTAL{separador}{total}")
    return "\n".join(lineas)


def _render_texto(ventas, total, detalle):
    return _render_lineas(ventas, total, detalle, ": ").replace("TOTAL: ", "TOTAL ")


def _render_csv(ventas, total, detalle):
    return _render_lineas(ventas, total, detalle, ",")


def _render_json(ventas, total, detalle):
    return json.dumps({"total": total})


RENDERIZADORES = {
    "texto": _render_texto,
    "csv": _render_csv,
    "json": _render_json,
}


def reporte_ventas(datos, formato, moneda, region, incluir_iva, detalle):
    if formato not in RENDERIZADORES:
        raise ValueError(f"Formato no soportado: {formato}")
    ventas = _filtrar(datos, region)
    total = sum(_convertir(v["monto"], moneda, incluir_iva) for v in ventas)
    return RENDERIZADORES[formato](ventas, total, detalle)
