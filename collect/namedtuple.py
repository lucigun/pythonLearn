from collections import namedtuple

# Define a Book namedtuple
# Fields : title, author, year_published, isbn
Book = namedtuple(
    'Book',
    ['title','author','year_published', 'isbn']
)

# Create an instance of the Book
my_book = Book(
    title='The blahblah',
    author='John Doe',
    year_published='2025',
    isbn='111111'
)

print(f'Book title:{my_book.title}')
print(f'book author:{my_book.author}')
print(f'year_pub:{my_book.year_published}')
print(f'isbn={my_book.isbn}')

print('\n--Accessing by index---')
print(f'title (by index): {my_book[0]}')
print(f'author (by index): {my_book[1]}')
print(f'year_published (by index): {my_book[2]}')
print(f'isbn (by index): {my_book[3]}')


