def sucesor(dia):
    if dia == "Lunes":
        return "Martes"
    elif dia == "Martes":
        return "Miércoles"
    elif dia == "Miércoles":
        return "Jueves"
    elif dia == "Jueves":
        return "Viernes"
    elif dia == "Viernes":
        return "Sábado"
    elif dia == "Sábado":
        return "Domingo"
    elif dia == "Domingo":
        return "Lunes"
    else:
        return "Día no válido"

# Input del día
dia_actual = input("Introduce un día de la semana: ")

# Llamada a la función sucesor y print del resultado
print("El día siguiente a", dia_actual, "es", sucesor(dia_actual))
