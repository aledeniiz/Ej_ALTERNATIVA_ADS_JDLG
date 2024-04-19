def calcular_descuento(cantidad_componentes, cliente):
    descuento = 0
    
    if 10000 <= cantidad_componentes <= 20000:
        descuento = 0.10
    elif 20001 <= cantidad_componentes <= 40000:
        descuento = 0.15
    elif cantidad_componentes > 40000:
        descuento = 0.20
    
    if cliente == "COMMAQ":
        descuento -= 0.02
    elif cliente == "BEL":
        descuento += 0.01
    
    return descuento

# Función principal
def main():
    cantidad_componentes = int(input("Ingrese la cantidad de componentes pedidos: "))
    cliente = input("Ingrese el nombre del cliente (COMMAQ, BEL u otro): ")
    porcentaje_descuento = calcular_descuento(cantidad_componentes, cliente)
    print("El porcentaje de descuento concedido es:", porcentaje_descuento * 100, "%")

if __name__ == "__main__":
    main()