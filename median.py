import statistics
list = []
# Prends les infos des utilisateurs
n = int (input ("Combien il y a t-il de chiffres ?  "))
 
 
# append element into list using list.append
for i in range (n) :
    storeElement = int (input ("il y a- "))
    list.append (storeElement)
 
for i in range (n) :
    print(f"La mediane est {statistics.median(list)}")