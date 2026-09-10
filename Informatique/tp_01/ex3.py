age = int(input("Quel est votre âge ? "))
if age < 0:
    print("L'âge ne peut pas être négatif.")
elif age > 0:
    if age <= 2:
        age = age * 10.5
    elif age > 2:
        age = 21 + (age - 2) * 4
    print(f"Votre âge en années de chien est de {age}.")
