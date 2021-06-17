import math
corp = str(input("Veuillez entré Cônes ou Pyramide: "))
mesure = str(input("Entrer la mesure: "))


if corp == "Cônes":
    n1 = int(input("Entrer le rayon du Cônes: "))
    n = int(input("Entrer la hauteur du Cônes:  "))
    n2 = pow(n1,2)*math.pi
    n3 = n2*n/3
    print("{} {}".format(n3, mesure))
    


elif corp == "Pyramides":
    n1 = int(input("Entrer un coté de la base de la Pyramide: "))
    n = int(input("Entrer la hauteur de la Pyramide: "))
    n2 = pow(n1,2)*n/3
    print("{} {}".format(n2, mesure))
