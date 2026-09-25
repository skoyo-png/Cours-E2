import random
with open("dic.txt", 'r', encoding = 'utf-8') as f:
    ligne = f.readlines()
    mot = random.choice(ligne)
    print(mot)
