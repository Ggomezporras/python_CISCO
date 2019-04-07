def suma (a, b):
    resultado=float(a)+float(b)
    return (resultado)

def resta (a, b):
    resultado=float(a)-float(b)
    return (resultado)

def producto (a, b):
    resultado=float(a)*float(b)
    return (resultado)

def division (a, b):
    try:
        resultado=float(a)/float(b)
        print (a,"entre",b,"es",resultado)
    except (ZeroDivisionError):
        print ("No se puede dividir por 0")
        pass


def exponencial (a, b):
    resultado=float(a)**float(b)
    return (resultado)

print ("Esta calculadora requiere insertar los valores deseados primero y despues seleccionar la operacion a realizar. Puede pulsar 0 para salir")
print ("Por favor, escriba el primer numero:")
a=input()
print ("Por favor, escriba el segundo numero:")
b=input()
print ("Elija la operacion:")
print ("1. Suma")
print ("2. Resta")
print ("3. Producto")
print ("4. División")
print ("5. Potencia")
operacion=input()

if (operacion=="1"):
    print (a,"mas",b,"es",suma(a,b))
elif (operacion=="2"):
    print (a,"menos",b,"es",resta(a,b))
elif (operacion=="3"):
    print (a,"por",b,"es",producto(a,b))
elif (operacion=="4"):
    division(a,b)
elif (operacion=="5"):
    print (a,"elevado a",b,"es",exponencial(a,b))
else:
    print ("Introduzca una operacion correcta")
