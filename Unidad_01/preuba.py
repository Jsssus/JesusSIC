umbral = - 10
lista_de_elementos = elementos = [10, 3.14, "7", -5, "2.718", 42, "Python", -8.9, "Hola", 100.5, "Mundo", -15, "GPT-3", 5.5, "AI", -20, "2023", 123, "OpenAI", -2.5, "Ejemplo"]

# Desarrollo loop del código principal.

#Iniciando los valores
aprobados = 0
rechazados = 0
conteo_strings = 0

#Rezalizando el loop

for elemento in lista_de_elementos:
     #usaremos isinstance para validar los elementos que son enteros o floats 
    if type(elemento) == str:
        conteo_strings += 1
    elif type(elemento) == int or float: 
        if elemento >= umbral:
             aprobados += 1
        else:
            rechazados += 1
        
            
print("Total aprobados:",aprobados)
print("Total rechazados:",rechazados)
print("Total de strings:",conteo_strings)