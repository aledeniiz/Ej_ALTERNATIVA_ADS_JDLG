class Alumno:
    def __init__(self, notas):
        self.notas = notas
        self.media = sum(notas) / len(notas)
        self.evaluacion = self.calcular_evaluacion()

    def calcular_evaluacion(self):
        if self.media > 15:
            return "Alumno con talento"
        elif 12 <= self.media <= 15:
            return "Con capacidad"
        else:
            return "Debe reorientarse"

# Función para ingresar las notas de un alumno
def ingresar_notas():
    notas = []
    for i in range(4):
        nota = float(input(f"Ingrese la nota {i+1} del alumno: "))
        notas.append(nota)
    return notas

# Función principal
def main():
    notas_alumno = ingresar_notas()
    alumno = Alumno(notas_alumno)
    print("La media del alumno es:", alumno.media)
    print("Evaluación del alumno:", alumno.evaluacion)

if __name__ == "__main__":
    main()