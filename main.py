"""Cloud Function to pull events from Somerville Meeting Calendar."""

import feedparser 

def get_events(request):
    """Get events from Somerville Meeting Calendar."""
    url = "http://somervillecityma.iqm2.com/Services/RSS.aspx?Feed=Calendar"
    feed = feedparser.parse(url)
    for entry in feed["entries"]:
        print(entry["title"])

if __name__ == "__main__":
    get_events(None)
