#!/usr/bin/env python3
"""
Script per scaricare e sostituire le immagini errate (ritratti di artisti anziché opere d'arte)
in Storia dell'Arte 1 e 2 con fotografie autentiche delle opere da musei, archivi o Wikimedia Commons.
Regola: ZERO EMOJI.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_ARTE1 = os.path.join(BASE_DIR, "assets", "corsi", "dapl08", "anno-1", "storia-arte-1", "images")
DIR_ARTE2 = os.path.join(BASE_DIR, "assets", "corsi", "dapl08", "anno-2", "storia-arte-2", "images")

# Elenco delle opere errate da sostituire con le rispettive fonti su Wikimedia Commons o archivi pubblici
ARTWORKS_TO_FIX = [
    # 1. Michelangelo Pistoletto, Quadro Specchiante (Uomo nudo di schiena, 1962-87)
    {
        "target": os.path.join(DIR_ARTE1, "pistoletto_quadro_specchiante.jpg"),
        "title": "Michelangelo Pistoletto, Quadro specchiante",
        "wiki_commons_file": "File:Michelangelo_pistoletto,_uomo_nudo_di_schiena,_1962-87,_01.jpg"
    },
    # 2. Daniel Buren, In Situ / Les Deux Plateaux (installazione a strisce alternate)
    {
        "target": os.path.join(DIR_ARTE1, "buren_in_situ.jpg"),
        "title": "Daniel Buren, In Situ (Les Deux Plateaux, Colonnes de Buren)",
        "wiki_commons_file": "File:Cour_d%27honneur_du_Palais-Royal_12.jpg"
    },
    # 3. Sol LeWitt, Struttura modulare / Serial Project (Cubi modulari aperti)
    {
        "target": os.path.join(DIR_ARTE1, "lewitt_serial_project.jpg"),
        "title": "Sol LeWitt, Modular Cube Structure",
        "wiki_commons_file": "File:Sol_LeWitt_White_Cubes.jpg"
    },
    # 4. Allan Kaprow, Yard (Ambiente con pneumatici)
    {
        "target": os.path.join(DIR_ARTE1, "kaprow_yard.jpg"),
        "title": "Allan Kaprow, Yard (Ambiente di copertoni)",
        "wiki_commons_file": "File:Allan_Kaprow_Yard_Hauser_and_Wirth.jpg"
    },
    # 5. Carl Andre, Equivalent VIII (I mattoni refrattari alla Tate)
    {
        "target": os.path.join(DIR_ARTE1, "andre_floor_pieces.jpg"),
        "title": "Carl Andre, Equivalent VIII (Firebricks)",
        "wiki_commons_file": "File:Carl_Andre_Equivalent_VIII.jpg"
    },
    # 6. Man Ray, Cadeau (Il Dono - ferro da stiro con chiodi)
    {
        "target": os.path.join(DIR_ARTE1, "man_ray_indestructible_object.jpg"),
        "title": "Man Ray, Cadeau (Il Dono, 1921)",
        "wiki_commons_file": "File:Cadeau_by_Man_Ray,_1921.jpg"
    },
]

def get_wikimedia_image_url(file_name):
    """Interroga l'API di Wikimedia Commons per ottenere l'URL dell'immagine scalata a 1200px."""
    api_url = (
        "https://commons.wikimedia.org/w/api.php?action=query"
        f"&titles={urllib.parse.quote(file_name)}"
        "&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = urllib.request.Request(api_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for pid, pdata in pages.items():
                if "imageinfo" in pdata and len(pdata["imageinfo"]) > 0:
                    info = pdata["imageinfo"][0]
                    return info.get("thumburl") or info.get("url")
    except Exception as e:
        print(f"Errore query API per {file_name}: {e}")
    return None

def download_and_verify(url, target_path, min_bytes=10000):
    """Scarica il file e verifica che sia una valida immagine JPG/PNG."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
            if len(data) < min_bytes:
                print(f"File troppo piccolo ({len(data)} byte) da {url}")
                return False
            
            temp_path = target_path + ".tmp"
            with open(temp_path, "wb") as f:
                f.write(data)
                
            # Verifica con PIL
            with Image.open(temp_path) as img:
                w, h = img.size
                format_name = img.format
                if w < 200 or h < 200:
                    print(f"Risoluzione troppo bassa ({w}x{h})")
                    os.remove(temp_path)
                    return False
            
            # Sostituisci il file definitivo
            if os.path.exists(target_path):
                os.remove(target_path)
            os.rename(temp_path, target_path)
            print(f"OK: Aggiornato {os.path.basename(target_path)} ({w}x{h}, {len(data)//1024} KB)")
            return True
    except Exception as e:
        print(f"Errore download {url}: {e}")
        return False

def main():
    print("Inizio correzione immagini errate...")
    success_count = 0
    for item in ARTWORKS_TO_FIX:
        print(f"\nElaborazione: {item['title']}")
        file_name = item["wiki_commons_file"]
        img_url = get_wikimedia_image_url(file_name)
        if not img_url:
            print(f"Impossibile trovare URL per {file_name}")
            continue
        print(f"URL trovato: {img_url}")
        if download_and_verify(img_url, item["target"]):
            success_count += 1
            
    print(f"\nOperazione completata: {success_count}/{len(ARTWORKS_TO_FIX)} immagini aggiornate con successo.")

if __name__ == "__main__":
    main()
