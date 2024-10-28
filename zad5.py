# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list, a drugi
# typu int. Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def contain( array: list, a: int) -> bool:
    return a in array
    
print (contain([1,2,3], 3))
