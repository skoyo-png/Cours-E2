import sys

while True:
    type = str(input("Quelle est l'opération que vous souhaitez utiliser ? (a)ddition, (s)oustraction, (m)ultiplication, (d)ivision : "))
    type = type.lower()

    if type != "a" and type != "s" and type != "m" and type != "d":
        print("Opération non reconnue, veuillez réessayer.")
        reponse = str(input("Voulez-vous refaire un calcul ? (o)ui / (n)on : "))
        if reponse == "o" :
            continue
        else:
            print("Aurevoir !")
            sys.exit()
    else:
        break

valeur1 = int(input("Entrez la première valeur : "))
valeur2 = int(input("Entrez la deuxième valeur : "))

if type == "a":
    résultat = valeur1 + valeur2
    print(f"Le résultat de l'addition est : {valeur1} + {valeur2} = {résultat}")

elif type == "s":
    résultat = valeur1 - valeur2
    print(f"Le résultat de la soustraction est : {valeur1} - {valeur2} = {résultat}")

elif type == "m":
    résultat = valeur1 * valeur2
    print(f"Le résultat de la multiplication est : {valeur1} * {valeur2} = {résultat}")

elif type == "d":
    if valeur2 == 0:
        print(f"Le résultat de la division est : {valeur1} / {valeur2} = Division impossible")
    else:
        résultat = valeur1 / valeur2
        print(f"Le résultat de la division est : {valeur1} / {valeur2} = {résultat}")