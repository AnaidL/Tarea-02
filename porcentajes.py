#Autor: Anaid Fernanda Labat González, A01746289
#Descripción: Dar a conocer el porcentaje de hombres y mujeres según el número de alumnos inscritos

#A partir de aqui escribe tu programa

AlumnosInscritos = int(input("Total de Alumnos Inscritos:"))
Mujeres=AlumnosInscritos/4
Hombres=(3*(AlumnosInscritos/4))
PorcentajeMujeres=((Mujeres*100)/AlumnosInscritos)
PorcentajeHombres= ((Hombres*100/AlumnosInscritos))

print("Número de Mujeres", Mujeres)
print("Número de Hombres:", Hombres)
print("Porcentaje de Mujeres: ", PorcentajeMujeres, "%")
print("Porcentaje de Hombres:", PorcentajeHombres, "%")