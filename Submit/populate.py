from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Uncomment these to test your functions:
#Tome_Rater.print_catalog()
#Tome_Rater.print_users()

#print("Most positive user:")
#print(Tome_Rater.most_positive_user())
#print("Highest rated book:")
#print(Tome_Rater.highest_rated_book())
#print("Most read book:")
#print(Tome_Rater.most_read_book())
#print(Tome_Rater.get_n_most_read_books(2))
#print(Tome_Rater.get_n_most_prolific_readers(3))


Tome_Rater.add_user("Morne", "MorneTer@gmail.com")
Tome_Rater.add_user("Nici", "Nici@gmail.com")

mybook1 = Tome_Rater.create_book("Book1", 10000000, 30)
mybook2 = Tome_Rater.create_book("Book2", 20000000, 20)
mybook3 = Tome_Rater.create_book("Book3", 30000000, 50)
mybook4 = Tome_Rater.create_book("Book4", 40000000, 10)
mybook5 = Tome_Rater.create_book("Book5", 50000000, 40)

mynovel1 = Tome_Rater.create_novel("Novel1", "Dude", 60000000, 80)


Tome_Rater.add_book_to_user(mybook1, "MorneTer@gmail.com", 1)
Tome_Rater.add_book_to_user(mybook2, "MorneTer@gmail.com", 2)
Tome_Rater.add_book_to_user(mybook3, "MorneTer@gmail.com", 3)
Tome_Rater.add_book_to_user(mybook4, "Nici@gmail.com", 4)
Tome_Rater.add_book_to_user(mybook5, "Nici@gmail.com", 3)
Tome_Rater.add_book_to_user(mynovel1, "Nici@gmail.com", 3)

#print(Tome_Rater.get_n_most_expensive_books(2))


print(Tome_Rater.get_worth_of_user("MorneTer@gmail.com"))
print(Tome_Rater.get_worth_of_user("Nici@gmail.com"))
