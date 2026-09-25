import random
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

with open("dic.txt", 'r', encoding = 'utf-8') as f:
    ligne = f.readlines()
    ligne_ = random.choice(ligne)
    ligne_ = strip_accents(ligne_).upper().strip()
    print(ligne_)
mot = list(ligne_)

pendu = []
pendu += mot[0]
for i in range(1, len(mot)):
    pendu += "_"
print(pendu)

vie = 6
lettres = []
print("Vous avez 6 vies")
while mot != pendu and vie != 0:
    a = input("Entrer une lettre :")
    a = a.upper()
    if a in lettres:
        print("Cette lettre est déjà mise")
    else:
        if a in mot:
            for i in range(len(mot)):
                if a == mot[i]:
                    pendu[i] = mot[i]
                    lettres += a
                    print(pendu)
        else:
            vie -= 1
            print(pendu)
            print("Cette lettre n'est pas dans le mot ")
            print(f"Il vous reste {vie} vie(s)")
            lettres += a

print("Bravo ! Vous avez trouvé le mot", ligne_)