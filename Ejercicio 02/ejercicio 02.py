import random
r=random.randint(1,20)
num=0
contador=6



while(contador!=0):
    print("ingrese su numero")
    num=int(input())
    
    if(num>r):
        print("tu numero es mas grande que el oculto, te quedan",contador,'oportunidades')
        contador=contador-1
        
    else:
        if(num<r):
            print("tu numero es menor que el oculto, te quedan",contador,'oportunidades')
            contador=contador-1
            
        else:
            if(num==r):
                print('Adivinaste el numero!!!')
                
            else:
                print('te quedaste sin oportunidades')
        




