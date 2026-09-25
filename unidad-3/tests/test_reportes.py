import itertools
import sys
from pathlib import Path

import pytest

from src.reportes import reporte_ventas

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from legacy.reportes import reporte_ventas as reporte_legacy  # noqa: E402

DATOS = [
    {"cliente": "Ana", "monto": 2000, "region": "NOA"},
    {"cliente": "Luis", "monto": 3000, "region": "NOA"},
    {"cliente": "Eva", "monto": 9000, "region": "CUYO"},
]


def test_total_en_ars_con_iva():
    resultado = reporte_ventas(DATOS, "csv", "ARS", "NOA", True, False)

    assert resultado == "TOTAL,6050.0"


def test_formato_no_soportado_lanza_error():
    with pytest.raises(ValueError):
        reporte_ventas(DATOS, "xml", "ARS", "NOA", False, False)


@pytest.mark.parametrize(
    "formato,moneda,iva,detalle",
    list(
        itertools.product(
            ["texto", "json", "csv"], ["USD", "ARS", "EUR"], [True, False], [True, False]
        )
    ),
)
def test_refactor_mantiene_comportamiento_del_legacy(formato, moneda, iva, detalle):
    esperado = reporte_legacy(DATOS, formato, moneda, "NOA", iva, detalle)

    obtenido = reporte_ventas(DATOS, formato, moneda, "NOA", iva, detalle)

    assert obtenido == esperado
