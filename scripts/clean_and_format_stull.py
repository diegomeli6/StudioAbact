# -*- coding: utf-8 -*-
import re

# ==================== PARTE 1 ====================
with open('scripts/build_stull_p1_complete.py', 'r', encoding='utf-8') as f:
    c1 = f.read()

# Ch 11 pyramid
c1 = re.sub(
    r'```\s*/\\\s*[\s\S]*?\+----------------\+\s*```',
    '''> **La Gerarchia dei Bisogni della UX (dalla base al vertice)**:
> 1. **UTILE (Fondamenta assolute)**: risolve un bisogno umano primario autentico
> 2. **AFFIDABILE (Infrastruttura)**: il sistema è stabile, veloce e protegge i dati
> 3. **USABILE (Ergonomia cognitiva)**: l'interfaccia è intuitiva, riduce gli errori e azzera il carico mentale
> 4. **PIACEVOLE / DELIGHT (Vertice emotivo)**: bellezza estetica, micro-interazioni gratificanti e sorpresa positiva''',
    c1
)

# Ch 9 formula
c1 = re.sub(
    r'\$\$8\.760\s*\\\\+times\s*0,01\s*=\s*87,6\s*\\\\+text\{\s*ore di blackout all\'anno\}\$\$',
    '**8.760 ore × 0,01 = 87,6 ore di blackout all\'anno**',
    c1
)

# Ch 10 formula
c1 = re.sub(
    r'\$\$\\\\+text\{Velocità Percepita\}\s*=\s*\\\\+text\{Tempo Reale\}\s*-\s*\(\\\\+text\{Coinvolgimento Cognitivo\}\s*\+\s*\\\\+text\{Feedback Visivo Positivo\}\)\$\$',
    '**Velocità Percepita = Tempo Reale − (Coinvolgimento Cognitivo + Feedback Visivo Positivo)**',
    c1
)

with open('scripts/build_stull_p1_complete.py', 'w', encoding='utf-8') as f:
    f.write(c1)


# ==================== PARTE 2 ====================
with open('scripts/build_stull_p2_complete.py', 'r', encoding='utf-8') as f:
    c2 = f.read()

# Ch 12 Gestalt
c2 = re.sub(
    r'```\s*\+--+[\s\S]*?LE PRINCIPALI LEGGI DELLA GESTALT[\s\S]*?\+--+\s*```',
    '''| Legge della Gestalt | Principio Percettivo |
| :--- | :--- |
| **1. Prossimità** | Gli elementi spazialmente vicini vengono percepiti come parte del medesimo gruppo o unità logica. |
| **2. Somiglianza** | Gli elementi che condividono forma, colore o stile vengono percepiti come aventi la medesima funzione. |
| **3. Continuità** | L'occhio segue percorsi e linee naturali percependo gli elementi allineati come continui. |
| **4. Chiusura** | Il cervello completa automaticamente le figure incomplete percependo forme chiuse. |
| **5. Figura / Sfondo** | La mente separa istintivamente l'oggetto in primo piano (figura focale) dallo sfondo retrostante. |
| **6. Destino Comune** | Elementi che si muovono nella medesima direzione vengono percepiti come un unico gruppo coerente. |''',
    c2
)

# Ch 14 formula
c2 = re.sub(
    r'\$\$\\\\+text\{Larghezza di Banda dell\'Attenzione\}\s*\\\\+approx\s*110\s*\\\\+text\{\s*bit al secondo \(bit/s\)\}\$\$',
    '**Larghezza di Banda dell\'Attenzione ≈ 110 bit al secondo (bit/s)**',
    c2
)

with open('scripts/build_stull_p2_complete.py', 'w', encoding='utf-8') as f:
    f.write(c2)


# ==================== PARTE 3 ====================
with open('scripts/build_stull_p3_complete.py', 'r', encoding='utf-8') as f:
    c3 = f.read()

# Ch 24 Sahlins
c3 = re.sub(
    r'```\s*\+--+[\s\S]*?LE TRE FORME DI RECIPROCITÀ DI SAHLINS[\s\S]*?\+--+\s*```',
    '''| Forma di Reciprocità (Sahlins) | Definizione Antropologica | Traduzione Operativa in UX |
| :--- | :--- | :--- |
| **1. Generalizzata** | Dono puro senza aspettativa di ritorno immediato | Tool gratuiti senza login, open source, guide di valore |
| **2. Bilanciata** | Scambio equo e trasparente di beni equivalenti | Acquisto trasparente (pago un servizio e ricevo valore) |
| **3. Negativa** | Tentativo predatorio di ottenere il massimo dando il minimo | Costringere a lasciare il telefono per un documento, dark pattern |''',
    c3
)

# Ch 25 Kotler
c3 = re.sub(
    r'```\s*\+--+[\s\S]*?I TRE LIVELLI DEL PRODOTTO \(PHILIP KOTLER\)[\s\S]*?\+--+\s*```',
    '''| Livello del Prodotto (Kotler) | Definizione Teorica | Esempio Applicato |
| :--- | :--- | :--- |
| **1. Beneficio Essenziale** | Il bisogno umano primario risolto | Non comprate un trapano, comprate un buco nel muro |
| **2. Prodotto Effettivo** | Il manufatto tangibile con cui si interagisce | Schermate, codice, pulsanti, interfaccia, feature |
| **3. Prodotto Ampliato** | I servizi accessori e di supporto | Assistenza, garanzie, resi facili (qui si vince la fedeltà!) |''',
    c3
)

# Ch 23 formula
c3 = re.sub(
    r'\$\$\\\\+text\{Rilevanza\}\s*=\s*\\\\+frac\{\\\\+text\{Bisogno Specifico dell\'Utente\}\s*\\\\+times\s*\\\\+text\{Tempismo Opportuno \(Timing\)\}\}\{\\\\+text\{Rumore Visivo e Informativo\}\}\$\$',
    '**Rilevanza = (Bisogno Specifico dell\'Utente × Tempismo Opportuno) / Rumore Visivo e Informativo**',
    c3
)

with open('scripts/build_stull_p3_complete.py', 'w', encoding='utf-8') as f:
    f.write(c3)


# ==================== PARTE 4 ====================
with open('scripts/build_stull_p4_complete.py', 'r', encoding='utf-8') as f:
    c4 = f.read()

# Ch 30 3 pilastri
c4 = re.sub(
    r'```\s*\+--+[\s\S]*?I TRE PILASTRI DELLA DEFINIZIONE DEL PROBLEMA[\s\S]*?\+--+\s*```',
    '''| Pilastro della Definizione | Funzione Progettuale | Domanda Guida |
| :--- | :--- | :--- |
| **1. COSA** | Delimita il perimetro esatto del progetto | Cosa creeremo e soprattutto cosa NON faremo? |
| **2. PERCHÉ** | Esplicita il bisogno profondo e il valore economico | Perché questo problema merita di essere risolto? |
| **3. COME** | Dichiara il principio operativo differenziante | Come la nostra soluzione supererà la seconda alternativa? |''',
    c4
)

# Ch 33 McResources
c4 = re.sub(
    r'```\s*\+--+[\s\S]*?IL CALCOLO ECONOMICO CHE SMONTA MCRESOURCES[\s\S]*?\+--+\s*```',
    '''| Voce di Bilancio | Importo Annuo ($) |
| :--- | :--- |
| Paga oraria media addetto friggitoria (BLS) | 10,93 $ / ora |
| Retribuzione annua a tempo pieno (2.080 ore) | ≈ 22.730,00 $ |
| Au-pair (10,72 $/h) a copertura oraria | − 22.290,00 $ |
| Addetto alla piscina (13,51 $/h, 1 ora/sett.) | − 702,52 $ |
| Personal trainer (18,85 $/h, sedute periodiche) | − 980,20 $ |
| **RISULTATO: DEBITO ANNUALE** | **− 1.242,72 $** |
*(Prima di pagare affitto, cibo, riscaldamento, tasse e... mance!)*''',
    c4
)

# Ch 33 formula
c4 = re.sub(
    r'\$\$5\.000\s*\\\\+text\{\s*operatori\}\s*\\\\+times\s*80\s*\\\\+text\{\s*pratiche\}\s*\\\\+times\s*6\s*\\\\+text\{\s*secondi\}\s*=\s*2\.400\.000\s*\\\\+text\{\s*secondi/giorno\}\s*=\s*666\s*\\\\+text\{\s*ore di lavoro\}\$\$',
    '**5.000 operatori × 80 pratiche × 6 secondi = 2.400.000 secondi/giorno = 666 ore di lavoro risparmiate al giorno**',
    c4
)

with open('scripts/build_stull_p4_complete.py', 'w', encoding='utf-8') as f:
    f.write(c4)

print("Tutte le sostituzioni mirate sono state eseguite!")
