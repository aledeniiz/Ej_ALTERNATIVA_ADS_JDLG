def clasificar_numeros(a, b):
    a = int(a)  # Convertir la entrada a entero
    b = int(b)  # Convertir la entrada a entero

    # Calcular suma y producto
    suma = a + b
    producto = a * b
    
    # Ordenar los números y sus resultados
    numeros_ordenados = sorted([a, b, suma, producto])
    
    # Devolver el resultado en una cadena formateada
    resultado = f"{numeros_ordenados[2]} < {numeros_ordenados[0]} < {numeros_ordenados[1]} < {numeros_ordenados[3]}"
    
    return resultado

# Ejemplo
a = input("Introduce un número a: ")
b = input("Introduce un número b: ")
print(clasificar_numeros(a, b))
