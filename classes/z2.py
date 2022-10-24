class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return ("Biblioteka w miescie {}, na ulicy {}, kod pocztowy {}, otwarta w godzinach {}, nr telefonu: {}".format(
            self.city, self.street, self.zip_code, self.open_hours, self.phone))


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return ("Pracownik {} {}, zatrudniony {}, urodzony {}. Mieszka w {}, {}, {}. Nr Telefonu: {}".format(
            self.first_name, self.last_name, self.hire_date, self.birth_date, self.city, self.street, self.zip_code,
            self.phone))


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return ('Książka autorstwa {} {} opublikowana {}, mająca {} stron.\n W bibliotece {}'.format(self.author_name,
                                                                                                     self.author_surname,
                                                                                                     self.publication_date,
                                                                                                     self.number_of_pages,
                                                                                                     self.library))


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return ("Zamowienie {} zawierajace {}, zatwierdzone przez {} dnia {}".format(self.student,
                                                                                     (Book for Book in self.books),
                                                                                     self.employee, self.order_date))
