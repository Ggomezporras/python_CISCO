def suma (a, b):
    try:
        resultado=float(a)+float(b)
        print (a,"más",b,"es",resultado)
    except(ValueError):
        print ("Por favor, introduzca valores numericos enteros o decimales")

def resta (a, b):
    try:
        resultado=float(a)-float(b)
        print (a,"menos",b,"es",resultado)
    except(ValueError):
        print ("Por favor, introduzca valores numericos enteros o decimales")

def producto (a, b):
    try:
        resultado=float(a)*float(b)
        print (a,"por",b,"es",resultado)
    except(ValueError):
        print ("Por favor, introduzca valores numericos enteros o decimales")

def division (a, b):
    try:
        resultado=float(a)/float(b)
        print (a,"entre",b,"es",resultado)
    except (ZeroDivisionError):
        print ("No se puede dividir por 0")
        pass
    except (ValueError):
        print ("Por favor, introduzca valores numericos enteros o decimales")


def exponencial (a, b):
    try:
        resultado=float(a)**float(b)
        print (a,"elevado a",b,"es",resultado)
    except(ValueError):
        print ("Por favor, introduzca valores numericos enteros o decimales")
        
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
    suma(a,b)
elif (operacion=="2"):
    resta(a,b)
elif (operacion=="3"):
    producto(a,b)
elif (operacion=="4"):
    division(a,b)
elif (operacion=="5"):
    exponencial(a,b)
else:
    print ("Introduzca una operacion correcta")
