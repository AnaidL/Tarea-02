#Autor: Anaid Fernanda Labat González, A01746289
#Descripción: Transformar de coordenadas rectangulares a polares

#A partir de aqui escribe tu programa

x= int(input("Valor de x:"))
y= int(input("Valor de y:"))

import math
r=(((x**2)+(y**2))**1/2)
magnitud= math.atan2(y,x)
angulo=(magnitud*180)/3.1416

print("Magnitud:", r)
print("Ángulo:" ,angulo,"°")