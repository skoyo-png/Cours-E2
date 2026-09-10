taille = float(input("Entrez la taille en mètres : "))
poids = float(input("Entrez le poids en kilogrammes : "))
IMC = poids / (taille **2)
print(f"Votre IMC est de {IMC:.2f}")