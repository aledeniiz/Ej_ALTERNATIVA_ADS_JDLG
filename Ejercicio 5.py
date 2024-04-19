def calcular_descuento(num_ninos):
    if num_ninos == 2:
        descuento = 0.10
    elif num_ninos == 3:
        descuento = 0.15
    elif num_ninos == 4:
        descuento = 0.18
    elif num_ninos >= 5:
        descuento = 0.18 + (num_ninos - 4) * 0.01
    else:
        descuento = 0
    return descuento

# Función principal
def main():
    num_ninos = int(input("Ingrese la cantidad de niños en la familia: "))
    descuento = calcular_descuento(num_ninos)
    print("El descuento al que tiene derecho la familia es:", descuento * 100, "%")

if __name__ == "__main__":
    main()