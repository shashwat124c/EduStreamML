import os
import html
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_youtube_resources(query, max_results=5):
    """
    Fetches videos from YouTube and normalizes them into our standard schema.
    """
    if not YOUTUBE_API_KEY:
        raise ValueError("YouTube API key not found. Check your .env file.")

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    normalized_results = []

    try:
        # Call the search.list method
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results,
            videoCaption='any', # Good for educational content
            relevanceLanguage='en'
        )
        response = request.execute()

        # Normalize the data for our ML model and Frontend
        for item in response.get('items', []):
            video_id = item['id']['videoId']
            snippet = item['snippet']
            
            # Clean up HTML entities in titles (e.g., &amp; -> &)
            clean_title = html.unescape(snippet['title'])
            clean_desc = html.unescape(snippet['description'])

            resource = {
                "title": clean_title,
                "description": clean_desc,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "thumbnail": snippet['thumbnails']['high']['url'],
                "source": "youtube",
                "metadata": {
                    "channel_title": snippet['channelTitle'],
                    "published_at": snippet['publishedAt']
                }
                # Note: We will add an "ml_difficulty" key here later!
            }
            normalized_results.append(resource)

        return normalized_results

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return []

# --- TEST RUNNER ---
# This allows you to test the script directly without Flask
if __name__ == "__main__":
    print("Testing YouTube API Integration...\n")
    topic = input("Enter a topic to learn (e.g., 'React Hooks'): ")
    
    print(f"\nFetching resources for '{topic}'...")
    results = fetch_youtube_resources(topic, max_results=3) # Fetching 3 just for a quick test
    
    for i, res in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"Title: {res['title']}")
        print(f"URL: {res['url']}")
        print(f"Description snippet: {res['description'][:100]}...")