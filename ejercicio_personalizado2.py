entry_message = """Aquí ingresarás un valor inicial y después podrás usar los operadores para sumar, restar y demás con él
Usa los operadores + - * / respectivamente, cuando quieras salir escribe salir cuando te pida el operador."""
print(entry_message)

n = None

while True:
    if n == None:
        n = float(input("Ingresa un número: "))

    n1 = float(input("Ingresa un número: "))
    op = input("Ingresa un operador: ")
    
    resultado_sum = n + n1
    resultado_res = n - n1
    resultado_mul = n * n1
    resultado_div = n / n1
    
    if op == "+":
        print(f"La suma de {n} y {n1} es: {resultado_sum}")
        resultado_sum = n
                    
    elif op == "-":
        print(f"La resta de {n} y {n1} es: {resultado_res}")
        resultado_res = n
                    
    elif op == "*":
        print(f"La multiplicación de {n} y {n1} es: {resultado_mul}")
        resultado_mul = n
                    
    elif op == "/":
        print(f"La división de {n} y {n1} es: {resultado_div}")
        resultado_div = n
        
    elif op.lower() == "salir":
        print("Calculo finalizado")
        break
    
    else:
        print("No entendí lo escribiste, asegúrate de escribirlo correctamente.")