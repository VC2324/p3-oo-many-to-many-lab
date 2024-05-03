class Author:
    def __init__(self, name:str):
        self.name = name
        
    def contracts(self):
        contract_list =[contract for contract in Contract.all if contract.author == self]
        return contract_list
        
    def books(self):
        book_list= [contract.book for contract in Contract.all if contract.author == self]
        return book_list
        
    def sign_contract(self, book: "Book", date:str, royalties: int ):
        return Contract(author=self, book=book, date=date, royalties=royalties)
        
    def total_royalties(self):
        royalties_list = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(royalties_list)
        
class Book:
    def __init__(self, title: str) :
        self.title = title

    def contracts(self):
        contract_list =[contract for contract in Contract.all if contract.book == self]
        return contract_list
    
    def authors(self):
        author_list=[contract.author for contract in Contract.all if contract.book == self]
        return author_list

class Contract:
    all =[]
    def __init__(self, author:Author, book:Book, date:str, royalties:int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)


    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if type(value)==Author:
            self._author = value
        else:
            raise Exception("author must be of type Author")
        
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if type(value)== Book:
            self._book= value
        else:
            raise Exception("book must be of type Book")
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if type(value) == str:
            self._date = value
        else:
            raise Exception("Date must be of type string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if type(value) == int:
            self._royalties = value
        else: 
            raise Exception("royalties must be of type Integer")
    
    @classmethod
    def contracts_by_date(cls, date):
        return[contract for contract in cls.all if contract.date == date]