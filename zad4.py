# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool

def compere(a: int, b: int, c: int) -> bool:
    return (a+c) >= c 

print (compere(1,2,3))