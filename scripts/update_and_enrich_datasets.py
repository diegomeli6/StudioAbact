#!/usr/bin/env python3
"""
Script per arricchire e aggiornare data/arte1-data.js e data/arte-data.js.
Sostituisce tutte le immagini errate (scansioni libro) con le opere d'arte autentiche.
Aggiunge apparati iconografici ricchi e didatticamente ineccepibili in tutti i capitoli.
REGOLA ASSOLUTA: ZERO EMOJI in ogni punto.
"""

import os
import sys
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_arte2():
    path = os.path.join(BASE_DIR, "data", "arte-data.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Sostituzioni capitolo 42 (Hirst & YBAs)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_p1_0.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_shark.jpg")
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_p1_1.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/emin_my_bed.jpg")
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_p2_0.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_shark.jpg")
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_p3_0.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/hirst_skull_diamond.jpg")

    # Sostituzioni capitolo 45 (Olafur Eliasson)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_p1_0.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_weather_project.jpg")
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_work_1.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_weather_project.jpg")
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_p4_0.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/eliasson_weather_project.jpg")

    # Sostituzioni capitolo 46 (Miguel Chevalier)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/chevalier_pixels_p1_0.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/chevalier_pixels.jpg")
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/chevalier_work_3.png",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/chevalier_surnatures.jpg")

    # Sostituzione capitolo 9 (Middendorf -> Baselitz)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/middendorf_peep_show.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/baselitz_ragazze_olmo.jpg")

    # Sostituzione capitolo 10 (Kiefer Sulamith)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/kiefer_high_priestess.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/kiefer_sulamith.jpg")

    # Sostituzione capitolo 15 (Cindy Sherman Film Still)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/sherman_untitled_175.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/sherman_film_still_21.jpg")

    # Sostituzione capitolo 18 (Jeff Koons Balloon Dog)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/koons_equilibrium.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/koons_balloon_dog.jpg")

    # Sostituzione capitolo 27 (Matthew Barney)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/barney_blind_peril.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/barney_cremaster.jpg")

    # Sostituzione capitolo 40 (Gregor Schneider)
    content = content.replace("assets/corsi/dapl08/anno-2/storia-arte-2/images/schneider_totes_haus.jpg",
                              "assets/corsi/dapl08/anno-2/storia-arte-2/images/schneider_totes_haus.jpg")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Aggiornato data/arte-data.js con successo!")

def update_arte1():
    path = os.path.join(BASE_DIR, "data", "arte1-data.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Carica JSON
    idx = content.find('[')
    end_idx = content.rfind(']')
    prefix = content[:idx]
    suffix = content[end_idx+1:]
    chapters = json.loads(content[idx:end_idx+1])

    # Mappatura immagini per i capitoli privi di immagine in Storia 1
    new_images = {
        "arte1-c9": (
            "Franz Kline, Chief, 1950 - Olio su tela, 148 x 209 cm, The Museum of Modern Art (MoMA), New York",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/kline_chief.jpg",
            "La monumentale impalcatura nero-bianca esprime la forza tensiva e costruttiva del gesto pittorico di Franz Kline, lontano da ogni intento calligrafico per farsi struttura architettonica pura."
        ),
        "arte1-c10": (
            "Mark Rothko, Four Darks in Red, 1958 - Olio su tela, Whitney Museum of American Art, New York",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/rothko_color_field.jpg",
            "Le campiture cromatiche fluttuanti e i margini sfumati invitano l'osservatore a un'esperienza contemplativa di pura risonanza spirituale ed emotiva."
        ),
        "arte1-c13": (
            "Ad Reinhardt, Abstract Painting (Black Painting), 1960-1966 - Olio su tela, Museum of Modern Art, New York",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/reinhardt_black_painting.jpg",
            "L'estremo azzeramento della pittura: una griglia a croce quasi impercettibile su fondo nero opaco, che esige un tempo prolungato di adattamento retinico."
        ),
        "arte1-c18": (
            "Robert Rauschenberg, Monogram, 1955-1959 - Combine painting con capra d'angora tassidermizzata, pneumatico, pittura e collage, Moderna Museet, Stoccolma",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/rauschenberg_monogram.jpg",
            "L'opera cardine del New Dada che colma il divario tra arte e vita, integrando scarti urbani e oggetti tridimensionali nella superficie del dipinto."
        ),
        "arte1-c21": (
            "Andy Warhol, Campbell's Soup Cans, 1962 - Sintetico polimero su trentadue tele, The Museum of Modern Art (MoMA), New York",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/warhol_campbell_soup.jpg",
            "L'icona fondante della Pop Art americana: la serialità industriale delle scatolette di zuppa assurge a emblema universale della società dei consumi."
        ),
        "arte1-c24": (
            "Andy Warhol, Green Coca-Cola Bottles, 1962 - Serigrafia e acrilico su tela, Whitney Museum of American Art, New York",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/warhol_coca_cola.jpg",
            "La ripetizione modulare della bottiglia di Coca-Cola esalta la natura democratica e spersonalizzata del consumo di massa."
        ),
        "arte1-c25": (
            "Tom Wesselmann, Great American Nude No. 21, 1961 - Tecnica mista e collage su tavola, Collezione privata",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/wesselmann_nude.jpg",
            "La sensualità stilizzata del nudo femminile fusa con ritagli pubblicitari di prodotti di largo consumo e colori acrilici piatti e squillanti."
        ),
        "arte1-c27": (
            "David Hockney, A Bigger Splash, 1967 - Acrilico su tela, 242.5 x 243.9 cm, Tate Britain, Londra",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/hockney_bigger_splash.jpg",
            "Il capolavoro del pop britannico in California: la quiete della villa modernista infranta dall'effimero e meticoloso spruzzo dell'acqua nella piscina."
        ),
        "arte1-c29": (
            "Tano Festa, La Creazione di Adamo (da Michelangelo), 1964 - Smalto su tela e legno sagomato, Collezione privata",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/festa_creazione.jpg",
            "La Scuola di Piazza del Popolo a Roma: la storia dell'arte italiana (Michelangelo) trattata come un reperto pubblicitario e un'icona di massa."
        ),
        "arte1-c30": (
            "Victor Vasarely, Vega-Nor, 1969 - Olio su tela, 200 x 200 cm, Albright-Knox Art Gallery, Buffalo",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/vasarely_vega_nor.jpg",
            "La distorsione ottica programmata della griglia geometrica crea una potente illusione tridimensionale di rigonfiamento spaziale (Op Art)."
        ),
        "arte1-c33": (
            "Donald Judd, Untitled (Stack), 1967 - Dieci elementi in ferro galvanizzato e plexiglas verde, The Museum of Modern Art, New York",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/judd_stack.jpg",
            "La scultura come Specific Object modulare: scatole geometriche identiche distanziate a intervalli regolari lungo la parete verticale."
        ),
        "arte1-c37": (
            "Sol LeWitt, Wall Drawing #831 (Geometric Forms), 1997 - Acrilico su parete, Museo Guggenheim, Bilbao",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/lewitt_wall_drawing.jpg",
            "L'idea come motore primario dell'opera: l'artista redige le istruzioni concettuali e matematiche che gli esecutori traducono sul muro."
        ),
        "arte1-c41": (
            "Michelangelo Pistoletto, Venere degli stracci, 1967 - Calco in gesso di Venere con stracci colorati, Museo d'Arte Contemporanea Donnaregina (MADRE), Napoli",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/pistoletto_venere_stracci.jpg",
            "Il manifesto scultoreo dell'Arte Povera: il contrasto poetico e dialettico tra la purezza marmorea del canone classico e il cumulo caotico dei rifiuti tessili moderni."
        ),
        "arte1-c46": (
            "Pino Pascali, Trappola, 1968 - Lana d'acciaio su telaio metallico, Tate Modern, Londra",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/pascali_mare.jpg",
            "La scultura ludica e biomorfa di Pino Pascali: una forma organica sospesa realizzata con materiale industriale povero come la paglietta di ferro."
        ),
        "arte1-c5": (
            "Jean Dubuffet, Corps de dame, 1950 - Olio su tela con sabbia e impasti materici, Collezione privata",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/dubuffet_art_brut.jpg",
            "La celebrazione dell'Art Brut e dell'informale materico: la figura femminile deformata e incisa direttamente nella pasta cromatica spessa e terrosa."
        ),
        "arte1-c6": (
            "Wols (Alfred Otto Wolfgang Schulze), Composizione, 1946-1947 - Olio su tela, Centre Pompidou, Parigi",
            "assets/corsi/dapl08/anno-1/storia-arte-1/images/wols_composizione.jpg",
            "Il nucleo vibrante del tachisme europeo: graffi, colature e una ferita cromatica centrale che esprimono la fragilità dell'esistenza del dopoguerra."
        )
    }

    modified_count = 0
    for ch in chapters:
        cid = ch.get("id")
        summary = ch.get("summary", "")

        # Se il capitolo è nella lista di arricchimento e non ha già un'immagine valida incorporata
        if cid in new_images and "![" not in summary:
            caption, img_path, descr = new_images[cid]
            figure_md = f"\n\n---\n\n### Apparato Iconografico Documentario\n\n![{caption}]({img_path})\n\n* **Analisi storico-stilistica dell'opera**: {descr}\n\n---\n"
            ch["summary"] = summary + figure_md
            modified_count += 1

    print(f"Arricchiti {modified_count} capitoli in Storia dell'Arte 1!")

    # Ricostruisci il file JS preservando il formato
    new_json_str = json.dumps(chapters, indent=2, ensure_ascii=False)
    final_output = prefix + new_json_str + suffix
    with open(path, "w", encoding="utf-8") as f:
        f.write(final_output)
    print("Salvataggio completato per data/arte1-data.js!")

if __name__ == "__main__":
    update_arte2()
    update_arte1()
