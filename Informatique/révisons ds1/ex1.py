def decalage_cesar(cle, phrase):
    cle = list(cle.upper())
    phrase = list(phrase.upper())
    print(phrase,"==>", end = " ")
    for i in range(len(phrase)):
        phrase[i] = chr(ord(phrase[i]) + ord(cle[i])-64)
        print(phrase[i], end = " ")
    return " "
        

print(decalage_cesar("ABABABA", "Je"))
