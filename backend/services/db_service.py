# backend/services/db_service.py
import os
from pymongo import MongoClient
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/") # Fallback to local
client = MongoClient(MONGO_URI)

# Create/Select the database and collection
db = client.learning_path_db
cache_collection = db.search_cache

# Cache expiration time (e.g., 7 days)
CACHE_EXPIRATION_DAYS = 15

def get_cached_path(query):
    """Checks if a fresh learning path exists in the database."""
    query_slug = query.lower().strip()
    
    cached_doc = cache_collection.find_one({"query": query_slug})
    
    if cached_doc:
        # Check if the cache is expired
        last_updated = cached_doc.get("last_updated")
        if last_updated:
            expiration_date = last_updated + timedelta(days=CACHE_EXPIRATION_DAYS)
            if datetime.utcnow() < expiration_date:
                print(f"✅ Cache HIT for '{query}'! Saved 100 API Units.")
                # Remove the MongoDB internal _id before returning to frontend
                cached_doc.pop('_id', None) 
                return cached_doc
        
        print(f"⚠️ Cache STALE for '{query}'. Re-fetching...")
    else:
        print(f"❌ Cache MISS for '{query}'. Fetching from APIs...")
        
    return None

def save_to_cache(query, structured_path):
    """Saves or updates a learning path in the database."""
    query_slug = query.lower().strip()
    
    document = {
        "query": query_slug,
        "last_updated": datetime.utcnow(),
        "learning_path": structured_path
    }
    
    # upsert=True means it will update if it exists, or insert if it doesn't
    cache_collection.update_one(
        {"query": query_slug},
        {"$set": document},
        upsert=True
    )
    print(f"💾 Saved new path for '{query}' to MongoDB.")