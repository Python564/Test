list = []
 
# take number from user, how many element in list
n = int (input ("How many element in list :- "))
 
 
# append element into list using list.append
for i in range (n) :
    storeElement = int (input ("Enter an integer num :- "))
    myList.append (storeElement)
 
# print all elements
print("Input list elements are: ")
for i in range (n) :
    print(myList [i])