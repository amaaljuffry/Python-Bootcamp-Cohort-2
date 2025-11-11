from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongo_uri = os.getenv("MONGO_ATLAS_CLUSTER_URI")
client = MongoClient(mongo_uri)

# Source and target DB names
source_db = client["blog_db"]
target_db = client["example_db"]

# Get all collections in source DB
collections = source_db.list_collection_names()

for col_name in collections:
    source_col = source_db[col_name]
    target_col = target_db[col_name]

    # Copy all documents from source to target
    docs = list(source_col.find())
    if docs:
        target_col.insert_many(docs)
        print(f"Copied {len(docs)} documents from '{col_name}'")

print("✅ Migration complete!")

client.drop_database("blog_db")
print("✅ blog_db deleted")


client.close()
