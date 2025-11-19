import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    response = requests.get(url)
    content = response.text
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)
    hrefs = []
    return hrefs

if __name__ == "__main__":
    url = input("Zadej URL:")
    try:
        links = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for l in links:
            print(l)
    except Exception as e:
        print(f"Program skončil chybou: {e}")