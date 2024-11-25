class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library is located at: {self.zip_code} {self.city} {self.street}.\n"
            f"Open hours: {self.open_hours}\n"
            f"More info: {self.phone}\n"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}\n"
            f"Hired on: {self.hire_date}\n"
            f"More info: {self.birth_date} {self.city} {self.street}\n"
        )


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"You can find book in: {self.library}\n"
            f"Book info:\n"
            f"Released at: {self.publication_date}\n"
            f"Written by: {self.author_name} {self.author_surname}\n"
            f"Book legnth: {self.number_of_pages}\n"
        )


class Order:
    def __init__(self, employee, books, order_date):
        self.employee = employee
        # self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_details = "\n".join(str(book) for book in self.books)
        return (
            f"Employee: {self.employee}\n"
            # f'Student: {self.student}\n'
            f"Books: \n"
            f"{books_details}\n"
            f"order date: {self.order_date}\n"
        )


library1 = Library("Katowice", "Bankowa", 40 - 600, "8-17", "666-333-222")
library2 = Library("Katowice", "Administracyjna", 40 - 600, "8-20", "566-333-444")

book1 = Book(library1, "2017", "Dazai", "Osamu", 170)
book2 = Book(library2, "2016", "Haruki", "Murakami", 700)
book3 = Book(library1, "2015", "George", "Orwell", 350)
book4 = Book(library1, "2020", "Yoko", "Ogawa", 220)
book5 = Book(library2, "1910", "Franz", "Kafka", 120)

employee1 = Employee(
    "Marek", "Komarek", "12-1-2023", "1-1-2000", "Poznan", "Mikolowska"
)
employee2 = Employee(
    "Marianna", "Kocioł", "1-12-2013", "12-11-1990", "Warszawa", "Bankowa"
)

order1 = Order(employee1, [book1, book2, book4], "23-10-2024")
order2 = Order(employee2, [book3, book5], "12-10-2024")

print(f"FIRST ORDER: {order1}\n")
print(f"SECOND ORDER: {order2}\n")
