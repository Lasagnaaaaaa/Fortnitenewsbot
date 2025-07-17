import feedparser
import requests
import time

# Your Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_here'

# Fortnite RSS feed
FEED_URL = 'https://www.fortnite.com/news/rss'

# To keep track of what we've already posted
seen_entries = set()

def post_to_discord(title, link):
    data = {
        "content": f"📰 **{title}**\n{link}"
    }
    requests.post(WEBHOOK_URL, json=data)

def check_feed():
    feed = feedparser.parse(FEED_URL)
    for entry in feed.entries:
        if entry.id not in seen_entries:
            post_to_discord(entry.title, entry.link)
            seen_entries.add(entry.id)

# Run every 10 minutes
while True:
    check_feed()
    time.sleep(600)  # Wait 10 mins (600 seconds)
