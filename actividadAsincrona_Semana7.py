print ("Buenas ingeniero, esta es la actividad asincrona de la semana 7")
print (" ")

#Enteros (Int)
print ("Datos Enteros")
#Asignación de variables
var1 = int(6)
var2 = int(3)
var3 = int(2)

#Se relizara una multiplicación con tres variables distintas
multi_resultado = var1 * var2 * var3
print (f"El resutado de la multiplicación entre {var1} * {var2} * {var3} es: {multi_resultado}")

#Se realizara una división entre dos varables distintas
division_resultado = var1 // var2
print (f"El resultado de la división entre {var1} / {var2} es: {division_resultado}")

#Se suman ambos resutados
resultado_multi_divison = multi_resultado + division_resultado
print (f"La suma entre {multi_resultado} + {division_resultado} es: {resultado_multi_divison} y su tipo es: {type (resultado_multi_divison)}")
print (" ")

#Flotante (float)
print("Datos Flotantes")
#Asignación de variables
var_float1 = float(3.5)
var_float2 = float(3.3)
var_float3 = float(3.1)

#Se elevaran dos variables
result_exponentes = var_float1 ** var_float2
print (f"El numero {var_float1} ^ {var_float2} es igual a: {result_exponentes}")

#Se les sacara el modulos a dos variables distintas
result_modulo = var_float2 % var_float3
print (f"El modulo de {var_float2} con {var_float3} es igual a : {result_modulo}")

#Se restan ambos resultados
result_expo_modu = result_exponentes - result_modulo
print (f"La resta entre {result_exponentes} - {result_modulo} es igual a: {result_expo_modu}")

#Se divide el resultado de la resta entre el resultado de la suma
div_sum_rest = resultado_multi_divison - result_expo_modu
print (f"La división entre {resultado_multi_divison} / {result_expo_modu} es de: {div_sum_rest} y su tipo es: {type (div_sum_rest)}")
print(" ")

#Complejo (complex)
print("Datos Complejos")

#Se definen cuatro variables complex
var_complex1 = complex(4, + 8j)
var_complex2 = complex(3,- 1)
var_complex3 = complex(6j)
var_complex4 = complex(8, + 2j)
print (f"La variable {var_complex1} es de tipo {type(var_complex1)}")
print (" ")

#Caracter (string o str)
print ("Datos string")
#Se definen variables para todos los integrante para almacenar una fruta por variable 
#Cada fruta pertenece a un integrante
integrante1 = str("Mango") #Pertenece a Felix
integrante2 = str("Sandia") #Pertenece a Sonia
integrante3 = str("Uva") #Pertenece a Carlos
integrante4 = str("Fresa") #Pertenece a Iván
integrante5 = str("Melón") #Pertenece a Marilyn
integrante6 = str("Papaya") #Pertenece a Alejandro
print (f"La variable {integrante1} es de tipo: {type (integrante1)}")
print (" ")

#Boolenano (bool)
print ("Datos Booleanos ")
#Se realiza una estructura if
print ("""Puedes ingresar estas frutas:
Mango
Sandia
Uva
Fresa
Melón
Papaya""")
print (" ")
fruta = str(input("Ingresa el nombre de una fruta: "))
print (" ")
bool(fruta)

if fruta == "Mango":
    print ("La fruta es", fruta, "y pertenece a Felix" )
    print (" ")
    print ("Fin de la actividad, gracias por participar :)")
    
if fruta == "Sandia":
    print ("La fruta es", fruta, "y pertenece a Sonia" )
    print (" ")
    print ("Fin de la actividad, gracias por participar :)")
   
if fruta == "Uva":
    print ("La fruta es", fruta, "y pertenece a Carlos" )
    print (" ")
    print ("Fin de la actividad, gracias por participar :)")
    
if fruta == "Fresa":
    print ("La fruta es", fruta, "y pertenece a Iván" )
    print (" ")
    print ("Fin de la actividad, gracias por participar :)")

if fruta == "Melón":
    print ("La fruta es", fruta, "y pertenece a Marilyn" )
    print (" ")
    print ("Fin de la actividad, gracias por participar :)")
    
if fruta == "Papaya":
    print ("La fruta es", fruta, "y pertenece a Alejandro" )
    print (" ")
    print ("Fin de la actividad, gracias por participar :)")