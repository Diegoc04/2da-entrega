import math
import Libreria as lc
def sumvectores(v,w):
    return [a + b for a, b in zip(v, w)]
    
if __name__ == "__main__":
    v = [(1,0),(2,0)]
    w = [(3,0),(7,0)]
    print(sumvectores(v,w))


def inverso(v):
    r1 = v[0]
    r2 = v[-1]
    return (f"[{r1},{r2}]")

if __name__ == "__main__":
    v = [(1,0),(2,0)]
    print(inverso(v))

def multescalar(c,v):
    r1 = v[0]
    r2 = v[-1]
    return (f"[{c}{r1},{c}{r2}]")

if __name__ == "__main__":
    v = [(1,0),(2,0)]
    c = 3
    print(multescalar(c,v))
