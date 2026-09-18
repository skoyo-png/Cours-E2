p = ["10","2","C","D","+"]

def calculScore(p):
    scores = []
    for i in p:
        if i == "+":
            scores.append(scores.pop() + scores.pop())
        elif i == "D":
            scores.append(2 * scores[-1])
        elif i == "C":
            scores.pop()
        else:
            scores.append(int(i))
    return sum(scores)

print(calculScore(p))