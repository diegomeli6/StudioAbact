#!/usr/bin/env python3
"""
Download remaining 6 photographers using open mirrors with polite delay to avoid rate-limiting.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import ssl

DEST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "assets", "corsi", "dapl08", "anno-1", "fotografia-digitale", "images")
os.makedirs(DEST_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 (Academic study project)"
ctx = ssl._create_unverified_context()

REMAINING = [
    ("eggleston_color.jpg", ["William Eggleston", "Eggleston Red Ceiling", "William Eggleston Memphis"]),
    ("parr_last_resort.jpg", ["Martin Parr", "Martin Parr photographer", "Martin Parr New Brighton"]),
    ("van_agtmael_disco_night.jpg", ["Peter van Agtmael", "Peter van Agtmael photographer", "Van Agtmael Magnum"]),
    ("guidi_in_veneto.jpg", ["Guido Guidi", "Guido Guidi fotografo", "Guido Guidi In Veneto"]),
    ("ventura_winter_stories.jpg", ["Paolo Ventura", "Paolo Ventura Winter Stories", "Paolo Ventura fotografo"]),
    ("hido_house_hunting.jpg", ["Todd Hido", "Todd Hido House Hunting", "Todd Hido photographer"]),
]

def search_wikimedia_api(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        time.sleep(2)  # Polite delay
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for pid, p in pages.items():
                infos = p.get("imageinfo", [])
                if infos and "url" in infos[0]:
                    img_url = infos[0]["url"]
                    if img_url.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                        # Avoid svgs or logos
                        if "logo" not in img_url.lower() and "icon" not in img_url.lower():
                            return img_url
    except Exception as e:
        print(f"Error querying {query}: {e}")
    return None

def download_file(url, out_path):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        time.sleep(2)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = resp.read()
            if len(data) < 5000:
                return False
            with open(out_path, "wb") as f:
                f.write(data)
            print(f"[OK] Scaricato {os.path.basename(out_path)} ({len(data)//1024} KB)")
            return True
    except Exception as e:
        print(f"[FAIL] Download {url}: {e}")
        return False

def main():
    for filename, queries in REMAINING:
        target = os.path.join(DEST_DIR, filename)
        if os.path.exists(target) and os.path.getsize(target) > 5000:
            print(f"[SKIP] Gia presente: {filename}")
            continue

        found = False
        for q in queries:
            print(f"Ricerca per '{q}'...")
            img_url = search_wikimedia_api(q)
            if img_url:
                print(f"Trovato: {img_url}")
                if download_file(img_url, target):
                    found = True
                    break
        if not found:
            print(f"[ATTENZIONE] Nessun file reperito per {filename}")

if __name__ == "__main__":
    main()
