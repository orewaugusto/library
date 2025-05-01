class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def get_charge(self, days_rented: int) -> float:
        if self.price_code == Book.REGULAR:
            amount = 2
            if days_rented > 2:
                amount += (days_rented - 2) * 1.5
            return amount
        elif self.price_code == Book.NEW_RELEASE:
            return days_rented * 3
        elif self.price_code == Book.CHILDREN:
            amount = 1.5
            if days_rented > 3:
                amount += (days_rented - 3) * 1.5
            return amount
        else:
            return 0.0

    def get_frequent_renter_points(self, days_rented: int) -> int:
        if self.price_code == Book.NEW_RELEASE and days_rented > 1:
            return 2
        return 1


class Rental:
    def __init__(self, book: Book, days_rented: int):
        self.book = book
        self.days_rented = days_rented

    def get_charge(self) -> float:
        return self.book.get_charge(self.days_rented)

    def get_frequent_renter_points(self) -> int:
        return self.book.get_frequent_renter_points(self.days_rented)


class Client:

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def statement(self) -> str:

        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"
        
        for rental in self.rentals:
            this_amount = rental.get_charge()
            points = rental.get_frequent_renter_points()

            frequent_renter_points += points
            result += f"- {rental.book.title}: {this_amount}\n"
            total_amount += this_amount
        
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        
        return result


# Nova hierarquia de classes adicionada

from abc import ABC, abstractmethod

class Price(ABC):

    @abstractmethod
    def get_charge(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def get_frequent_renter_points(self, days_rented: int) -> int:
        pass


class RegulaPrice(Price):
    pass


class NewReleasePrice(Price):
    pass


class ChildrenPrice(Price):
    pass
