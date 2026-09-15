class Book:
    def __init__(self, title, autor, editorhouse, purchaseprice):
        self.title = title
        self.autor = autor
        self.editorhouse = editorhouse
        self.__purchaseprice = purchaseprice
        
    def get_purchaseprice(self):
        return self.__purchaseprice
    #con get leggiamo il valore dell'attributo nascosto con Mangling
    
    def set_purchaseprice(self, value):
        self.__purchaseprice = value
    #con set ne modifichiamo il valore 
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.autor}, Editor: {self.editorhouse}, Price: {self.__purchaseprice}"
    

class Catalog:
    def __init__(self, name, description, booklist, totalvalue):
        self.name = name
        self.description = description
        self.booklist = booklist
        self.__totalvalue = totalvalue
        
    def get_totalvalue(self):
        return self.__totalvalue
    
    def set_totalvalue(self, value):
        self.__totalvalue = value
    
    def add_book(self, book):
        self.booklist.append(book)
        self.__totalvalue += book.get_purchaseprice()
        
        
    def remove_book(self, book):
        self.booklist.remove(book)
        self.__totalvalue -= book.get_purchaseprice()
        

    def __eq__(self, other):
        if isinstance(other, Catalog):
            return self.name == other.name and self.description == other.description and self.booklist == other.booklist
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, Catalog):
            newlist = self.booklist + other.booklist
            return Catalog(self.name + other.name, "merged catalog", newlist, 0)
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Total: {self.__totalvalue}"
    
    
    
bk1 = Book("The Mistery", "Stephen Forward", "ForwardHouse", 30)

cat1 = Catalog("Yellow", "An collections of yellow and thriller books", [], 0)
cat2 = Catalog("Yellow", "An collections of yellow and thriller books", [], 0)

print(bk1)
print(cat1)

cat1.add(cat2)

