def calcular_prima_anual(kilometros_recorridos, años_antiguedad, cantidad_accidentes, responsabilidad_accidentes):
    # Calcular la prima de distancia
    prima_distancia = min(kilometros_recorridos * 0.01, 400)  # Máximo de 400€
    
    # Determinar si el conductor es elegible para la prima de antigüedad
    if años_antiguedad >= 4:
        prima_antiguedad = 200 + (años_antiguedad - 4) * 20
    else:
        prima_antiguedad = 0
    
    # Determinar la prima según los accidentes y la responsabilidad
    if cantidad_accidentes == 0 or (responsabilidad_accidentes / cantidad_accidentes) < 0.20:
        prima_final = prima_distancia + prima_antiguedad
    elif cantidad_accidentes == 1:
        prima_final = (prima_distancia + prima_antiguedad) / 2
    elif cantidad_accidentes == 2:
        prima_final = (prima_distancia + prima_antiguedad) / 3
    elif cantidad_accidentes == 3:
        prima_final = (prima_distancia + prima_antiguedad) / 4
    else:
        prima_final = 0  # Prima anulada si hay más de tres accidentes
    
    return prima_final

# Ejemplo
kilometros_recorridos = float(input("Introduce los kilómetros recorridos durante el año: "))
años_antiguedad = int(input("Introduce los años de antigüedad del conductor: "))
cantidad_accidentes = int(input("Introduce la cantidad de accidentes del conductor: "))
responsabilidad_accidentes = float(input("Introduce la responsabilidad total en los accidentes del conductor: "))

prima_anual = calcular_prima_anual(kilometros_recorridos, años_antiguedad, cantidad_accidentes, responsabilidad_accidentes)
print(f"La prima anual que se concederá al conductor es de {prima_anual:.2f} €.")
