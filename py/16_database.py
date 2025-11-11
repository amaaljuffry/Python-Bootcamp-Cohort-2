# Date: 2025-11-11
# Database in Python

from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

mongo_uri = os.getenv("MONGO_ATLAS_CLUSTER_URI")


class DatabaseManager:
    def __init__(self, db_name='example_db'):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.users_collection = self.db["users"]
        self.posts_collection = self.db["posts"]
        self.init_database()

    def init_database(self):
        """Initialize the database with collections and indexes"""
        # Create unique index on email for users
        self.users_collection.create_index("email", unique=True)
        # Create index on user_id for posts for better query performance
        self.posts_collection.create_index("user_id")

        #Create Functions
    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            user_doc = {
            "name": name,
            "email": email,
            "age": age,
            "created_at": datetime.now()
            }
            result = self.users_collection.insert_one(user_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    def create_post(self, user_id, title, content):
        """Create a new post"""
        try:
            # Convert string user_id to ObjectId if it's a valid ObjectID
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            post_doc = {
            "user_id": user_object_id,
            "title": title,
            "content": content,
            "created_at": datetime.now()
            }
            result = self.posts_collection.insert_one(post_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return None

# Read Functions
    def get_all_users(self):
        """Get all users"""
        try:
            users = list(self.users_collection.find())
            # Convert ObjectId to string for JSON serialization
            for user in users:
                user["_id"] = str(user["_id"])
            return users
        except Exception as e:
            print(f"Error fetching all users: {e}")
            return []
        
    def get_user_posts(self, user_id):
        """Get all posts for a user"""
        try:
            #Convert string user_id to ObjectId if it's a valid ObjectID
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
                
            posts = list(self.posts_collection.find({"user_id": user_object_id}).sort("created_at", -1))
            # Convert ObjectId to string for JSON serialization
            for post in posts:
                post["_id"] = str(post["_id"])
            return posts
        except Exception as e:
            print(f"Error fetching user posts: {e}")
            return []
        
    #Delete Functions
    def delete_user(self, user_id):
        """Delete a user"""
        try:
            #Convert string user_id to ObjectId if it's a valid ObjectID
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id
                
            #Delete user's posts first
            self.posts_collection.delete_many({"user_id": user_object_id})

            #Delete the user
            result = self.users_collection.delete_one({"_id": user_object_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
    def close_db(self):
        """Close the Mongodb connection"""
        self.client.close()

#Run on Terminal Functions

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("MongoDB Database Manager")
    print("="*40)
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Delete User")
    print("6. Exit")
    print("-"*40)

def main():
    """Main Interactive CLI function"""
    try:
        db = DatabaseManager("example_db")
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        print("Make sure MongoDB is running on localhost:27017")
        return
    
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
                    print(f"ID: {user['_id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}")
            else:
                print("No users found.")
        elif choice == "3":
            print("\n--- Create New Post ---")
            user_id = input("Enter user ID: ").strip()
            title = input("Enter post title: ").strip()
            content = input("Enter post content: ").strip()
            post_id = db.create_post(user_id, title, content)
            if post_id:
                print(f"Post created successfully with ID: {post_id}")
            else:
                print("Failed to create post.")
        elif choice == "4":
            print("\n--- View User Posts ---")
            user_id = input("Enter user ID: ").strip()
            try:
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"\nID: {post['_id']}")
                        print(f"Title: {post['title']}")
                        print(f"Content: {post['content']}")
                        print(f"Created At: {post['created_at']}")
                        print("-"*30)
                else:
                    print("No posts found for this user.")
            except ValueError:
                print("Invalid user ID. Please enter a valid user ID.")
        elif choice == "5":
            print("\n--- Delete User ---")
            user_id = input("Enter user ID: ").strip()
            confirm = input(f"Are you sure you want to delete user {user_id}? (y/n): ").strip().lower()
            if confirm == "y":
                if db.delete_user(user_id):
                    print(f"User {user_id} deleted successfully.")
                else:
                    print(f"User {user_id} not found.")
            else:
                print("Deletion cancelled.")
        elif choice == "6":
            print("\nClosing MongoDB connection...")
            db.close_db()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
   main()

