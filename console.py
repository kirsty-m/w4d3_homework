import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Charles Dickens")
author_repository.save(author_1)
author_2 = Author("Anne Patchett")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("Great Expectations", "Fiction", author_1)
book_repository.save(book_1)
book_2 = Book("The Dutch House", "Fiction", author_2)
book_repository.save(book_2)

book_repository.select_all()

pdb.set_trace()

