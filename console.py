def load_library():
    library = []
    try:
        with open("library.txt", "r") as file:
            for line in file:
                title, author, year, genre, read = line.strip().split(",")
                library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read": read == "True"})
    except FileNotFoundError:
        print("No library file found. Starting with empty library.")
    return library

library = load_library()

def add_book():
    print("\nEnter the book details:")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower()
    read = True if read == "yes" else False
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    print(f"{title} added successfully!")

def remove_book():
    title = input("\nEnter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"{title} removed successfully!")
            return
    print(f"Sorry, {title} is not in the library.")

def search():
    print("\nSearch by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")

    if choice not in ["1", "2"]:
        print("Invalid choice.")
        return
    
    found = []
    if choice == "1":
        search_text = input("Enter the title: ")
        found = [book for book in library if search_text.lower() in book["title"].lower()]
    else:
        search_text = input("Enter the author: ")
        found = [book for book in library if search_text.lower() in book["author"].lower()]

    
    if found:
        print("\nMatching Books:")
        for book in found:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No books found.")

def display_all():
    print("\nYour Library:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print("")

def display_stats():
    total_books = len(library)
    total_read_books = len([book for book in library if book["read"]])
    print(f"Total books: {total_books}")
    print(f"Percentage read: {(total_read_books / total_books) * 100}%")

def save_library():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n")

def main():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Save and exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search()
        elif choice == "4":
            display_all()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
