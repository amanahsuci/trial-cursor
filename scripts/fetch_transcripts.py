from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import time

VIDEO_LIST = [
    # Sam Oh / Ahrefs — interview di SaaS SEO Show
    ("P-ooyBFUte0", "sam-oh-ahrefs", "video-content-strategy-b2b-saas"),

    # Dave Gerhardt — sudah berhasil, pertahankan
    ("S3jOSiE6l80", "dave-gerhardt", "content-community-building-200k-b2b-audience"),

    # Ross Simmonds — sudah berhasil, pertahankan
    ("8lQfWBFF45U", "ross-simmonds", "b2b-content-social-media-strategy"),

    # Rand Fishkin — sudah berhasil, pertahankan
    ("vthgW-oBLmU", "rand-fishkin", "5-big-marketing-trends-2024"),

    # Lenny Rachitsky — behind the scenes building newsletter & podcast
    ("HEqrvF7ztBE", "lenny-rachitsky", "building-newsletter-and-podcast-from-scratch"),

    # Peep Laja — how to win beyond the product
    ("UddBHQ0PuTg", "peep-laja", "how-to-win-beyond-the-product"),

    # Wes Bush — product led growth masterclass
    ("16L-UYXq6Vs", "wes-bush", "product-led-growth-masterclass"),

    # Dan Martell — SaaS scaling dan YouTube strategy
    ("sBZmzlJu8oM", "dan-martell", "secret-to-running-saas-business"),

    # Kyle Poyar — deliver value before customer buys
    ("owG-HOg6AqA", "kyle-poyar", "deliver-value-before-customer-buys-plg"),

    # Tim Soulo — inside Ahrefs $100M growth (via Ross Simmonds channel)
    ("Nw-HgjJClpM", "tim-soulo-ahrefs", "inside-ahrefs-100m-growth-content-seo"),
]

OUTPUT_DIR = Path("research/youtube-transcripts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def fetch_transcript(video_id):
    try:
        ytt = YouTubeTranscriptApi()
        fetched = ytt.fetch(video_id, languages=["en", "en-US"])
        return " ".join([s.text for s in fetched.snippets])
    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def save_transcript(video_id, expert, title, text):
    filename = OUTPUT_DIR / f"{expert}_{title}.md"
    content = f"""# Transcript: {title.replace('-', ' ').title()}

**Expert:** {expert}
**Video ID:** {video_id}
**URL:** https://www.youtube.com/watch?v={video_id}

---

{text}
"""
    filename.write_text(content, encoding="utf-8")
    print(f"  Saved -> {filename}")


print(f"Fetching {len(VIDEO_LIST)} transcripts...\n")
success, failed = 0, []

for video_id, expert, title in VIDEO_LIST:
    print(f"[{expert}] {title}")
    text = fetch_transcript(video_id)
    if text:
        save_transcript(video_id, expert, title, text)
        success += 1
    else:
        failed.append((video_id, expert, title))
    time.sleep(1)

print(f"\nDone: {success}/{len(VIDEO_LIST)} berhasil")
if failed:
    print("Gagal:")
    for v, e, t in failed:
        print(f"  - {e}: https://www.youtube.com/watch?v={v}")
