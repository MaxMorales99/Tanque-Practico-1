x = 0

while x<=30:
    print("El valor del bucle es:", x)
    
    if x ==15:
        print("Se rompio el bucle cuando x vale :", x)
        break   
    if x == 4 or x==6 or x==10:
        print("Se salto el valor", x , "de x")
        
    x +=1

print("Se terminó el programa")