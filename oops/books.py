# class Book:
# title,author
# display_details()
# calculate_price()
# class Fiction_book:
# title,author,gener
# display_details()
# calculate_price()

# class nonfiction_book
# title,author,topic
# display_detais()
# calculate_price()


# class Book:
# title,author
# display_details()
# claculate_price()
# class Fiction_book:
#     title,author,genre 
#     display_details()
#     claculate_price()

# class Nonfiction_book:
#     title,author,topic
#     display_details()
#     claculate_price()

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def display_details(self):
        print(f"name of title: {self.title}")
        print(f"name of author: {self.author}")
        
    
    def calcutate_price(self):
        pass

class FictionBook(Book):
    def _init_(self, title, author,genre):
        super().__init__(title, author)
        self.genre = genre

    def display_details(self):
        super().display_details()
        print(f"genre : {self.genre}")
    
    def calcutate_price(self):
        pass

class NonfictionBook(Book):
    def __init__(self, title, author,topic):
        super().__init__(title, author)
        self.topic = topic
    
    def display_details(self):
        super().display_details()
        print(f"topic : {self.topic}")
    
    def calcutate_price(self):
        pass



fiction_book = FictionBook("The Hobbit", "J.R.R. Tolkien", "Fantasy")
nonfiction_book = NonfictionBook("Sapiens", "Yuval Noah Harari", "History")

fiction_book.display_details()
fiction_book.calculate_price()

print("\n")

nonfiction_book.display_details()
nonfiction_book.calculate_price()