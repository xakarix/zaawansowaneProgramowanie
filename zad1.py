# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false .


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 5


student1 = Student("Marek", [5, 5, 6, 5, 6, 5, 6, 4, 6])
print(f"{student1.name} ma ma średnią powyej 50: {student1.is_passed()}")

student2 = Student("Marek2", [1, 2, 3, 2, 3])
print(f"{student2.name} ma ma średnią powyej 50: {student2.is_passed()}")
