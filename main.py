import sumar
import resta
import multiplicacion
import division
import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("6. Salir")

while True:
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar.sumar(num1, num2)
        print("El resultado es:", resultado)
    # ... (resto de las opciones)
    elif opcion == 6:
        break