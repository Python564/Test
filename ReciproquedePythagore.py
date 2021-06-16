n1 = int(input("Entré la valeur du premier côté: "))
n2 = int(input("Entré la valeur du deuxième côté: "))
n3 = int(input("Entré la valeur de l'hypothénuse: "))
n4 = pow(n1,2)+pow(n2,2)
n5 = pow(n3,2)

if n4 == n5:
    print("Le triangle est bien rectangle.")
else:
    print("Le triangle n'est pas rectangle.")
