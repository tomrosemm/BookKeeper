from setup import marathon, jongara, strip_unique_isbns


def bookandcopyinitialize():
    initial_isbn_list = "Files/list_of_isbn_mine.txt"
    singleton_isbn_list = "Files/unique_isbn.txt"
    copies_file = "Files/copies.csv"
    books_file = "Files/books.csv"
    strip_unique_isbns(initial_isbn_list, singleton_isbn_list)
    marathon(singleton_isbn_list, copies_file)
    jongara(singleton_isbn_list, books_file)


def main():
    bookandcopyinitialize()


if __name__ == "__main__":
    main()
