# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.

def merge( a: list, b: list) -> list:
    merged_list = list(set(a+b))
    new_list = [x**3 for x in merged_list]
    return new_list

print (merge([1,2,3], [1,2]))