n1 = int(input("Entrer le nombre à calculer : "))
n2 = int(input("La puissance : "))
if n2 > 0:
    float(n2)
    n3 = pow(n1, n2)
    print(n3)

elif n2 < 0:
    n2 = -n2
    n5=pow(n1, n2)
    n4=1/n5
    print(n4) 
     

else : 
    print("1")