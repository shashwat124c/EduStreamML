import os
import requests
from pymongo import MongoClient
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.learning_path_db
modules_collection = db.modules

# Check for API Key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# Trusted Educational Channels Whitelist
TRUSTED_CHANNELS = {
    "freeCodeCamp": "UC8butISFwT-Wl7EV0hUK0BQ",
    "Net Ninja": "UCW5YeuERMmlnqo4oq8vwUpg",
    "Traversy Media": "UC29ju8bIPH5as8OGnQzwJyA"
}

def search_channel(channel_id, query):
    """Hits the YouTube Data API for a single channel."""
    print(f"    🔍 Searching channel {channel_id} for '{query}'...")
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "channelId": channel_id,
        "maxResults": 3, # Grab top 3 from each channel
        "type": "video",
        "key": YOUTUBE_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "items" in data:
            return data["items"]
        else:
            print(f"      [!] API Error or Quota exceeded: {data}")
            return []
    except Exception as e:
        print(f"      [!] Error fetching from youtube: {e}")
        return []

def automate_content_sourcing():
    if not YOUTUBE_API_KEY:
        print("🚨 ERROR: YOUTUBE_API_KEY environment variable not found.")
        print("Please create a .env file in the backend directory containing:")
        print("YOUTUBE_API_KEY=your_key_here")
        return

    modules = list(modules_collection.find({}))
    print(f"🚀 Starting Automated Content Sourcing for {len(modules)} modules...\n")

    for module in modules:
        # Create a highly targeted query (e.g. "React React Components tutorial")
        query = f"{module.get('course', '')} {module.get('name', '')} tutorial"
        print(f"📚 Sourcing videos for module: {module['name']} ({module['topic_id']})")
        
        aggregated_results = []
        
        # Search across all whitelisted channels
        for channel_name, channel_id in TRUSTED_CHANNELS.items():
            results = search_channel(channel_id, query)
            aggregated_results.extend(results)
            
        # We need at least 2 videos (1 primary, 1 fallback)
        if len(aggregated_results) >= 2:
            # We will just take the top 2 hits. 
            # In the future, you could implement complex ranking heuristics here based on view_count or recency!
            primary_video_id = aggregated_results[0]["id"]["videoId"]
            fallback_video_id = aggregated_results[1]["id"]["videoId"]
            
            primary_url = f"https://www.youtube.com/watch?v={primary_video_id}"
            fallback_url = f"https://www.youtube.com/watch?v={fallback_video_id}"
            
            print(f"    ✅ Found Primary: {primary_url}")
            print(f"    ✅ Found Fallback: {fallback_url}")
            
            # Update the database
            modules_collection.update_one(
                {"_id": module["_id"]},
                {"$set": {
                    "primary_video_url": primary_url,
                    "fallback_video_url": fallback_url
                }}
            )
            print("    💾 Successfully updated MongoDB.")
        else:
            print(f"    ❌ Not enough videos found across whitelisted channels for '{query}'. Kept old dummy URLs.")
            
        print("-" * 50)

    print("\n🎉 Automated Sourcing Complete!")

if __name__ == "__main__":
    automate_content_sourcing()
