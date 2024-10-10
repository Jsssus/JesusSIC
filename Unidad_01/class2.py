## este es el último ejercicio de la guia 
import random as rd

usuario = int(input('ingresa un numero: '))
numero = rd.randint(1,100)
intentos = 0

while usuario != numero:
    if usuario < numero:
        print('intena con un numero más alto!')
    else:
         print('intenta con un numero mas bajo!')
            
    usuario = int(input('ingresa un numero: '))
    intentos += 1

print(f'adivinaste el numero {numero}')
print(f'numero de intentos {intentos}') 