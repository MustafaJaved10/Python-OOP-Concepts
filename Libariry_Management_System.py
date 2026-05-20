
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.Is_issued = False

    def display(self):
        status = "Issued" if self.Is_issued else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")


class User:
    def __init__(self, UserId, name):
        self.UserId = UserId
        self.name = name
        self.borrowed_List = []

    def display(self):
        print(f"User ID        : {self.UserId}")
        print(f"Name           : {self.name}")
        print(f"Borrowed Books : {self.borrowed_List}")


class Library:
    def __init__(self):
        self.userList = []
        self.booksList = []

    def addUser(self, user):
        self.userList.append(user)

    def addBook(self, book):
        self.booksList.append(book)

    def findUser(self, UserId):
        for user in self.userList:
            if user.UserId == UserId:
                return user
        return None

    def findBook(self, book_id):
        for book in self.booksList:
            if book.book_id == book_id:
                return book
        return None

    def userIdExists(self, UserId):
        return self.findUser(UserId) is not None

    def bookIdExists(self, book_id):
        return self.findBook(book_id) is not None

    def IssueBook(self, UserId, book_id):
        user = self.findUser(UserId)
        book = self.findBook(book_id)
        if user is None or book is None:
            return "User or book not found"
        if book.Is_issued:
            return "Book is already issued"
        book.Is_issued = True
        user.borrowed_List.append(book_id)
        return (f"Book issued successfully!\n"
                f"User ID   : {user.UserId}\n"
                f"User Name : {user.name}\n"
                f"Book ID   : {book.book_id}\n"
                f"Book Title: {book.title}")

    def returnBooks(self, UserId, book_id, daysLate):
        user = self.findUser(UserId)
        book = self.findBook(book_id)
        if user is None or book is None:
            return "User or book not found"
        if not book.Is_issued:
            return "Book is not issued"
        book.Is_issued = False
        user.borrowed_List.remove(book_id)
        fine = self.calculateFine(daysLate)
        return f"Book returned successfully. Fine = {fine} Rs"

    def searchUser(self, key):
        for user in self.userList:
            if user.UserId == key or user.name.lower() == key.lower():
                return user
        return None

    def searchBook(self, key):
        for book in self.booksList:
            if (book.book_id == key or
                book.title.lower() == key.lower() or
                book.author.lower() == key.lower()):
                return book
        return None

    def bookCount(self):
        return len(self.booksList)

    def UserCount(self):
        return len(self.userList)

    def calculateFine(self, daysLate):
        return daysLate * 10 if daysLate > 0 else 0

    def showUser(self):
        if not self.userList:
            print("No users added yet!")
        else:
            for i, user in enumerate(self.userList, 1):
                print(f"\nUser {i}:")
                user.display()

    def showBook(self):
        if not self.booksList:
            print("No books added yet!")
        else:
            for i, book in enumerate(self.booksList, 1):
                print(f"\nBook {i}:")
                book.display()


def pause():
    input("\nPress Enter to continue...")

def getDigitInput(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Only digits allowed! Try again.")

def getAlphaInput(prompt):
    while True:
        value = input(prompt).strip()
        if value.replace(" ", "").isalpha():
            return value
        print("Only alphabets allowed! Try again.")

def getDaysLate():
    while True:
        value = input("Days Late: ").strip()
        if value.isdigit():
            return int(value)
        print("Days late must be a number! Try again.")


library = Library()


def adminPanel():
    while True:
        print("\n===== ADMIN PANEL =====")
        print("1.  Add User")
        print("2.  Add Book")
        print("3.  Show Users")
        print("4.  Show Books")
        print("5.  Search User")
        print("6.  Search Book")
        print("7.  Book Count")
        print("8.  User Count")
        print("9.  Issue Book")
        print("10. Return Book")
        print("11. Exit Admin Panel")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            user_id = getDigitInput("User ID (digits only): ")
            if library.userIdExists(user_id):
                existing = library.findUser(user_id)
                print(f"User ID '{user_id}' already exists!")
                print(f"Existing user - ID: {existing.UserId}, Name: {existing.name}")
            else:
                name = getAlphaInput("Name (alphabets only): ")
                library.addUser(User(user_id, name))
                print(f"User added! ID: {user_id}, Name: {name}")
            pause()

        elif choice == "2":
            book_id = getDigitInput("Book ID (digits only): ")
            if library.bookIdExists(book_id):
                existing = library.findBook(book_id)
                print(f"Book ID '{book_id}' already exists!")
                print(f"Existing book - ID: {existing.book_id}, Title: {existing.title}, Author: {existing.author}")
            else:
                title = input("Title: ").strip()
                author = getAlphaInput("Author (alphabets only): ")
                library.addBook(Book(book_id, title, author))
                print(f"Book added! ID: {book_id}, Title: {title}, Author: {author}")
            pause()

        elif choice == "3":
            library.showUser()
            pause()

        elif choice == "4":
            library.showBook()
            pause()

        elif choice == "5":
            key = input("Enter User ID or Name: ").strip()
            result = library.searchUser(key)
            if result is None:
                print("User not found!")
            else:
                print("User found:")
                result.display()
            pause()

        elif choice == "6":
            key = input("Enter Book ID, Title or Author: ").strip()
            result = library.searchBook(key)
            if result is None:
                print("Book not found!")
            else:
                print("Book found:")
                result.display()
            pause()

        elif choice == "7":
            print(f"Total Books: {library.bookCount()}")
            pause()

        elif choice == "8":
            print(f"Total Users: {library.UserCount()}")
            pause()

        elif choice == "9":
            user_id = getDigitInput("User ID: ")
            book_id = getDigitInput("Book ID: ")
            print(library.IssueBook(user_id, book_id))
            pause()

        elif choice == "10":
            user_id = getDigitInput("User ID: ")
            book_id = getDigitInput("Book ID: ")
            daysLate = getDaysLate()
            print(library.returnBooks(user_id, book_id, daysLate))
            pause()

        elif choice == "11":
            break

        else:
            print("Invalid choice!")
            pause()


def userPanel():
    while True:
        print("\n===== USER PANEL =====")
        print("1. View Books")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. My Borrowed Books")
        print("6. Exit User Panel")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            library.showBook()
            pause()

        elif choice == "2":
            key = input("Enter Book ID, Title or Author: ").strip()
            result = library.searchBook(key)
            if result is None:
                print("Book not found!")
            else:
                print("Book found:")
                result.display()
            pause()

        elif choice == "3":
            user_id = getDigitInput("User ID: ")
            book_id = getDigitInput("Book ID: ")
            print(library.IssueBook(user_id, book_id))
            pause()

        elif choice == "4":
            user_id = getDigitInput("User ID: ")
            book_id = getDigitInput("Book ID: ")
            daysLate = getDaysLate()
            print(library.returnBooks(user_id, book_id, daysLate))
            pause()

        elif choice == "5":
            user_id = getDigitInput("Enter User ID: ")
            user = library.findUser(user_id)
            if user is not None:
               if len(user.borrowed_List) == 0:
                 print("No books borrowed yet!")
               else:
                  print(f"User ID   : {user.UserId}")
                  print(f"User Name : {user.name}")
                  print("Borrowed Books:")
                  for book_id in user.borrowed_List:
                   book = library.findBook(book_id)
                   print(f"  Book ID   : {book.book_id}")
                   print(f"  Book Title: {book.title}")
            else:
               print("User not found!")
               pause()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")
            pause()


while True:
    print("\n===== MAIN MENU =====")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        adminPanel()
    elif choice == "2":
        userPanel()
    elif choice == "3":
        print("System closed")
        break
    else:
        print("Invalid choice!")
        pause()
