library = [
    {
        "title": "The Pragmatic Programmer",
        "author": "David Thomas",
        "pages": 352,
        "read": True,
    },
    {"title": "Clean Code", "author": "Robert Martin", "pages": 431, "read": False},
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "pages": 544,
        "read": True,
    },
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": 310, "read": True},
    {"title": "Atomic Habits", "author": "James Clear", "pages": 320, "read": False},
    {"title": "Deep Work", "author": "Cal Newport", "pages": 296, "read": True},
    {"title": "Dune", "author": "Frank Herbert", "pages": 688, "read": False},
    {
        "title": "Python with Claude AI",
        "author": "Frank Herbert",
        "pages": 688,
        "read": False,
    },
]


def print_book(header, books):
    print(f"\n--- {header} ---")
    for book in books:
        title = book["title"]
        author = book["author"]
        pages = book["pages"]

        print(f"Title: {title} | Author: {author} | Pages: {pages}")


def get_author():
    to_search = input("\nEnter Author's name: ").lower()

    match = [book for book in library if book["author"].lower() == to_search]

    if not match:
        print("No books found by that author!")
        return

    print_book(to_search.title(), match)


def books_with_pages(page_count):
    return [book for book in library if book["pages"] == page_count]


# Print all books you've already read
read_books = [book for book in library if book["read"]]

print_book("Read Books", read_books)


# Print all unread books
unread_books = [book for book in library if not book["read"]]

print_book("Unread Books", unread_books)


# Print books sorted by page count ascending
sorted_books = sorted(library, key=lambda book: book["pages"])

print_book("Books sorted by page count", sorted_books)


# Print the longest and shortest book
longest_book = max(book["pages"] for book in library)
print_book("Longest Book", books_with_pages(longest_book))


shortest_book = min(book["pages"] for book in library)
print_book("Shortest Book", books_with_pages(shortest_book))

# Print the total pages of all read books
total_pages_of_read_books = sum(book["pages"] for book in read_books)
print(f"\nTotal pages of all books: {total_pages_of_read_books:,}")

# Print the average page count across all books
avg_page_count = sum(book["pages"] for book in library) / len(library)
print(f"Average page count: {avg_page_count:.2f}")


get_author()
