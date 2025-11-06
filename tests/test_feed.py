import re
from time import mktime
from datetime import datetime, timezone
import feedparser

FEEDS = {
    "gdansk_wiadomosci": "https://www.gdansk.pl/subpages/rss/wiadomosci_rss.xml",
    "gdansk_komunikaty": "https://www.gdansk.pl/subpages/rss/komunikaty_rss.xml",
}

IMG_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

def first_image_url(entry) -> str | None:
    # пробуем description, потом content:encoded
    for key in ("summary", "content", "description"):
        val = entry.get(key)
        if isinstance(val, list) and val:
            # feedparser может класть content как список словарей
            val = val[0].get("value", "")
        val = val or ""
        m = IMG_RE.search(val)
        if m:
            return m.group(1)
    return None

def ts(entry) -> str:
    # ISO8601 для наглядности; если нет даты — now()
    t = entry.get("published_parsed") or entry.get("updated_parsed")
    dt = datetime.fromtimestamp(mktime(t), tz=timezone.utc) if t else datetime.now(tz=timezone.utc)
    return dt.isoformat(timespec="seconds")

def inspect(feed_id: str, url: str, limit: int = 3):
    print(f"\n=== {feed_id} === {url}")
    feed = feedparser.parse(url)
    for e in feed.entries[:limit]:
        link = e.get("link") or e.get("id")
        title = e.get("title") or "(no title)"
        img = first_image_url(e)
        print("-" * 60)
        print("title:", title)
        print("link :", link)
        print("time :", ts(e))
        print("img  :", img or "—")

if __name__ == "__main__":
    for fid, url in FEEDS.items():
        inspect(fid, url, limit=3)
