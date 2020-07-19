
class Library:

    def __init__(self,libraryname,booklist):
        self.libarayname=libraryname
        self.booklist= booklist

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
        dictt={"Nepali":"Suresh"}
        print("Which book ???")
        userlend=input("Book name:").capitalize()
        if userlend in self.booklist:
            print("Checking the availability of the book...\n")
            for keys in dictt.keys():
                if userlend == keys:
                    print(f"This book has already been taken by {dictt.get(userlend)}.\nIt will be available in thisthis date...\nReserver for me (option)")
                    # print("Do you want to take any other book?")
                    break
            else:
                print(f"The book '{userlend}', you requested is currently available.\n")
                print("Do you want to lend it: ")
                lendingpermission = int(input("1.yes 2.No"))
                if lendingpermission == 1:
                    username = input("Your name:")
                    dictt.update({userlend:username})
                    print("Your name and the name of the book has been registered successfully\n")
                    print("List of the book with the name of student who took the book".upper())
                    for key, val in dictt.items():
                        print(f"Book: {key} -- Student's name: {val}")
                else:
                    pass
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


shreelibrary=Library("Shreejan's library", ["Math", "Science","Nepali"])
if __name__ == '__main__':

        print("\nDo you want to\n"
              " 1:see the detail of the books\n "
              "2:Lend of book \n"
              " 3:donate a book \n"
              " 4:return a book".upper())
        firstuser=int(input("Provide the option to the system:"))
        if firstuser==1:
            shreelibrary.listofbook()
        elif firstuser==2:
            shreelibrary.lendbook()
        elif firstuser==3:
            shreelibrary.addbook()
        elif firstuser==4:
            shreelibrary.returnbook()
        else:
            print(f"Welcome to {shreelibrary.libarayname} ")













