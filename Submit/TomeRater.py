
# TomeRater by MM Terblanche

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} # book, rating

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books_read}".format(name=self.name, email=self.email, books_read=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def __hash__(self):
        return hash((self.name, self.email))

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user's email has been updated to {email}".format(email=self.email))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        sum_of_ratings = 0
        amount_of_ratings = 0
        
        for book_rating in self.books.values():
            if book_rating is not None:
                sum_of_ratings += book_rating
                amount_of_ratings += 1

        return sum_of_ratings / amount_of_ratings


class Book(object):
    def __init__(self, title, isbn, price=0):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __repr__(self):
        return "{title} with isbn {isbn}".format(title=self.title, isbn=self.isbn)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn and self.price == other_book.price

    def __hash__(self):
        return hash((self.title, self.isbn, self.price))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The book's ISBN has been updated to {isbn}".format(isbn=self.isbn))

    def add_rating(self, rating):
        if rating is None:
            return
        elif rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        sum_of_ratings = sum(self.ratings)
        amount_of_ratings = len(self.ratings)
        
        return sum_of_ratings / amount_of_ratings


class Fiction(Book):
    def __init__(self, title, author, isbn, price=0):
        super(Fiction, self).__init__(title, isbn, price)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

    def get_author(self):
        return self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price=0):
        super(Non_Fiction, self).__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater(object):
    def __init__(self):
        self.users = {} # email, user
        self.books = {} # book, users_read

    def __repr__(self):
        return "TomeRater with {user_count} users and {book_count} books".format(user_count=len(self.users), book_count=len(self.books))

    def __eq__(self, other_tomerater):
        return self.users == other_tomerater.users and self.books == other_tomerater.books

    def create_book(self, title, isbn, price=0):
        for book in self.books.keys():
            if book.isbn == isbn:
                print("A book with this ISBN already exists!")
                return

        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price=0):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price=0):
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users[email]

        if email in self.users.keys():
            user.read_book(book, rating)
            book.add_rating(rating)
            test_book = self.books.get(book, None)

            if test_book is None:
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        is_valid_email = "@" in email and (".com" in email or ".edu" in email or ".org" in email)

        if not is_valid_email:
            "Invalid email, should contain an @ character and either .com , .edu , .org!"
        elif email in self.users.keys():
            "This user already exists"
        else:
            self.users[email] = User(name, email)
            if user_books is not None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        '''
        most_read = 0
        most_read_book = None
        for book, read in self.books.items():
            if read > most_read:
                most_read = read
                most_read_book = book
        '''
        most_read_book = self.get_n_most_read_books(1)

        #print("The most read book is {title} with a total of {read} times read".format(title=most_read_book.title, read=most_read))
        return most_read_book

    def highest_rated_book(self):
        rating = 0
        highest_rated = 0
        highest_rated_book = None

        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rated:
                highest_rated = rating
                highest_rated_book = book

        #print("The highest rated book is {title} with a rating of {rating}".format(title=highest_rated_book.title, rating=highest_rated))
        return highest_rated_book

    def most_positive_user(self):
        most_positive = 0
        most_positive_user = None

        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > most_positive:
                most_positive = rating
                most_positive_user = user

        #print("The most positive user is {name} with an average rating of {rating}".format(name=most_positive_user.name, rating=most_positive))
        return most_positive_user

    def get_n_most_read_books(self, n):
        most_read_books = {}
        most_n = 0

        for book, users_read in sorted(self.books.items(), key=lambda x:x[1], reverse=True):
            if most_n < n: 
                most_read_books[book] = users_read
            most_n += 1

        return most_read_books

    def get_n_most_prolific_readers(self, n):
        most_prolific_readers = {}
        most_n = 0

        for user in sorted(self.users.values(), key=lambda user:len(user.books), reverse=True):
            if most_n < n: 
                most_prolific_readers[user] = len(user.books)
            most_n += 1

        return most_prolific_readers

    def get_n_most_expensive_books(self, n):
        most_expensive_books = {}
        most_n = 0

        for book in sorted(self.books.keys(), key=lambda book:book.price, reverse=True):
            if most_n < n: 
                most_expensive_books[book] = book.price
            most_n += 1

        return most_expensive_books

    def get_worth_of_user(self, user_email):
        worth = 0
        
        user = self.users.get(user_email, None)

        if user is None:
            print("User not found!")
        else:
            worth = sum(book.price for book in user.books)

        return worth
