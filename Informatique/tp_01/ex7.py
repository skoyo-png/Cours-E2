import string
import random

while True:
    char = [x for x in string.ascii_uppercase if x not in ['U','I','O'] ]
    plaque = ""
    for i in range(9):
            if i in [2,6]:
                plaque = f"{plaque}-"
            elif i in [3,4,5]:
                plaque = f"{plaque}{random.randint(0,9)}"
            else:
                plaque = f"{plaque}{random.choice(char)}"

        # Façon récursive de traiter le SS, si on en trouve un, on regen la plaque
    if 'SS' in plaque:
        plaque = get_plaque()
    print(plaque)

if __name__ == '__main__':
    for i in range(20):
        print(get_plaque())
