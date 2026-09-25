"""Calculo de descuentos para pedidos de la tienda."""


def calcular_descuento(monto, tipo_cliente, cantidad):
    """Devuelve el porcentaje de descuento (0 a 30) para un pedido.

    Reglas:
    - Montos negativos o cero no son validos.
    - Clientes "premium" con 10 o mas unidades reciben 20%; si el monto
      supera 10000 reciben 30%.
    - Clientes "regular" con 10 o mas unidades reciben 10%.
    - Cualquier otro caso no recibe descuento.
    """
    if monto <= 0:
        raise ValueError("El monto debe ser mayor a cero")

    descuento = 0
    if tipo_cliente == "premium":
        if cantidad >= 10:
            descuento = 20
            if monto > 10000:
                descuento = 30
    elif tipo_cliente == "regular":
        if cantidad >= 10:
            descuento = 10
    return descuento
