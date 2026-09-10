nombres = []

n = int(input("Combien de valeurs en tout ? "))

for _ in range(n):
    i = int(input("Entrez un entier : "))
    nombres.append(i)

else:
    nombres_tries = sorted(nombres)
    minimum = min(nombres)
    maximum = max(nombres)
    moyenne = sum(nombres) / len(nombres)

    print(f"Nombres triés : {nombres_tries}")
    print(f"Minimum : {minimum}")
    print(f"Maximum : {maximum}")
    print(f"Moyenne : {moyenne}")
    
