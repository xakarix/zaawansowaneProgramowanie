import zad1, zad2, zad3

# zadanie 1
student1 = zad1.Student("Marek", [5, 5, 6, 5, 6, 5, 6, 4, 6])
print(f"{student1.name} ma ma średnią powyej 50: {zad1.student1.is_passed()}")

# zadanie 2

library1 = zad2.Library("Katowice", "Bankowa", 40 - 600, "8-17", "666-333-222")
library2 = zad2.Library("Katowice", "Administracyjna", 40 - 600, "8-20", "566-333-444")

book1 = zad2.Book(library1, "2017", "Dazai", "Osamu", 170)
book2 = zad2.Book(library2, "2016", "Haruki", "Murakami", 700)
book3 = zad2.Book(library1, "2015", "George", "Orwell", 350)
book4 = zad2.Book(library1, "2020", "Yoko", "Ogawa", 220)
book5 = zad2.Book(library2, "1910", "Franz", "Kafka", 120)

employee1 = zad2.Employee(
    "Marek", "Komarek", "12-1-2023", "1-1-2000", "Poznan", "Mikolowska"
)
employee2 = zad2.Employee(
    "Marianna", "Kocioł", "1-12-2013", "12-11-1990", "Warszawa", "Bankowa"
)

order1 = zad2.Order(employee1, [book1, book2, book4], "23-10-2024")
order2 = zad2.Order(employee2, [book3, book5], "12-10-2024")

print(f"FIRST ORDER: {order1}\n")
print(f"SECOND ORDER: {order2}\n")


# zadanie 3

domek = zad3.House(300, 8, 1000000, "Wierzbowa 5, Katowice", 1200)
flat1 = zad3.Flat(80, 4, 700000, "Mikołowska 12, Katowice", 4)
print(domek, "\n")
print(flat1)
