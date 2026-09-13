#!/usr/bin/env python3
"""
Script per scaricare e verificare i capolavori d'arte contemporanea autentici
per Storia dell'Arte 1 e 2.
Regola imperativa: ZERO EMOJI.
"""

import os
import sys
import json
import re
import urllib.request
import urllib.parse
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_ARTE1 = os.path.join(BASE_DIR, "assets", "corsi", "dapl08", "anno-1", "storia-arte-1", "images")
DIR_ARTE2 = os.path.join(BASE_DIR, "assets", "corsi", "dapl08", "anno-2", "storia-arte-2", "images")

os.makedirs(DIR_ARTE1, exist_ok=True)
os.makedirs(DIR_ARTE2, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 StudioArteAcademic/1.0"
}

def download_file(url, filepath):
    """Scarica e convalida l'immagine."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read()
            if len(content) < 8000:
                print(f"[ERRORE] File troppo piccolo ({len(content)} byte): {url}")
                return False
            with open(filepath, "wb") as f:
                f.write(content)
        with Image.open(filepath) as img:
            w, h = img.size
            if w < 150 or h < 150:
                print(f"[ERRORE] Risoluzione insufficiente ({w}x{h}): {filepath}")
                os.remove(filepath)
                return False
            print(f"[OK] Salvato {os.path.basename(filepath)} ({w}x{h}, {len(content)//1024} KB)")
        return True
    except Exception as e:
        print(f"[ERRORE] Download fallito da {url}: {e}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return False

def get_wiki_rest_image(title, lang="en"):
    """Cerca su Wikipedia REST API l'immagine di un'opera."""
    clean_title = urllib.parse.unquote(title).replace(" ", "_")
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(clean_title)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("originalimage", {}).get("source") or data.get("thumbnail", {}).get("source")
    except Exception:
        return None

def get_wikiart_image(artist, title):
    """Estrae l'immagine dell'opera da WikiArt."""
    url = f"https://www.wikiart.org/en/{artist}/{title}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")
            m = re.search(r'itemprop=["\']image["\']\s+src=["\']([^"\']+)["\']', html)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None

if __name__ == "__main__":
    print("Inizializzazione catalogo opere d'arte...")
