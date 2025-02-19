# class library

# generate [] for object

# method1,  add_book           (b_name,b_author) obj1.add_book(b_name,b_author)   >>>    [{"name":b_name,"author":b_author}]

# obj1.add_book(b_name1,b_author1)    >>>   [{"name":b_name,"author":b_author},{"name":b_name1,"author":b_author1}]

# method2 ,remove_book ,b_name

# method3 ,diplay books


class Library:

    def __init__(self):
        
        self.books = []

    def add_book(self,b_name,b_author):

        self.b_name = b_name

        self.b_author = b_author

        self.books.append({"name":b_name,"author":b_author})

        print(self.books)

    def remove_book(self,b_name):

        for i in self.books:

            if i["name"] == b_name:

                self.books.remove(i)

                print("Book removed successfully")

                print(self.books)

        else:

            print("requested book not found")

    def display_books(self,b_author):

        books_found = [i for i in self.books if i["author"] == b_author]

        if books_found:

            for i in books_found:

              # print("Requested Author's Book Found")

                print(i)

        else:

            print("Requested Author's Books not found")

obj1 = Library()

obj1.add_book(b_name="An Era of Darkness",b_author="Sasi Tharoor")

obj1.add_book(b_name="The Color Purple",b_author="Alice Walker")

obj1.add_book(b_name="A Passage to India",b_author="E M Forster")

obj1.add_book(b_name="Everyday Use",b_author="Alice Walker")

obj1.remove_book(b_name="xyz")

obj1.display_books(b_author="Alice Walker")

