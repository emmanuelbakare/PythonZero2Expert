# SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# A class should have one and only one reason to change, 
# meaning that a class should have only one job.
class Book:
    def __init__(self):
        self.books={}
        self.number=0
    
    def add_book(self, book):
        self.number+=1
        self.books[self.number]=book
        
    def __str__(self):
        return str(self.books)

# the save_book breaks SRP save_book should be in another class should have
# because it is doing something different even though related to the Book class
    # def save_book(self, filename):
    #     with open(filename,'w') as file:
    #         file.write(str(self.books))
    
class StoreBooks:
    @staticmethod
    def save_book(filename,books):
        with open(filename,'w') as file:
            file.write(str(books))
books=Book()
books.add_book('The Voice Magazine')
books.add_book('Making IPhone')
books.add_book('Python Zero to Expert')
# book.save_book('bookstores.txt')
print(books) 

# store the book with the StoreBooks class
bookstore=StoreBooks()
bookstore.save_book('classbookstore.txt',books)
        