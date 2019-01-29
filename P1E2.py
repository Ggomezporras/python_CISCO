# Declaración de las tres listas
strList=["Pasagarda", "Susa", "Persépolis"]
intList=[5,3,6]
varList=["Botella", 5, 5.2]

#Print de las tres listas
print (strList)
print (intList)
print (varList)

#Asignacion de los ultimos valores de cada lista a variables
lastStr = strList[-1]
lastInt = intList[-1]
lastVar = varList[-1]

#Print de un texto y la concatenacion de variables de distinto tipo
print ("No se si entiendo muy bien este apartado",lastStr, str(lastInt), str (lastVar))

#Declaración de un diccionario
peliculas ={
    "Aronofsky": "Black Swan",
    "Borges": "El Aleph"
}

#print del diccionario, sus claves y sus valores
print (peliculas)

for key in peliculas:
    print (key)

for key in peliculas:
    print (peliculas[key])
