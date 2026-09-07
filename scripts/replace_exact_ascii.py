# -*- coding: utf-8 -*-
"""
Esegue le 5 sostituzioni dei blocchi ASCII rimanenti in build_stull_p2, p3, p4.
"""

# 1. build_stull_p2_complete.py (Gestalt)
with open('scripts/build_stull_p2_complete.py', 'r', encoding='utf-8') as f:
    c2 = f.read()

target_p2 = """```
+-------------------------------------------------------------------------+
|                  LE PRINCIPALI LEGGI DELLA GESTALT                      |
+-------------------------------------------------------------------------+
| 1. PROSSIMITÀ   | Gli elementi spazialmente vicini vengono percepiti    |
|                 | come parte del medesimo gruppo o unità logica.        |
+-----------------+-------------------------------------------------------+
| 2. SOMIGLIANZA  | Gli elementi che condividono forma, colore o stile    |
|                 | vengono percepiti come aventi la medesima funzione.   |
+-----------------+-------------------------------------------------------+
| 3. CONTINUITÀ   | L'occhio segue percorsi, linee e curve naturali       |
|                 | percependo gli elementi allineati come continui.      |
+-----------------+-------------------------------------------------------+
| 4. CHIUSURA     | Il cervello completa automaticamente le figure        |
|                 | incomplete, percependo forme chiuse anche con buchi.  |
+-----------------+-------------------------------------------------------+
| 5. FIGURA/SFONDO| La mente separa istintivamente l'oggetto in primo     |
|                 | piano (figura focale) dallo sfondo retrostante.       |
+-----------------+-------------------------------------------------------+
| 6. DESTINO      | Elementi che si muovono nella medesima direzione      |
|    COMUNE       | vengono percepiti come un unico gruppo coerente.      |
+-------------------------------------------------------------------------+
```"""

repl_p2 = """| Legge della Gestalt | Principio Percettivo |
| :--- | :--- |
| **1. Prossimità** | Gli elementi spazialmente vicini vengono percepiti come parte del medesimo gruppo o unità logica. |
| **2. Somiglianza** | Gli elementi che condividono forma, colore o stile vengono percepiti come aventi la medesima funzione. |
| **3. Continuità** | L'occhio segue percorsi, linee e curve naturali percependo gli elementi allineati come continui. |
| **4. Chiusura** | Il cervello completa automaticamente le figure incomplete, percependo forme chiuse anche con buchi. |
| **5. Figura / Sfondo** | La mente separa istintivamente l'oggetto in primo piano (figura focale) dallo sfondo retrostante. |
| **6. Destino Comune** | Elementi che si muovono nella medesima direzione vengono percepiti come un unico gruppo coerente. |"""

assert target_p2 in c2, "target_p2 non trovato in c2!"
c2 = c2.replace(target_p2, repl_p2)
with open('scripts/build_stull_p2_complete.py', 'w', encoding='utf-8') as f:
    f.write(c2)
print("P2 sostituito con successo!")


# 2. build_stull_p3_complete.py (Sahlins + Kotler)
with open('scripts/build_stull_p3_complete.py', 'r', encoding='utf-8') as f:
    c3 = f.read()

target_p3_1 = """```
+--------------------------------------------------------------------------+
|                  LE TRE FORME DI RECIPROCITÀ DI SAHLINS                  |
+--------------------------------------------------------------------------+
| 1. RECIPROCITÀ   | Il dono puro tra affetti stretti: si dona valore      |
|    GENERALIZZATA | senza fissare scadenze o pretese di ritorno esatto.   |
|                  | (In UX: tool gratuiti senza registrazione, open source)|
+------------------+-------------------------------------------------------+
| 2. RECIPROCITÀ   | Lo scambio commerciale trasparente: scambio simultaneo|
|    BILANCIATA    | di beni di valore equivalente (acquisto chiaro).       |
|                  | (In UX: pago 10€ e ricevo immediatamente il servizio) |
+------------------+-------------------------------------------------------+
| 3. RECIPROCITÀ   | Il tentativo predatorio di ottenere il massimo        |
|    NEGATIVA      | dando il minimo (estorsione, trappole, dark pattern). |
|                  | (In UX: costringere a lasciare il telefono per un pdf)|
+------------------+-------------------------------------------------------+
```"""

repl_p3_1 = """| Forma di Reciprocità (Sahlins) | Definizione Antropologica | Traduzione Operativa in UX |
| :--- | :--- | :--- |
| **1. Generalizzata** | Dono puro senza aspettativa di ritorno immediato | Tool gratuiti senza login, open source, guide di valore |
| **2. Bilanciata** | Scambio equo e trasparente di beni equivalenti | Acquisto trasparente (pago un servizio e ricevo valore) |
| **3. Negativa** | Tentativo predatorio di ottenere il massimo dando il minimo | Costringere a lasciare il telefono per un documento, dark pattern |"""

target_p3_2 = """```
+--------------------------------------------------------------------------+
|                  I TRE LIVELLI DEL PRODOTTO (PHILIP KOTLER)              |
+--------------------------------------------------------------------------+
| 1. BENEFICIO    | Il bisogno umano primario risolto dal prodotto.         |
|    ESSENZIALE   | (Es. Non comprate un trapano, comprate un buco nel muro)|
+-----------------+--------------------------------------------------------+
| 2. PRODOTTO     | Il manufatto tangibile con cui si interagisce:          |
|    EFFETTIVO    | codice, interfaccia grafica, packaging, marca e feature.|
+-----------------+--------------------------------------------------------+
| 3. PRODOTTO     | L'insieme dei servizi accessori e di supporto:          |
|    AMPLIATO     | assistenza clienti, garanzie, resi facili, community.   |
|                 | (È QUI CHE SI VINCE O SI PERDE LA FEDELTÀ DEL CLIENTE!) |
+--------------------------------------------------------------------------+
```"""

repl_p3_2 = """| Livello del Prodotto (Kotler) | Definizione Teorica | Esempio Applicato |
| :--- | :--- | :--- |
| **1. Beneficio Essenziale** | Il bisogno umano primario risolto | Non comprate un trapano, comprate un buco nel muro |
| **2. Prodotto Effettivo** | Il manufatto tangibile con cui si interagisce | Schermate, codice, pulsanti, interfaccia, feature |
| **3. Prodotto Ampliato** | I servizi accessori e di supporto | Assistenza, garanzie, resi facili (qui si vince la fedeltà!) |"""

assert target_p3_1 in c3, "target_p3_1 non trovato in c3!"
assert target_p3_2 in c3, "target_p3_2 non trovato in c3!"
c3 = c3.replace(target_p3_1, repl_p3_1).replace(target_p3_2, repl_p3_2)
with open('scripts/build_stull_p3_complete.py', 'w', encoding='utf-8') as f:
    f.write(c3)
print("P3 sostituito con successo!")


# 3. build_stull_p4_complete.py (3 pilastri + McResources)
with open('scripts/build_stull_p4_complete.py', 'r', encoding='utf-8') as f:
    c4 = f.read()

target_p4_1 = """```
+--------------------------------------------------------------------------+
|                  I TRE PILASTRI DELLA DEFINIZIONE DEL PROBLEMA           |
+--------------------------------------------------------------------------+
| 1. COSA         | Delimita il perimetro esatto del progetto:             |
|                 | stabilisce cosa si creerà e soprattutto COSA NON SI FARÀ|
+-----------------+--------------------------------------------------------+
| 2. PERCHÉ       | Esplicita il bisogno umano profondo e il valore        |
|                 | economico/strategico irrinunciabile per il business.   |
+-----------------+--------------------------------------------------------+
| 3. COME         | Dichiara il principio operativo differenziante con cui  |
|                 | la nostra soluzione supererà la seconda alternativa.    |
+--------------------------------------------------------------------------+
```"""

repl_p4_1 = """| Pilastro della Definizione | Funzione Progettuale | Domanda Guida |
| :--- | :--- | :--- |
| **1. COSA** | Delimita il perimetro esatto del progetto | Cosa creeremo e soprattutto cosa NON faremo? |
| **2. PERCHÉ** | Esplicita il bisogno profondo e il valore economico | Perché questo problema merita di essere risolto? |
| **3. COME** | Dichiara il principio operativo differenziante | Come la nostra soluzione supererà la seconda alternativa? |"""

target_p4_2 = """```
+-------------------------------------------------------------------------+
|                  IL CALCOLO ECONOMICO CHE SMONTA MCRESOURCES            |
+-------------------------------------------------------------------------+
| Voce di Bilancio                                | Importo Annuo ($)     |
+-------------------------------------------------+-----------------------+
| Paga oraria media di un addetto alla friggitoria| 10,93 $ / ora         |
| Retribuzione annua a tempo pieno (2.080 ore)    | ≈ 22.730,00 $         |
| Au-pair (10,72 $/h) a copertura oraria          | - 22.290,00 $         |
| Addetto alla piscina (13,51 $/h, 1 ora/sett.)   | - 702,52 $            |
| Personal trainer (18,85 $/h, sedute periodiche) | - 980,20 $            |
+-------------------------------------------------+-----------------------+
| RISULTATO: DEBITO ANNUALE                       | - 1.242,72 $          |
| (Prima di pagare affitto, cibo, riscaldamento, tasse e... mance!)       |
+-------------------------------------------------------------------------+
```"""

repl_p4_2 = """| Voce di Bilancio | Importo Annuo ($) |
| :--- | :--- |
| Paga oraria media addetto friggitoria (BLS) | 10,93 $ / ora |
| Retribuzione annua a tempo pieno (2.080 ore) | ≈ 22.730,00 $ |
| Au-pair (10,72 $/h) a copertura oraria | − 22.290,00 $ |
| Addetto alla piscina (13,51 $/h, 1 ora/sett.) | − 702,52 $ |
| Personal trainer (18,85 $/h, sedute periodiche) | − 980,20 $ |
| **RISULTATO: DEBITO ANNUALE** | **− 1.242,72 $** |
*(Prima di pagare affitto, cibo, riscaldamento, tasse e... mance!)*"""

assert target_p4_1 in c4, "target_p4_1 non trovato in c4!"
assert target_p4_2 in c4, "target_p4_2 non trovato in c4!"
c4 = c4.replace(target_p4_1, repl_p4_1).replace(target_p4_2, repl_p4_2)
with open('scripts/build_stull_p4_complete.py', 'w', encoding='utf-8') as f:
    f.write(c4)
print("P4 sostituito con successo!")
