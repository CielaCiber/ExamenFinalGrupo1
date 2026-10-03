def validar_datos(a, b, c, d, A, B, C, D):
    errores = []

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        errores.append("Error: los lados deben ser valores positivos.")

    if (A <= 0 or B <= 0 or C <= 0 or D <= 0 or
            A >= 180 or B >= 180 or C >= 180 or D >= 180):
        errores.append("Error: cada angulo debe estar entre 0 y 180 grados.")

    if (A + B + C + D) != 360:
        errores.append("Error: la suma de los angulos internos debe ser 360 grados.")

    if (a >= b + c + d or b >= a + c + d or
            c >= a + b + d or d >= a + b + c):
        errores.append("Error: cada lado debe ser menor que la suma de los otros tres.")

    return len(errores) == 0, errores


def clasificar_cuadrilatero(a, b, c, d, A, B, C, D):
    lados_todos_iguales = (a == b == c == d)
    lados_opuestos_iguales = (a == c) and (b == d) and (a != b)
    angulos_todos_rectos = (A == 90 and B == 90 and C == 90 and D == 90)
    angulos_opuestos_iguales = (A == C) and (B == D)
    tiene_lados_paralelos = (A + D == 180) or (A + B == 180)

    if lados_todos_iguales and angulos_todos_rectos:
        return "CUADRADO", "Tiene los 4 lados iguales y los 4 ángulos son rectos (90°)."
    elif lados_opuestos_iguales and angulos_todos_rectos:
        return "RECTANGULO", "Sus lados opuestos son iguales y los 4 ángulos son rectos, pero los lados adyacentes son distintos."
    elif lados_todos_iguales and not angulos_todos_rectos:
        return "ROMBO", "Tiene los 4 lados iguales, pero sus ángulos no son rectos."
    elif lados_opuestos_iguales and angulos_opuestos_iguales and A != 90:
        return "ROMBOIDE", "Sus lados opuestos son iguales entre sí y sus ángulos opuestos también, pero ninguno es recto."
    elif tiene_lados_paralelos:
        return "TRAPECIO", "No cumple las condiciones de cuadrado, rectángulo, rombo ni romboide, y tiene un par de lados paralelos."
    else:
        return "NINGUNA DE LAS 5 FIGURAS", "No tiene lados paralelos,  no es trapecio."


# --- Programa principal ---
def main():
    while True:
        print("=== Clasificador de Cuadrilateros ===")
        a = float(input("Ingrese la longitud del lado a: "))
        b = float(input("Ingrese la longitud del lado b: "))
        c = float(input("Ingrese la longitud del lado c: "))
        d = float(input("Ingrese la longitud del lado d: "))
        A = float(input("Ingrese el angulo A (grados): "))
        B = float(input("Ingrese el angulo B (grados): "))
        C = float(input("Ingrese el angulo C (grados): "))
        D = float(input("Ingrese el angulo D (grados): "))

        validos, errores = validar_datos(a, b, c, d, A, B, C, D)

        if validos:
            resultado, explicacion = clasificar_cuadrilatero(a, b, c, d, A, B, C, D)
            print("Resultado:", resultado)
            print("Explicacion:", explicacion)
        else:
            for error in errores:
                print(error)

        respuesta = input("¿Desea clasificar otra figura? (S/N): ")
        if respuesta.lower() == "n":
            break

    print("muchas gracias por usar el programa. ¡Hasta luego!")


if __name__ == "__main__":
    main()
