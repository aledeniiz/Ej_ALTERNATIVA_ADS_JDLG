def calcular_coste_viaje(cantidad_alumnos, cantidad_dias):
    # Coste del trayecto por alumno
    if cantidad_alumnos <= 25:
        coste_trayecto_por_alumno = 67.30
    else:
        coste_trayecto_por_alumno = 61.00
    
    # Coste de la comida por alumno por día
    coste_comida_por_alumno_por_dia = 3.50
    
    # Coste del alojamiento por alumno por día
    if cantidad_alumnos < 30:
        coste_alojamiento_por_alumno_por_dia = 4.75
    elif 30 <= cantidad_alumnos <= 35:
        coste_alojamiento_por_alumno_por_dia = 4.00
    else:
        coste_alojamiento_por_alumno_por_dia = 3.50
    
    # Coste total de comida del viaje
    coste_comida_viaje_por_alumno = coste_comida_por_alumno_por_dia * cantidad_dias

    # Coste total alojamiento 
    coste_total_alojamiento = coste_alojamiento_por_alumno_por_dia * cantidad_dias

    # Coste total del viaje por alumno
    coste_total_viaje_por_alumno = coste_comida_viaje_por_alumno + coste_trayecto_por_alumno + coste_total_alojamiento
    
    # Coste global del viaje
    coste_global_viaje = coste_total_viaje_por_alumno * cantidad_alumnos
    
    return coste_total_viaje_por_alumno, coste_global_viaje

# Ejemplo
cantidad_alumnos = int(input("Introduce la cantidad de alumnos: "))
cantidad_dias = int(input("Introduce la cantidad de días: "))
coste_total_viaje_por_alumno, coste_total_viaje = calcular_coste_viaje(cantidad_alumnos, cantidad_dias)
print(f"El coste total del viaje por alumno es de {coste_total_viaje_por_alumno} € para {cantidad_dias} días.")
print(f"El coste total del viaje para {cantidad_alumnos} alumnos es de {coste_total_viaje} €.")
