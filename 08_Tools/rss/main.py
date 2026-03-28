import feedparser

# URL ของ RSS Feed
rss_url = "https://news.ycombinator.com/rss"

# ดึง feed
feed = feedparser.parse(rss_url)

# แสดงหัวข้อข่าวล่าสุด 5 รายการ
for entry in feed.entries[:5]:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print("-" * 50)
