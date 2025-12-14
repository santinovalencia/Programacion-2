iva=1.21
iva2=0
factura=0
total=0
cambiar=""

print("de cuanto es su factura")
factura=int(input())

print("desea cambiar el porcentaje de su iva el porcentaje actual es de 21% responda con NO o SI")
cambiar=input()

if(cambiar=="SI"):
    print("de cuanto va a ser su iva")
    iva2=int(input())
    iva2=iva2/100+1
    total=factura*iva2
    print("el total a pagar despues de los inpuestos es: ",total)

else:
    total=factura*iva
    print("el total a pagar despues de los inpuestos es: ",total)
    
