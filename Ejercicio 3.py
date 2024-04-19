def calcular_descuento(importe_compra):
    if 100 <= importe_compra <= 500:
        descuento = importe_compra * 0.05
    else:
        descuento = importe_compra * 0.08
    return descuento

importe_compra = float(input("Ingrese el importe de la compra: "))
descuento = calcular_descuento(importe_compra)
print("El importe del descuento es:", descuento)