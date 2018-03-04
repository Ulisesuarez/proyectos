"blablabla"
# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

print("¿Cuál es el radio de la cirunferencia en cm?")

while True:
    try:
        RADIO = float(input())
        break

    except  ValueError:
        print("Oops!  Eso no es un numero, introduce un radio en cm!")




def areaylongitud(rad):
    "esto es la documentación"
    return [round(2*math.pi*rad, 2), round(math.pi*rad**2, 2)]

RESULTADO = areaylongitud(RADIO)
FRASEFINAL = ""
FRASEFINAL = "El área del circulo es ="+str(RESULTADO[1])+" cm² y la "\
"longitud de la circunferencia ="+str(RESULTADO[0])+" cm"
print(FRASEFINAL)
