import sys

print ('argument list', sys.argv)
ht = sys.argv[1]
if ht.lower() != 'head' and ht.lower() != 'tail' :
    print("Error Value ! Entrer Head ou Tail")
lignes = int(sys.argv[2])
if lignes < 0:
    print("Error Value ! Entrer un nombre de lignes correct")
loc = sys.argv[3]

try :
    if ht.lower() == 'head':
        with open(loc, 'r', encoding = 'utf-8') as f:
            for _ in range(lignes):
                l = f.readline()
                if l == None:
                    break
                print(l)

    elif ht.lower() == 'tail':
        with open(loc, 'r', encoding = 'utf-8') as f:
            l = f.readlines()
            for l in l[- lignes]:
                if l == None:
                    break
                print(l)

except FileNotFoundError:
    print("Fichier Introuvable")