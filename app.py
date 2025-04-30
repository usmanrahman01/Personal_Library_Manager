import streamlit as st

def load_library():
    library = []
    with open("library.txt", "r") as file:
        for line in file:
            title, author, year, genre, read = line.strip().split(",")
            library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read": read == "True"})
    return library

library = load_library()
def save_library():
    with open("library.txt", "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n")

st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("📌 Menu", ["Add Book", "Remove Book", "Search Book", "View Library", "Statistics"])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")

    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author")
    year = st.number_input("Enter Publication Year", min_value=0, step=1)
    genre = st.text_input("Enter Genre")
    read = st.radio("Have you read this book?", ["Yes", "No"])

    if st.button("Add Book"):
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read == "Yes"
        }
        library.append(book)
        save_library()
        st.success(f"✅ '{title}' added successfully!")

elif menu == "Remove Book":
    st.subheader("🗑️ Remove a Book")

    book_titles = [f'{book["title"]} by {book["author"]}' for book in library]
    selected_book = st.selectbox("Select a book to remove", book_titles)

    if st.button("Remove Book"):
        # Extract the title from the selected book string
        title = selected_book.split(" by ")[0]
        for book in library:
            if book["title"].lower() == title.lower():
                library.remove(book)
                save_library()
                st.success(f"✅ '{title}' removed successfully!")
                break
        else:
            st.error(f"❌ Sorry, '{title}' is not in the library.")

elif menu == "Search Book":
    st.subheader("🔍 Search for a Book")

    search_by = st.radio("Search by:", ["Title", "Author"])
    if search_by == "Title":
        search_query = st.text_input("Enter the title")
    elif search_by == "Author":
        search_query = st.text_input("Enter the author")

    if st.button("Search"):
        found_books = [book for book in library if search_by == "Title" and search_query.lower() in book["title"].lower() or search_by == "Author" and search_query.lower() in book["author"].lower()]

        if found_books:
            for book in found_books:
                st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.error("❌ No books found.")

elif menu == "View Library":
    st.subheader("📚 Your Library")

    if not library:
        st.warning("No books in your library.")
    else:
        for index, book in enumerate(library):
            st.write(f"📖 **{index + 1}. {book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")

elif menu == "Statistics":
    st.subheader("📊 Library Statistics")

    total_books = len(library)
    total_read = len([book for book in library if book["read"]])
    percentage_read = (total_read / total_books) * 100 if total_books > 0 else 0

    st.write(f"📖 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {total_read}")
    st.write(f"📊 **Percentage Read:** {percentage_read}%")
