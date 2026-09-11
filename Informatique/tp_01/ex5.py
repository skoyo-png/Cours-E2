résultat = " "
q = int(input("Entrez un nombre : "))
while (q!= 0):
    r = q%2
    résultat += str(r)
    q = q//2
print(f"La representation binaire du nombre est : {résultat[::-1]}")