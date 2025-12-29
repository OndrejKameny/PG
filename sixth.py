import sys
import requests
import re
from urllib.parse import urljoin

def download_url_and_get_all_hrefs(url):
    response = requests.get(url)
    content = response.text

    raw_hrefs = re.findall(r'href\s*=\s*"([^"]+)"', content)

    hrefs = []
    for href in raw_hrefs:
        if not href:
            continue
        if href.startswith("#"):
            continue
        
        full_url = urljoin(url, href)
        hrefs.append(full_url)

    return hrefs

if __name__ == "__main__":
    url = input("Zadej URL:")

    if not url.startswith("https://") and not url.startswith("https://"):
        url = "https://" + url
    try:
        links = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for l in links:
            print(l)
    except Exception as e:
        print(f"Program skončil chybou: {e}")