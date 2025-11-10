# Date: 2025-11-10
# SQLite in Python

# SQLite is a lightweight database engine that doesn't require a server process.
# It's a good choice for small applications and embedded systems.

# SQLite is a relational database management system that can be used in a variety of applications.

# SQLite is a good choice for small applications and embedded systems.

# SQLite is a good choice for small applications and embedded systems.

# SQLite is a good choice for small applications and embedded systems.

#Basic commands:
# 1. CREATE Create a database
# 2. INSERT Insert data into a table
# 3. SELECT Select data from a table
# 4. UPDATE Update data in a table
# 5. DELETE Delete data from a table

import sqlite3

class DatabaseManager:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT NOT NULL,
                content TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            ''')

# Create Data (INSERT)

    def create_user(self, username, email, age):
        """Create a user in the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO users (username, email, age) VALUES (?, ?, ?)
            ''', (username, email, age))
            return cursor.lastrowid
    
    def create_post(self, user_id, title, content):
        """Create a product in the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO products (user_id, title, content) VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid
    
# Read Data (SELECT)

    def get_all_users(self):
        """Get all users from the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

    def get_user_posts(self, user_id):
        """Get all posts for a user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products WHERE user_id = ?', (user_id,))
            return cursor.fetchall()
    
# Delete Data (DELETE)

    def delete_user(self, user_id):
        """Delete a user from the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount
    
    def delete_post(self, post_id):
        """Delete a post from the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM products WHERE id = ?', (post_id,))
            return cursor.rowcount

# Run on Terminal:
def display_menu():
    """Display the menu"""
    print("\n--- SQLite Database Manager ---")
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Delete User")
    print("6. Exit")
    print("-"*40)

def main():
    """Main interactive CLI Function"""
    db = DatabaseManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Create User ---")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"User created successfully with ID: {user_id}")
                else:
                    print("Failed to create user.")
            except ValueError:
                print("Invalid age. Please enter a valid age.")

        elif choice == "2":
            print("\n--- View All Users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")
            else:
                print("No users found.")
        
        elif choice == "3":
            print("\n--- Create Post ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"Post created successfully with ID: {post_id}")
                else:
                    print("Failed to create post.")
            except ValueError:
                print("Invalid user ID. Please enter a valid number.")
        
        elif choice == "4":
            print("\n--- View User Posts ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"\nPost ID:{post[0]}")
                        print(f"Title: {post[1]}")
                        print(f"Content: {post[2]}")
                        print(f"Created At: {post[3]}")
                        print("-"*30)
                else:
                    print("No posts found for this user.")
            except ValueError:
                print("Invalid user ID. Please enter a valid number.")
        
        elif choice == "5":
            print("\n--- Delete User ---")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete user {user_id}? (y/n): ").strip().lower()
                if confirm == "y":
                    if db.delete_user(user_id):
                        print(f"User {user_id} deleted successfully.")
                    else:
                        print(f"User {user_id} not found.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Invalid user ID. Please enter a valid number.")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
