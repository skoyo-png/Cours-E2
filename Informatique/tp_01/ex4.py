N = int(input("Entrez un entier N : "))
i = 2
k = 2
pi = 3
terme = 1
while(terme != N):
    pi = pi+(4*(-1)**k) / (i*(i+1)*(i+2))
    i += 2
    k += 1
    terme += 1
print(f"La valeur de pi est : {round(pi,terme)}")