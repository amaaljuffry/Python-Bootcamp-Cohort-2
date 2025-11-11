from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load your MongoDB Atlas connection string
load_dotenv()
mongo_uri = os.getenv("MONGO_ATLAS_CLUSTER_URI")

# Connect to your MongoDB Atlas cluster
client = MongoClient(mongo_uri)

# List all databases before deletion
print("📋 Databases before deletion:")
print(client.list_database_names())

# Drop the unwanted database
client.drop_database("test_db")

print("\n✅ 'test_db' has been deleted successfully!")

# List all databases after deletion
print("\n📋 Databases after deletion:")
print(client.list_database_names())

# Close the connection
client.close()
