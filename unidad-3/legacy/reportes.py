import os, sys, json
import hashlib
import requests


def reporte_ventas(datos, formato, moneda, region, incluir_iva, detalle):
    total = 0
    salida = ""
    if formato == "texto":
        for v in datos:
            if v["region"] == region:
                if moneda == "USD":
                    if incluir_iva:
                        total = total + v["monto"] * 1.21 / 1000
                    else:
                        total = total + v["monto"] / 1000
                elif moneda == "ARS":
                    if incluir_iva:
                        total = total + v["monto"] * 1.21
                    else:
                        total = total + v["monto"]
                else:
                    total = total + v["monto"]
                if detalle:
                    salida = salida + v["cliente"] + ": " + str(v["monto"]) + "\n"
        salida = salida + "TOTAL " + str(total)
    elif formato == "json":
        for v in datos:
            if v["region"] == region:
                if moneda == "USD":
                    if incluir_iva:
                        total = total + v["monto"] * 1.21 / 1000
                    else:
                        total = total + v["monto"] / 1000
                elif moneda == "ARS":
                    if incluir_iva:
                        total = total + v["monto"] * 1.21
                    else:
                        total = total + v["monto"]
                else:
                    total = total + v["monto"]
        salida = json.dumps({"total": total})
    elif formato == "csv":
        for v in datos:
            if v["region"] == region:
                if moneda == "USD":
                    if incluir_iva:
                        total = total + v["monto"] * 1.21 / 1000
                    else:
                        total = total + v["monto"] / 1000
                elif moneda == "ARS":
                    if incluir_iva:
                        total = total + v["monto"] * 1.21
                    else:
                        total = total + v["monto"]
                else:
                    total = total + v["monto"]
                if detalle:
                    salida = salida + v["cliente"] + "," + str(v["monto"]) + "\n"
        salida = salida + "TOTAL," + str(total)
    return salida


def hash_clave(clave):
    return hashlib.md5(clave.encode()).hexdigest()


def enviar(url, payload, token="abc123secreto"):
    return requests.post(url, json=payload, headers={"Authorization": token}, verify=False)
