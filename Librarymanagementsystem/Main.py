
class Library:

    def __init__(self,libraryname,booklist):
        self.bookdata={}
        self.libarayname=libraryname
        self.booklist= booklist

        for book in booklist:
            self.bookdata[book] = None

    def listofbook(self):
        listt=self.booklist
        print("List of the books".upper())
        for index, books in enumerate (listt):
            print(f"{index}: {books}")

    def addbook(self):

        print("Enter the book name below. You can add only one book at a time.")
        while(True):
            userinput=input("Name: ")
            self.booklist.append(userinput)
            print(f"Thank you for you contribution to the library. Your book: '{userinput}' has been successfully added to "
                  f"our library."
                  )
            print("Do you want to add another book?")
            userinfo=int(input("1: yes, 2:No"))
            if userinfo==1:
                continue
            else:
                print("See you soon...")
                break

    def lendbook(self):

        print("Which book ???")
        userlend=input("Book name:").capitalize()
        if userlend in self.booklist:
            print("Checking the availability of the book...\n")

            if self.bookdata[userlend] is None:
                print(f"The book '{userlend}', you requested is currently available.\n")
                print("Do you want to lend it: ")
                lendingpermission = int(input("1.yes 2.No"))
                if lendingpermission == 1:
                    username = input("Your name:")
                    self.bookdata[userlend]=username
                    print("Your name and the name of the book has been registered successfully\n")
                    print("List of the book with the name of student who took the book".upper())
                    for key, val in self.bookdata.items() :
                        if val!=None:
                            print(f"Book: {key} -- Student's name: {val}")
            else:
                print(f"This book has already been taken by {self.bookdata.get(userlend)}.\nIt will be available in thisthis date...\nReserver for me (option)")


        else:
            print(f"Sorry there is no book named as '{userlend}' in our library. Please type the spelling of the book correctly.")


    def returnbook(self):
        dicttt = {"Nepali": "Suresh"}
        print("Enter your username")
        username=input("Username:")
        if username==dicttt.values():
            print("You took this this book on this this date")
        else:
            print("hahahah")

def main():
    listofbooks=["Math", "Science","Nepali"]
    libraryname="Shreejan's library"
    shreelibrary=Library(libraryname, listofbooks)

    print('Do you want to\n 1:see the detail of the books\n 2:Lend of book \n 3:donate a book \n 4:return a book\n Q for Exit from the system ')


    Exit = False
    while (Exit is not True):
        firstuser = input("\noption:").capitalize()

        if firstuser == '1':
            shreelibrary.listofbook()
        elif firstuser == '2':
            shreelibrary.lendbook()
        elif firstuser == '3':
            shreelibrary.addbook()
        elif firstuser == '4':
            shreelibrary.returnbook()
        elif firstuser == 'Q':
            Exit = True
        else:
            print(f"Welcome to {shreelibrary.libarayname} ")




if __name__ == '__main__':
    main()














