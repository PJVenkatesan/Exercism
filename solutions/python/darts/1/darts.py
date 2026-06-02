import math

def score(x, y):
    if math.sqrt(abs(x)**2 + abs(y)**2) > 10:
        return 0
    if math.sqrt(abs(x)**2 + abs(y)**2) > 5:
        return 1
    if math.sqrt(abs(x)**2 + abs(y)**2) > 1:
        return 5
    return 10
