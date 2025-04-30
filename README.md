# personal-library-manager

This project is a Personal Library Manager that allows users to manage their book collection. It provides functionalities to add, remove, search, view, and display statistics of books in the library. The project includes both a console-based application and a web-based application using Streamlit.

# Features
* Add Book: Add a new book to the library.
* Remove Book: Remove an existing book from the library.
* Search Book: Search for a book by title or author.
* View Library: View all books in the library.
* Statistics: Display statistics about the library, such as the total number of books and * the percentage of books read.

# Files
* `app.py`: The main file for the Streamlit web application.
* `console.py`: The main file for the console-based application.
* `library.txt`: The file where the library data is stored.

# Requirements
* Python 3.x
* Streamlit


# Installation
1. **Clone the repository:**

`git clone https://github.com/yourusername/personal-library-manager.git
cd personal-library-manager`
2. ** Install the required packages:**

`pip install streamlit`
# Usage
** Console Application **
1. **Run the console application:**

python console.py
Follow the on-screen instructions to manage your library.

Web Application
Run the Streamlit application:

streamlit run app.py
Open your web browser and go to the provided URL to access the web interface.

Code Explanation
app.py
Imports: The necessary libraries are imported.

import streamlit as st
Load Library: Function to load the library data from library.txt.

def load_library():
    library = []
    with open("library.txt", "r") as file:
        for line in file:
            title, author, year, genre, read = line.strip().split(",")
            library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read": read == "True"})
    return library
Save Library: Function to save the library data to library.txt.

def save_library():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n")
Streamlit Interface: The main interface for the Streamlit application.

st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("📌 Menu", ["Add Book", "Remove Book", "Search Book", "View Library", "Statistics"])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    # Code to add a book
elif menu == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    # Code to remove a book
elif menu == "Search Book":
    st.subheader("🔍 Search for a Book")
    # Code to search for a book
elif menu == "View Library":
    st.subheader("📚 Your Library")
    # Code to view the library
elif menu == "Statistics":
    st.subheader("📊 Library Statistics")
    # Code to display statistics
console.py
Load Library: Function to load the library data from library.txt.

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
Add Book: Function to add a new book to the library.

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
Remove Book: Function to remove a book from the library.

def remove_book():
    title = input("\nEnter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"{title} removed successfully!")
            return
    print(f"Sorry, {title} is not in the library.")
Search: Function to search for a book by title or author.

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
Display All: Function to display all books in the library.

def display_all():
    print("\nYour Library:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print("")
Display Stats: Function to display statistics about the library.

def display_stats():
    total_books = len(library)
    total_read_books = len([book for book in library if book["read"]])
    print(f"Total books: {total_books}")
    print(f"Percentage read: {(total_read_books / total_books) * 100}%")
Save Library: Function to save the library data to library.txt.

' def save_library():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n") '
* Main Function: The main function to run the console application.

' def main():
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
    main() '
