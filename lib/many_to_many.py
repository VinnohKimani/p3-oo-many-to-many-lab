class Author:
    all = []

    def __init__(self, name = str):
        self.name = name
        Author.all.append(self)

    def contracts(self):
            return [contract for contract in Contract.all if contract.author == self ]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []
    def __init__(self, title = str):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise ValueError("date must be a string.")
        if not isinstance(royalties, int):
            raise ValueError("royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    
    @classmethod
    def contracts_by_date(cls, date=None):
        contracts = cls.all
        if date is not None:
            contracts = [c for c in contracts if c.date == date]
        return sorted(contracts, key=lambda c: c.date)
       