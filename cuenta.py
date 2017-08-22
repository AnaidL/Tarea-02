#Autor: Anaid Fernanda Labat González, A01746289
#Descripción: Encontrar cuanto pago de IVA, cuanto de propina y cuanto pago en total basandonos en el subtotal ingresado

#A partir de aqui escribe tu programa

SubTotal=int(input("Costo de su comida:"))
Propina=SubTotal*1.12
PropinaTotal=Propina-SubTotal
Iva=SubTotal*1.16
IvaTotal=Iva-SubTotal
CostoTotal=SubTotal+PropinaTotal+IvaTotal

print("Propina:","$",PropinaTotal)
print("IVA:","$",IvaTotal)
print("Total a pagar:", "$", CostoTotal)