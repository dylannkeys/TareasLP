#IMPORTAMOS LAS LIBRERIAS CON LAS QUE VAMOS A TRABAJAR EN LA ELABORACION DEL GENERADOR DE CONTRASEÑAS

import random
import string
import sys
import subprocess

#AGREGAMOS LA OPCION DE "S" PARA CONTINUAR Y "N" PARA TERMIANAR EL PROCESO (EN EL CASO DE QUE NUESTRA OPCION SEA "S" VOLVEREMOS A REPRTIR TODO EL PROCESO)

def ns(r):
    while r!="n" and r!="s":
        r=input("Escriba solo \'n\' o \'s\' según su opción: ")
    return r

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

#EN EL DADO CASO DE QUE SE DIGITE UNA LETRA DIFERENTE A LA PEDIDA TENDREMOS UN BUCLE DEL SIGUIENTE MENSAJE

def opt(o,l):
    while o not in l:
        o=input("Escriba solo una de las opciónes posibles: ")
    return o

ops=sys.platform

#ABRIMOS EL BUCLE QUE VA A CONTENER LA CANTIDAD DE MINUSCULAS, MAYUSCULAS Y NUMEROS QUE VAMOS APODER ELEGIR 

while True:
    print("*******GENERADOR DE CONTRASEÑAS*******")
    minus=OKI(input("Indique número mínimo de minusculas: "))
    mayus=OKI(input("Indique número mínimo de mayusculas: "))
    numeros=OKI(input("Indique número mínimo de caracteres numéricos: "))
    longitud=OKI(input("Indique longitud de la contraseña: "))
    suma=minus+mayus+numeros #SUMA DE MINIMOS
    while longitud<suma: #COMPROBACION ADECUACIÓN DE LA "longitud".
        longitud=OKI(input("Longitud inadecuada: "))
    caract=string.ascii_letters+string.digits
    while True:
        contra=("").join(random.choice(caract)for i in range(longitud))
        if(sum(c.islower() for c in contra)>=minus
            and sum(c.isupper() for c in contra)>=mayus
            and sum(c.isdigit() for c in contra)>=numeros):
            break

#CERRAMOS EL BUCLE