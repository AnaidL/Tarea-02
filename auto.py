#Autor: Anaid Fernanda Labat González, A01746289
#Descripción: Encontrar la velocidad de un auto y su distancia recorrida en 6 y 10 horas, al igual que su tiempo para recorrer 500 km

#A partir de aqui escribe tu programa

v= int(input("velocidad del auto en km/h:"))
t6=6
t10=10
distancia1= t6*v
distancia2=t10*v
tiempo500=500/v

print("Distancia recorrida por 6 hrs:",distancia1, "km" )
print("Distancia recorrida por 10 horas", distancia2, "km")
print("Tiempo realizado al recorrer 500 km", tiempo500,"hrs")

