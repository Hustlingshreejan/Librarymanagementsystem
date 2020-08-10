from datetime import datetime
class Library:

    def __init__(self,libraryname,booklist):
        self.bookdata={}
        self.libarayname=libraryname
        self.booklist= booklist

        for book in booklist:
            self.bookdata[book] = None
    def save_book(self):
        with open("savingbook.txt","a") as sb:
            for book in self.booklist:
                sb.write(book+'\n')

    def listofbook(self):
        listt=self.booklist
        print("List of the books".upper())
        for index, books in enumerate (listt, start=1):
            print(f"{index}: {books}")

    def addbook(self):
        print("Enter the book name below. You can add only one book at a time.")
        while(True):
            userinput=input("Name: ")
            self.booklist.append(userinput)
            with open("savingbook.txt", "a") as sbb:
                sbb.write(userinput)
            self.bookdata[userinput]=None
            print(f"Thank you for your contribution to the library. Your book: '{userinput}' has been successfully added to "
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
        print("Which book you are looking for ???")
        userlend=input("Book name:").capitalize()

        if userlend in self.booklist:
            print("Checking the availability of the book...\n")
            if self.bookdata[userlend] is None:
                print(f"The book '{userlend}', you requested is currently available.\n")
                print("Do you want to lend it: ")
                lendingpermission = int(input("1.yes 2.No"))
                if lendingpermission == 1:
                    username = input("To lend a book you have to provide your name.\nYour name:")
                    self.bookdata[userlend]=username
                    with open("lendrecord.txt","a") as lr:
                        presentdate=datetime.now()
                        lr.write(f"Date:{[str(presentdate)]}, Book_name:{userlend}, Username:{username}\n")
                    print("Your name has been registered successfully\n")
                    # print("List of the book with the name of student who took the book".upper())
                    # for key, val in self.bookdata.items() :
                    #     if val!=None:
                    #         print(f"Book: {key} -- Student's name: {val}")
            else:
                print(f"This book has already been taken by {self.bookdata.get(userlend)}.\nIt will be available in thisthis date...\nReserver for me (option)")
        else:
            print(f"Sorry there is no book named as '{userlend}' in our library. Please type the spelling of the book correctly.")


    def returnbook(self):
        print("Enter your username")
        username=input("Username:")
        for key,value in self.bookdata.items():
            if value!=None:
                if value == username:
                    print(key, value)
                    print(f"You borrowed {key} book on this this date")
                    self.bookdata[key]=None
                    with open("bookreturnrecord.txt","a") as brr:
                        returndate=datetime.now()
                        brr.write(f"Date:{[str(returndate)]}, Book_name:{key}, Username:{username}\n")

                    # self.bookdata.pop(key)
                    print("The book has been released.")
                    break
                else:
                    print(f"The username is incorrect.\nUser name {username} has not been registered yet.")

    def bookdel(self):

        print("Now you have access to delete the book from the library.")
        admindel=input("Which book you want to delete? ").capitalize()
        print(self.booklist)
        self.booklist.remove(admindel)
        with open("savingbook.txt", "r+") as sbb:
            sbb.truncate(admindel)

        print(self.booklist)



def main():
    set_libraryname=input("Give the name to your library:")
    listofbooks=list(input("Add book in your library:").title().split(','))
    # print(listofbooks)
    shreelibrary=Library(set_libraryname, listofbooks)
    shreelibrary.save_book()
    adminpass=192
    print(f"Welcome to {shreelibrary.libarayname} ".upper())
    print('Do you want to\n 1:List all the books of the library\n 2:Lend of book \n 3:donate a book \n 4:return a book\n 5:Admin pannel\nQ for Exit from the system ')
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
        elif firstuser=='5':
            print("This is for admin only\n")
            foradmin=int(input("Enter the password:"))
            if foradmin == adminpass:
                shreelibrary.bookdel()
            else:
                print("Access denied")
        elif firstuser == 'Q':
            Exit = True
        else:
            print(f"Welcome to {shreelibrary.libarayname} ")

if __name__ == '__main__':
    main()
