#!/usr/bin/env python3
"""
Script per scaricare e validare immagini autentiche per Storia dell'Arte 1 e 2.
Rispetta la regola: ZERO EMOJI.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_ARTE1 = os.path.join(BASE_DIR, "assets", "corsi", "dapl08", "anno-1", "storia-arte-1", "images")
DIR_ARTE2 = os.path.join(BASE_DIR, "assets", "corsi", "dapl08", "anno-2", "storia-arte-2", "images")

os.makedirs(DIR_ARTE1, exist_ok=True)
os.makedirs(DIR_ARTE2, exist_ok=True)

USER_AGENT = "StudioArteAcademic/1.0 (contact: student@accademia.it)"

def fetch_wiki_summary_image(page_title, lang="en"):
    """Recupera URL immagine principale da Wikipedia REST API."""
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(page_title)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            orig = data.get("originalimage", {}).get("source")
            thumb = data.get("thumbnail", {}).get("source")
            return orig or thumb
    except Exception as e:
        return None

def fetch_commons_file_url(search_query):
    """Cerca su Wikimedia Commons per file pertinenti."""
    url = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&generator=search&gsrsearch={urllib.parse.quote(search_query)}&gsrnamespace=6&gsrlimit=5"
        "&prop=imageinfo&iiprop=url|size"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for pid, p in pages.items():
                infos = p.get("imageinfo", [])
                if infos and "url" in infos[0]:
                    img_url = infos[0]["url"]
                    # Filtra svg o pdf o tif enormi
                    if img_url.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                        return img_url
    except Exception as e:
        return None
    return None

def download_image(url, target_path):
    """Scarica e valida una singola immagine."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read()
            if len(content) < 5000:
                print(f"[ERRORE] File troppo piccolo ({len(content)} byte): {url}")
                return False
            with open(target_path, "wb") as f:
                f.write(content)
        # Valida con PIL
        with Image.open(target_path) as img:
            w, h = img.size
            if w < 100 or h < 100:
                print(f"[ERRORE] Risoluzione insufficiente ({w}x{h}): {target_path}")
                os.remove(target_path)
                return False
            print(f"[OK] Salvato {os.path.basename(target_path)} ({w}x{h}, {len(content)//1024} KB)")
        return True
    except Exception as e:
        print(f"[ERRORE] Download fallito da {url}: {e}")
        if os.path.exists(target_path):
            os.remove(target_path)
        return False

# Mappatura delle opere per Storia dell'Arte 1
ARTE1_TARGETS = [
    # Fautrier
    ("fautrier_ostaggi.jpg", [("wiki", "en", "Hostages_(Fautrier)"), ("commons", "Jean Fautrier Hostage"), ("commons", "Jean Fautrier Otages")]),
    ("fautrier_tete_otage.jpg", [("commons", "Fautrier Tete d'otage"), ("wiki", "fr", "Jean_Fautrier")]),
    # Dubuffet
    ("dubuffet_art_brut.jpg", [("commons", "Jean Dubuffet Corps de dame"), ("commons", "Jean Dubuffet"), ("wiki", "en", "Jean_Dubuffet")]),
    ("dubuffet_hourloupe.jpg", [("commons", "Dubuffet Hourloupe"), ("commons", "Jardin d'email Dubuffet")]),
    # Wols
    ("wols_composizione.jpg", [("wiki", "en", "Wols"), ("commons", "Wols painter"), ("commons", "Wols")]),
    # Burri
    ("burri_sacco_rosso.jpg", [("commons", "Alberto Burri Sacco"), ("wiki", "it", "Alberto_Burri"), ("commons", "Alberto Burri")]),
    ("burri_combustione.jpg", [("commons", "Alberto Burri Combustione"), ("commons", "Burri plastica")]),
    ("burri_cretto_gibellina.jpg", [("wiki", "it", "Grande_Cretto"), ("commons", "Grande Cretto Gibellina")]),
    # Pollock
    ("pollock_action_painting.jpg", [("wiki", "en", "Autumn_Rhythm_(Number_30)")]),
    ("pollock_namuth_fienile.jpg", [("commons", "Jackson Pollock painting"), ("wiki", "en", "Jackson_Pollock")]),
    ("pollock_number_1.jpg", [("commons", "Jackson Pollock Number 1"), ("wiki", "en", "Number_1A,_1948")]),
    # De Kooning
    ("de_kooning_woman.jpg", [("wiki", "en", "Woman_I")]),
    ("de_kooning_excavation.jpg", [("wiki", "en", "Excavation_(painting)"), ("commons", "Willem de Kooning Excavation")]),
    # Franz Kline
    ("kline_chief.jpg", [("wiki", "en", "Chief_(painting)"), ("commons", "Franz Kline Chief"), ("wiki", "en", "Franz_Kline")]),
    # Mark Rothko
    ("rothko_color_field.jpg", [("wiki", "en", "No._14_(White_and_Greens_in_Blue)"), ("wiki", "en", "Four_Darks_in_Red")]),
    ("rothko_chapel.jpg", [("wiki", "en", "Rothko_Chapel"), ("commons", "Rothko Chapel interior")]),
    # Barnett Newman
    ("newman_vir_heroicus.jpg", [("wiki", "en", "Vir_Heroicus_Sublimis")]),
    ("newman_onement.jpg", [("wiki", "en", "Onement_I"), ("commons", "Barnett Newman Onement")]),
    # Still & Reinhardt
    ("still_ph_1074.jpg", [("wiki", "en", "Clyfford_Still"), ("commons", "Clyfford Still painting")]),
    ("reinhardt_black_painting.jpg", [("wiki", "en", "Ad_Reinhardt"), ("commons", "Ad Reinhardt black painting")]),
    # Lucio Fontana
    ("fontana_concetto_spaziale.jpg", [("commons", "Lucio Fontana Concetto spaziale Attese"), ("commons", "Lucio Fontana Tagli"), ("wiki", "it", "Concetto_spaziale_Attese")]),
    ("fontana_ambiente_spaziale.jpg", [("commons", "Lucio Fontana Ambiente spaziale"), ("commons", "Fontana Ambiente spaziale luce nera")]),
    ("fontana_nature.jpg", [("commons", "Lucio Fontana Concetto spaziale Natura"), ("commons", "Fontana Natura bronzo")]),
    ("fontana_buchi.jpg", [("commons", "Lucio Fontana Buchi"), ("wiki", "it", "Lucio_Fontana")]),
    # Enrico Baj
    ("baj_generali.jpg", [("commons", "Enrico Baj I Generali"), ("wiki", "it", "Enrico_Baj"), ("commons", "Enrico Baj")]),
    ("baj_pinelli.jpg", [("wiki", "it", "I_funerali_dell%27anarchico_Pinelli"), ("commons", "Funerali dell'anarchico Pinelli")]),
    # Francis Bacon
    ("bacon_innocenzo_x.jpg", [("wiki", "en", "Study_after_Vel%C3%A1zquez%27s_Portrait_of_Pope_Innocent_X")]),
    ("bacon_crocifissione.jpg", [("wiki", "en", "Three_Studies_for_Figures_at_the_Base_of_a_Crucifixion")]),
    # Alberto Giacometti
    ("giacometti_uomo_cammina.jpg", [("wiki", "fr", "L%27Homme_qui_marche_I"), ("commons", "Giacometti Homme qui marche"), ("commons", "L'Homme qui marche Giacometti")]),
    ("giacometti_palazzo_4_mattino.jpg", [("wiki", "en", "The_Palace_at_4_a.m."), ("commons", "Giacometti Palace at 4 am")]),
    # Rauschenberg
    ("rauschenberg_bed.jpg", [("wiki", "en", "Bed_(artwork)"), ("commons", "Robert Rauschenberg Bed")]),
    ("rauschenberg_monogram.jpg", [("commons", "Robert Rauschenberg Monogram"), ("wiki", "en", "Robert_Rauschenberg")]),
    ("rauschenberg_retroactive.jpg", [("commons", "Rauschenberg Retroactive"), ("commons", "Robert Rauschenberg Retroactive I")]),
    # Jasper Johns
    ("johns_flag.jpg", [("wiki", "en", "Flag_(painting)")]),
    ("johns_target.jpg", [("wiki", "en", "Target_with_Four_Faces"), ("commons", "Jasper Johns Target")]),
    # Roy Lichtenstein
    ("lichtenstein_whaam.jpg", [("wiki", "en", "Whaam!")]),
    ("lichtenstein_drowning_girl.jpg", [("wiki", "en", "Drowning_Girl")]),
    # Claes Oldenburg
    ("oldenburg_floor_cake.jpg", [("wiki", "en", "Floor_Cake"), ("commons", "Claes Oldenburg Floor Cake")]),
    ("oldenburg_store.jpg", [("commons", "Claes Oldenburg The Store"), ("wiki", "en", "Claes_Oldenburg")]),
    # James Rosenquist
    ("rosenquist_f111.jpg", [("wiki", "en", "F-111_(painting)"), ("commons", "James Rosenquist F-111")]),
    # Wesselmann & Segal
    ("wesselmann_nude.jpg", [("commons", "Tom Wesselmann Great American Nude"), ("wiki", "en", "Tom_Wesselmann")]),
    ("segal_bus_driver.jpg", [("commons", "George Segal The Bus Driver"), ("wiki", "en", "George_Segal_(artist)")]),
    # Richard Hamilton
    ("hamilton_pop_art.jpg", [("wiki", "en", "Just_what_is_it_that_makes_today%27s_homes_so_different%2C_so_appealing%3F")]),
    # David Hockney
    ("hockney_bigger_splash.jpg", [("wiki", "en", "A_Bigger_Splash")]),
    ("hockney_clark_percy.jpg", [("wiki", "en", "Mr_and_Mrs_Clark_and_Percy")]),
    # Mario Schifano
    ("schifano_propaganda.jpg", [("commons", "Mario Schifano Propaganda"), ("wiki", "it", "Mario_Schifano"), ("commons", "Mario Schifano")]),
    ("schifano_incidente.jpg", [("commons", "Mario Schifano Grande particolare"), ("commons", "Schifano paesaggio")]),
    # Festa & Angeli
    ("festa_creazione.jpg", [("commons", "Tano Festa"), ("wiki", "it", "Tano_Festa")]),
    ("angeli_half_dollar.jpg", [("commons", "Franco Angeli"), ("wiki", "it", "Franco_Angeli_(artista)")]),
    # Victor Vasarely
    ("vasarely_vega_nor.jpg", [("commons", "Victor Vasarely Vega"), ("wiki", "en", "Victor_Vasarely"), ("commons", "Victor Vasarely")]),
    ("vasarely_zebra.jpg", [("commons", "Vasarely Zebras"), ("commons", "Victor Vasarely Zebra")]),
    # Gianni Colombo
    ("colombo_spazio_elastico.jpg", [("commons", "Gianni Colombo Spazio elastico"), ("wiki", "it", "Gianni_Colombo")]),
    # Donald Judd
    ("judd_stack.jpg", [("commons", "Donald Judd Untitled stack"), ("wiki", "en", "Donald_Judd"), ("commons", "Donald Judd sculpture")]),
    # Dan Flavin
    ("flavin_monument_tatlin.jpg", [("commons", "Dan Flavin Monument for Tatlin"), ("wiki", "en", "Dan_Flavin"), ("commons", "Dan Flavin light")]),
    # Carl Andre
    ("andre_equivalent_viii.jpg", [("wiki", "en", "Equivalent_VIII"), ("commons", "Carl Andre Equivalent")]),
    # Sol LeWitt
    ("lewitt_serial_project.jpg", [("commons", "Sol LeWitt Serial Project"), ("wiki", "en", "Sol_LeWitt")]),
    ("lewitt_wall_drawing.jpg", [("commons", "Sol LeWitt Wall Drawing"), ("commons", "Sol LeWitt")]),
    # Kaprow & Fluxus
    ("kaprow_yard.jpg", [("commons", "Allan Kaprow Yard"), ("wiki", "en", "Allan_Kaprow")]),
    ("maciunas_fluxus.jpg", [("commons", "George Maciunas Fluxus"), ("wiki", "en", "Fluxus")]),
    # Joseph Beuys
    ("beuys_coyote_america.jpg", [("commons", "Joseph Beuys Coyote"), ("wiki", "en", "I_Like_America_and_America_Likes_Me")]),
    ("beuys_abito_feltro.jpg", [("commons", "Joseph Beuys Filzanzug"), ("commons", "Beuys Felt Suit")]),
    ("beuys_lepre_morta.jpg", [("commons", "Joseph Beuys Dead Hare"), ("wiki", "en", "How_to_Explain_Pictures_to_a_Dead_Hare")]),
    # Nam June Paik
    ("paik_tv_buddha.jpg", [("commons", "Nam June Paik TV Buddha"), ("wiki", "en", "TV_Buddha"), ("wiki", "en", "Nam_June_Paik")]),
    ("paik_electronic_superhighway.jpg", [("wiki", "en", "Electronic_Superhighway"), ("commons", "Nam June Paik Electronic Superhighway")]),
    # Michelangelo Pistoletto
    ("pistoletto_venere_stracci.jpg", [("wiki", "it", "Venere_degli_stracci"), ("commons", "Venere degli stracci Pistoletto")]),
    ("pistoletto_quadro_specchiante.jpg", [("commons", "Michelangelo Pistoletto Quadro specchiante"), ("wiki", "it", "Michelangelo_Pistoletto")]),
    # Jannis Kounellis
    ("kounellis_cavalli_attico.jpg", [("commons", "Jannis Kounellis Cavalli L'Attico"), ("commons", "Jannis Kounellis 12 cavalli"), ("wiki", "it", "Jannis_Kounellis")]),
    ("kounellis_carbone.jpg", [("commons", "Jannis Kounellis carbone"), ("commons", "Jannis Kounellis")]),
    # Mario Merz
    ("merz_igloo_giap.jpg", [("commons", "Mario Merz Igloo"), ("wiki", "it", "Mario_Merz")]),
    # Alighiero Boetti
    ("boetti_mappa.jpg", [("commons", "Alighiero Boetti Mappa"), ("wiki", "it", "Alighiero_Boetti"), ("commons", "Alighiero Boetti")]),
    ("boetti_gemelli.jpg", [("commons", "Alighiero Boetti Gemelli"), ("commons", "Boetti Gemelli")]),
    # Pascali & Penone
    ("pascali_mare.jpg", [("commons", "Pino Pascali 32 mq di mare"), ("wiki", "it", "Pino_Pascali")]),
    ("penone_albero.jpg", [("commons", "Giuseppe Penone Albero"), ("wiki", "it", "Giuseppe_Penone")]),
    # Joseph Kosuth
    ("kosuth_one_and_three_chairs.jpg", [("wiki", "en", "One_and_Three_Chairs")]),
    # Daniel Buren & On Kawara
    ("buren_in_situ.jpg", [("commons", "Daniel Buren"), ("wiki", "en", "Daniel_Buren")]),
    ("on_kawara_today.jpg", [("commons", "On Kawara Today Series"), ("wiki", "en", "On_Kawara")]),
    # Robert Smithson
    ("smithson_spiral_jetty.jpg", [("wiki", "en", "Spiral_Jetty")]),
    # Walter De Maria & Christo
    ("de_maria_lightning_field.jpg", [("wiki", "en", "The_Lightning_Field"), ("commons", "The Lightning Field")]),
    ("christo_running_fence.jpg", [("wiki", "en", "Running_Fence"), ("commons", "Christo Running Fence")]),
    # Marina Abramović & Gina Pane
    ("abramovic_rhythm_0.jpg", [("wiki", "en", "Rhythm_0"), ("commons", "Marina Abramovic Rhythm 0"), ("wiki", "en", "Marina_Abramovi%C4%87")]),
    ("pane_azione_sentimentale.jpg", [("commons", "Gina Pane Azione sentimentale"), ("wiki", "it", "Gina_Pane")]),
    # René Magritte
    ("magritte_trahison_images.jpg", [("wiki", "en", "The_Treachery_of_Images")]),
    ("magritte_empire_lumieres.jpg", [("wiki", "en", "The_Empire_of_Light")]),
    ("magritte_condition_humaine.jpg", [("wiki", "en", "The_Human_Condition_(Magritte)")]),
    ("magritte_amants.jpg", [("wiki", "en", "The_Lovers_(Magritte_paintings)"), ("commons", "Magritte The Lovers")]),
    # Man Ray
    ("man_ray_violon_ingres.jpg", [("wiki", "en", "Le_Violon_d%27Ingres"), ("commons", "Man Ray Le Violon d'Ingres")]),
    ("man_ray_rayografia.jpg", [("commons", "Man Ray Rayograph"), ("wiki", "en", "Rayography")]),
    ("man_ray_cadeau.jpg", [("wiki", "en", "Cadeau_(sculpture)"), ("commons", "Man Ray Cadeau")]),
    ("man_ray_enigma_ducasse.jpg", [("commons", "Man Ray The Enigma of Isidore Ducasse"), ("wiki", "en", "Man_Ray")]),
    # Andy Warhol
    ("warhol_campbell_soup.jpg", [("wiki", "en", "Campbell%27s_Soup_Cans")]),
    ("warhol_marilyn_diptych.jpg", [("wiki", "en", "Marilyn_Diptych")]),
    ("warhol_gold_marilyn.jpg", [("wiki", "en", "Gold_Marilyn_Monroe"), ("commons", "Andy Warhol Gold Marilyn")]),
    ("warhol_green_car_crash.jpg", [("wiki", "en", "Green_Car_Crash"), ("commons", "Andy Warhol Green Car Crash")]),
    ("warhol_brillo_box.jpg", [("wiki", "en", "Brillo_Boxes"), ("commons", "Andy Warhol Brillo Box")])
]

# Mappatura delle opere per Storia dell'Arte 2
ARTE2_TARGETS = [
    # Transavanguardia
    ("chia_sinfonia_incompiuta.jpg", [("commons", "Sandro Chia"), ("wiki", "it", "Sandro_Chia")]),
    ("clemente_alba_danzante.jpg", [("commons", "Francesco Clemente"), ("wiki", "it", "Francesco_Clemente")]),
    ("cucchi_cani_lingua_spasso.jpg", [("commons", "Enzo Cucchi"), ("wiki", "it", "Enzo_Cucchi")]),
    ("paladino_lampeggiante.jpg", [("commons", "Mimmo Paladino"), ("wiki", "it", "Mimmo_Paladino")]),
    ("paladino_montagna_sale.jpg", [("commons", "Montagna di sale Paladino"), ("commons", "Mimmo Paladino Montagna di sale")]),
    ("demaria_regno_dei_fiori.jpg", [("commons", "Nicola De Maria"), ("wiki", "it", "Nicola_De_Maria")]),
    # Neoespressionismo tedesco
    ("kiefer_nigredo.jpg", [("commons", "Anselm Kiefer"), ("wiki", "en", "Anselm_Kiefer")]),
    ("kiefer_sulamith.jpg", [("commons", "Anselm Kiefer Sulamith"), ("wiki", "en", "Sulamith_(painting)")]),
    ("kiefer_high_priestess.jpg", [("commons", "Anselm Kiefer High Priestess"), ("commons", "Anselm Kiefer Zweistromland")]),
    ("baselitz_ragazze_olmo.jpg", [("commons", "Georg Baselitz"), ("wiki", "en", "Georg_Baselitz")]),
    ("baselitz_modell_skulptur.jpg", [("commons", "Georg Baselitz Modell fur eine Skulptur"), ("commons", "Georg Baselitz Venice 1980")]),
    ("polke_rasterbild.jpg", [("commons", "Sigmar Polke"), ("wiki", "en", "Sigmar_Polke")]),
    ("richter_abstract_composition.jpg", [("wiki", "en", "Gerhard_Richter"), ("commons", "Gerhard Richter")]),
    ("richter_18_oktober.jpg", [("wiki", "en", "October_18,_1977"), ("commons", "Gerhard Richter October 18 1977")]),
    ("immendorff_cafe_deutschland.jpg", [("commons", "Jorg Immendorff Cafe Deutschland"), ("wiki", "en", "J%C3%B6rg_Immendorff")]),
    ("middendorf_peep_show.jpg", [("commons", "Helmut Middendorf"), ("wiki", "en", "Helmut_Middendorf")]),
    # New Painting & Graffiti
    ("schnabel_maid_of_germany.jpg", [("commons", "Julian Schnabel"), ("wiki", "en", "Julian_Schnabel")]),
    ("salle_circumnavigating.jpg", [("commons", "David Salle"), ("wiki", "en", "David_Salle")]),
    ("basquiat_arroz_con_pollo.jpg", [("wiki", "en", "Arroz_con_Pollo_(painting)"), ("wiki", "en", "Jean-Michel_Basquiat")]),
    ("basquiat_irony_policeman.jpg", [("wiki", "en", "Irony_of_Negro_Policeman"), ("commons", "Basquiat Irony of Negro Policeman")]),
    ("basquiat_skull.jpg", [("wiki", "en", "Untitled_(1981_Basquiat_skull_painting)")]),
    ("basquiat_boy_dog.jpg", [("wiki", "en", "Boy_and_Dog_in_a_Johnnypump")]),
    ("haring_subway.jpg", [("commons", "Keith Haring Subway Drawing"), ("wiki", "en", "Keith_Haring")]),
    ("haring_radiant_baby.jpg", [("commons", "Keith Haring Radiant Baby"), ("commons", "Keith Haring Barking Dog")]),
    ("haring_tuttomondo.jpg", [("wiki", "it", "Tuttomondo"), ("commons", "Keith Haring Tuttomondo Pisa")]),
    # Pictures Generation & Simulacro
    ("sherman_film_still_21.jpg", [("wiki", "en", "Untitled_Film_Stills"), ("commons", "Cindy Sherman Untitled Film Still")]),
    ("sherman_untitled_153.jpg", [("wiki", "en", "Untitled_%23153"), ("wiki", "en", "Cindy_Sherman")]),
    ("kruger_your_body.jpg", [("wiki", "en", "Untitled_(Your_body_is_a_battleground)")]),
    ("kruger_i_shop.jpg", [("wiki", "en", "I_shop_therefore_I_am"), ("commons", "Barbara Kruger I shop therefore I am")]),
    ("prince_cowboy.jpg", [("wiki", "en", "Untitled_(Cowboy)")]),
    ("koons_equilibrium.jpg", [("wiki", "en", "Equilibrium_(sculpture_series)"), ("wiki", "en", "Jeff_Koons")]),
    ("koons_rabbit.jpg", [("wiki", "en", "Rabbit_(sculpture)")]),
    ("koons_michael_jackson.jpg", [("wiki", "en", "Michael_Jackson_and_Bubbles")]),
    ("holzer_truisms.jpg", [("wiki", "en", "Truisms_(Jenny_Holzer)"), ("commons", "Jenny Holzer Truisms")]),
    # YBA
    ("hirst_shark.jpg", [("wiki", "en", "The_Physical_Impossibility_of_Death_in_the_Mind_of_Someone_Living")]),
    ("hirst_skull_diamond.jpg", [("wiki", "en", "For_the_Love_of_God")]),
    ("quinn_self.jpg", [("wiki", "en", "Self_(sculpture)"), ("commons", "Marc Quinn Self")]),
    ("emin_my_bed.jpg", [("wiki", "en", "My_Bed")]),
    ("whiteread_house.jpg", [("wiki", "en", "House_(sculpture)")]),
    ("chapman_hell.jpg", [("wiki", "en", "Hell_(Chapman_brothers)"), ("commons", "Jake and Dinos Chapman")]),
    # Post-Human & Identity
    ("barney_cremaster.jpg", [("wiki", "en", "The_Cremaster_Cycle"), ("commons", "Matthew Barney Cremaster")]),
    ("gober_sink.jpg", [("commons", "Robert Gober Sink"), ("wiki", "en", "Robert_Gober")]),
    ("gonzalez_torres_ross.jpg", [("wiki", "en", "%22Untitled%22_(Portrait_of_Ross_in_L.A.)")]),
    ("gonzalez_torres_perfect_lovers.jpg", [("wiki", "en", "%22Untitled%22_(Perfect_Lovers)")]),
    ("beecroft_vb35.jpg", [("commons", "Vanessa Beecroft"), ("wiki", "en", "Vanessa_Beecroft")]),
    ("neshat_women_of_allah.jpg", [("commons", "Shirin Neshat Women of Allah"), ("wiki", "en", "Shirin_Neshat")]),
    ("walker_silhouette.jpg", [("commons", "Kara Walker"), ("wiki", "en", "Kara_Walker")]),
    ("goldin_nan_brian.jpg", [("wiki", "en", "The_Ballad_of_Sexual_Dependency"), ("commons", "Nan Goldin")]),
    ("tiravanija_pad_thai.jpg", [("commons", "Rirkrit Tiravanija Pad Thai"), ("wiki", "en", "Rirkrit_Tiravanija")]),
    ("pipilotti_rist_sip_my_ocean.jpg", [("commons", "Pipilotti Rist Sip My Ocean"), ("wiki", "en", "Pipilotti_Rist")]),
    # Cattelan
    ("cattelan_la_nona_ora.jpg", [("wiki", "en", "La_Nona_Ora"), ("commons", "Cattelan La Nona Ora"), ("wiki", "it", "Maurizio_Cattelan")]),
    ("cattelan_him.jpg", [("wiki", "en", "Him_(sculpture)"), ("commons", "Maurizio Cattelan Him")]),
    ("cattelan_bambini_milano.jpg", [("commons", "Cattelan bambini impiccati"), ("wiki", "it", "Maurizio_Cattelan")]),
    ("cattelan_love_piazza_affari.jpg", [("wiki", "it", "L.O.V.E._(scultura)"), ("commons", "L.O.V.E. Maurizio Cattelan")]),
    ("cattelan_comedian.jpg", [("wiki", "en", "Comedian_(artwork)")]),
    # Global & New Media
    ("ai_weiwei_sunflower_seeds.jpg", [("wiki", "en", "Sunflower_Seeds_(artwork)"), ("commons", "Ai Weiwei Sunflower Seeds")]),
    ("ai_weiwei_dropping_urn.jpg", [("wiki", "en", "Dropping_a_Han_Dynasty_Urn"), ("commons", "Ai Weiwei Han Dynasty Urn")]),
    ("eliasson_weather_project.jpg", [("wiki", "en", "The_Weather_Project"), ("commons", "Olafur Eliasson The Weather Project")]),
    ("eliasson_ice_watch.jpg", [("wiki", "en", "Ice_Watch_(artwork)"), ("commons", "Olafur Eliasson Ice Watch")]),
    ("salcedo_shibboleth.jpg", [("wiki", "en", "Shibboleth_(artwork)"), ("commons", "Doris Salcedo Shibboleth")]),
    ("kentridge_drawing.jpg", [("commons", "William Kentridge"), ("wiki", "en", "William_Kentridge")]),
    ("orozco_black_kites.jpg", [("commons", "Gabriel Orozco Black Kites"), ("wiki", "en", "Gabriel_Orozco")]),
    ("murakami_superflat.jpg", [("commons", "Takashi Murakami"), ("wiki", "en", "Superflat")]),
    ("banksy_balloon.jpg", [("wiki", "en", "Girl_with_Balloon"), ("wiki", "en", "Love_is_in_the_Bin")])
]

def process_targets(targets, out_dir):
    total = len(targets)
    success = 0
    for idx, (filename, sources) in enumerate(targets, 1):
        target_path = os.path.join(out_dir, filename)
        print(f"\n[{idx}/{total}] Ricerca: {filename}")
        img_url = None
        for src_type, *args in sources:
            if src_type == "wiki":
                lang, title = args
                print(f"  -> Wikipedia ({lang}): {title}")
                img_url = fetch_wiki_summary_image(title, lang)
            elif src_type == "commons":
                query = args[0]
                print(f"  -> Wikimedia Commons: {query}")
                img_url = fetch_commons_file_url(query)
            
            if img_url:
                print(f"  -> Trovato URL: {img_url[:90]}...")
                if download_image(img_url, target_path):
                    success += 1
                    break
            time.sleep(0.4)
        
        if not os.path.exists(target_path):
            print(f"  [ATTENZIONE] Nessuna immagine trovata per {filename}")

    print(f"\nCompletato: {success}/{total} immagini scaricate con successo.")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("1", "all", "arte1"):
        print("=== AVVIO DOWNLOAD STORIA DELL'ARTE 1 ===")
        process_targets(ARTE1_TARGETS, DIR_ARTE1)
    if mode in ("2", "all", "arte2"):
        print("\n=== AVVIO DOWNLOAD STORIA DELL'ARTE 2 ===")
        process_targets(ARTE2_TARGETS, DIR_ARTE2)
