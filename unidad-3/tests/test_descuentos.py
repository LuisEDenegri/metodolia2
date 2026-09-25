import pytest

from src.descuentos import calcular_descuento


def test_cliente_premium_con_10_unidades_recibe_20_por_ciento():
    # Arrange
    monto, tipo, cantidad = 5000, "premium", 10

    # Act
    resultado = calcular_descuento(monto, tipo, cantidad)

    # Assert
    assert resultado == 20


def test_cliente_premium_con_monto_alto_recibe_30_por_ciento():
    # Arrange
    monto, tipo, cantidad = 15000, "premium", 12

    # Act
    resultado = calcular_descuento(monto, tipo, cantidad)

    # Assert
    assert resultado == 30


def test_cliente_premium_con_pocas_unidades_no_recibe_descuento():
    # Arrange
    monto, tipo, cantidad = 5000, "premium", 3

    # Act
    resultado = calcular_descuento(monto, tipo, cantidad)

    # Assert
    assert resultado == 0


def test_cliente_regular_con_10_unidades_recibe_10_por_ciento():
    # Arrange
    monto, tipo, cantidad = 2000, "regular", 10

    # Act
    resultado = calcular_descuento(monto, tipo, cantidad)

    # Assert
    assert resultado == 10


def test_cliente_regular_con_pocas_unidades_no_recibe_descuento():
    # Arrange
    monto, tipo, cantidad = 2000, "regular", 9

    # Act
    resultado = calcular_descuento(monto, tipo, cantidad)

    # Assert
    assert resultado == 0


def test_tipo_de_cliente_desconocido_no_recibe_descuento():
    # Arrange
    monto, tipo, cantidad = 2000, "invitado", 50

    # Act
    resultado = calcular_descuento(monto, tipo, cantidad)

    # Assert
    assert resultado == 0


@pytest.mark.parametrize("monto", [0, -100])
def test_monto_no_positivo_lanza_error(monto):
    # Arrange
    tipo, cantidad = "regular", 1

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_descuento(monto, tipo, cantidad)
