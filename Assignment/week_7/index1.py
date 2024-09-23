# List of books and users
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Available"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Checked Out"},
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": []},
]

def main_menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View All Users")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            view_users()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def view_books():
    print("\n--- All Books ---")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Status: {book['status']}")

def view_users():
    print("\n--- All Users ---")
    for user in users:
        borrowed_titles = [b['title'] for b in books if b['id'] in user['borrowed_books']]
        print(f"ID: {user['id']}, Name: {user['name']}, Borrowed Books: {borrowed_titles if borrowed_titles else 'None'}")

def borrow_book():
    try:
        user_id = int(input("Enter user ID: "))
        book_id = int(input("Enter book ID: "))
        
        user = next((u for u in users if u['id'] == user_id), None)
        book = next((b for b in books if b['id'] == book_id), None)
        
        if user and book:
            if book['status'] == "Available":
                book['status'] = "Checked Out"
                user['borrowed_books'].append(book_id)
                print(f"Book '{book['title']}' borrowed by {user['name']}.")
            else:
                print(f"Book '{book['title']}' is already checked out.")
        else:
            print("Invalid user ID or book ID.")
    except ValueError:
        print("Please enter valid numeric IDs.")

def return_book():
    user_id = int(input("Enter user ID: "))
    book_id = int(input("Enter book ID: "))
    
    user = next((u for u in users if u['id'] == user_id), None)
    book = next((b for b in books if b['id'] == book_id), None)
    
    if user and book:
        if book["status"] == "Checked Out":
            book["status"] = "Available"  # Update book status
            user["borrowed_books"].remove(book["id"])  # Remove book ID from borrowed_books
            print(f"The user {user['name']} returned the book '{book['title']}'.")
        else:
            print(f"Sorry, the book '{book['title']}' is not checked out.")
    else:
        print("Invalid book or user ID.")

main_menu()
