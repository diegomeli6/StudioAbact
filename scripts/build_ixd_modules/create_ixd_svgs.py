#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera 5 schemi tecnici vettoriali SVG per Interaction Design (IxD)
Regola assoluta: ZERO EMOJI. Solo grafica vettoriale geometrica, label pulite e stili CSS moderni.
"""

import os

OUTPUT_DIR = "assets/corsi/dapl08/anno-1/interaction-design/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Schema Double Diamond (Design Thinking: Divergenza e Convergenza)
svg_diamond = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="diam1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="diam2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
    <marker id="arrDiamond" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <path d="M 1 1 L 6 3.5 L 1 6 Z" fill="#94a3b8" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">DESIGN THINKING: IL MODELLO A DOPPIO DIAMANTE (DOUBLE DIAMOND)</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Alternanza di Pensiero Divergente (Esplorazione) e Pensiero Convergente (Sintesi e Consegna)</text>

  <!-- DIAMANTE 1: IL PROBLEMA GIUSTO (Ricerca & Definizione) -->
  <g transform="translate(60, 110)">
    <!-- Poligono Diamante 1 -->
    <polygon points="0,170 170,10 340,170 170,330" fill="url(#diam1)" opacity="0.18" stroke="#38bdf8" stroke-width="2"/>
    <line x1="170" y1="10" x2="170" y2="330" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6 4"/>

    <!-- Etichette Fasi -->
    <text x="80" y="150" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="800">1. SCOPRI</text>
    <text x="80" y="170" text-anchor="middle" fill="#e2e8f0" font-size="12">EMPATHIZE</text>
    <text x="80" y="195" text-anchor="middle" fill="#94a3b8" font-size="10">Ricerca sul campo</text>
    <text x="80" y="210" text-anchor="middle" fill="#94a3b8" font-size="10">Etnografia &amp; Interviste</text>

    <text x="260" y="150" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="800">2. DEFINISCI</text>
    <text x="260" y="170" text-anchor="middle" fill="#e2e8f0" font-size="12">DEFINE</text>
    <text x="260" y="195" text-anchor="middle" fill="#94a3b8" font-size="10">Sintesi dei dati</text>
    <text x="260" y="210" text-anchor="middle" fill="#94a3b8" font-size="10">Personas &amp; Problem Statement</text>

    <!-- Header Diamante 1 -->
    <rect x="50" y="-15" width="240" height="26" rx="4" fill="#0369a1"/>
    <text x="170" y="3" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">PROGETTARE LA COSA GIUSTA</text>
  </g>

  <!-- FRECCIA CENTRALE: PROBLEM STATEMENT -->
  <circle cx="450" cy="280" r="14" fill="#fbbf24" stroke="#ffffff" stroke-width="2"/>
  <text x="450" y="284" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="900">BRIEF</text>

  <!-- DIAMANTE 2: LA SOLUZIONE GIUSTA (Sviluppo & Consegna) -->
  <g transform="translate(500, 110)">
    <!-- Poligono Diamante 2 -->
    <polygon points="0,170 170,10 340,170 170,330" fill="url(#diam2)" opacity="0.18" stroke="#a855f7" stroke-width="2"/>
    <line x1="170" y1="10" x2="170" y2="330" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="6 4"/>

    <!-- Etichette Fasi -->
    <text x="80" y="150" text-anchor="middle" fill="#c084fc" font-size="14" font-weight="800">3. SVILUPPA</text>
    <text x="80" y="170" text-anchor="middle" fill="#e2e8f0" font-size="12">IDEATE &amp; PROTOTYPE</text>
    <text x="80" y="195" text-anchor="middle" fill="#94a3b8" font-size="10">Brainstorming &amp; Wireframe</text>
    <text x="80" y="210" text-anchor="middle" fill="#94a3b8" font-size="10">Prototipi Low-Fi &amp; Hi-Fi</text>

    <text x="260" y="150" text-anchor="middle" fill="#c084fc" font-size="14" font-weight="800">4. CONSEGNA</text>
    <text x="260" y="170" text-anchor="middle" fill="#e2e8f0" font-size="12">TEST &amp; IMPLEMENT</text>
    <text x="260" y="195" text-anchor="middle" fill="#94a3b8" font-size="10">Usability Testing &amp; Feedback</text>
    <text x="260" y="210" text-anchor="middle" fill="#94a3b8" font-size="10">Rilascio e Iterazione Continua</text>

    <!-- Header Diamante 2 -->
    <rect x="50" y="-15" width="240" height="26" rx="4" fill="#6d28d9"/>
    <text x="170" y="3" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">PROGETTARE NEL MODO GIUSTO</text>
  </g>

  <!-- Footer Legenda Divergenza / Convergenza -->
  <g transform="translate(60, 460)">
    <rect width="780" height="42" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="150" y="26" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="700">DIVERGENTE: APRIRE OPZIONI</text>
    <text x="350" y="26" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="700">CONVERGENTE: FARE SCELTE</text>
    <text x="550" y="26" text-anchor="middle" fill="#c084fc" font-size="12" font-weight="700">DIVERGENTE: ESPLORARE IDEE</text>
    <text x="710" y="26" text-anchor="middle" fill="#34d399" font-size="12" font-weight="700">CONVERGENTE: TEST</text>
  </g>
</svg>
"""

# 2. Schema Interaction Matrix (Uomo vs Macchina)
svg_matrix = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <marker id="arrMatrixDown" markerWidth="7" markerHeight="7" refX="3.5" refY="5" orient="auto">
      <path d="M 1 1 L 6 1 L 3.5 6 Z" fill="#38bdf8" />
    </marker>
    <marker id="arrMatrixUp" markerWidth="7" markerHeight="7" refX="3.5" refY="1" orient="auto">
      <path d="M 1 6 L 6 6 L 3.5 1 Z" fill="#10b981" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">INTERACTION MATRIX: IL CIRCUITO UOMO-MACCHINA</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">I flussi bidirezionali tra apparato percettivo/motorio umano e controlli/display dell'artefatto</text>

  <!-- POLO SUPERIORE: ESSERE UMANO -->
  <g transform="translate(60, 95)">
    <rect width="780" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="780" height="32" rx="8" fill="#0284c7"/>
    <text x="390" y="22" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">POLO UMANO (SOGGETTO ATTIVO)</text>

    <!-- Recettori Sensoriali Umani (Sinistra) -->
    <rect x="25" y="45" width="350" height="85" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="40" y="70" fill="#38bdf8" font-size="13" font-weight="700">RECETTORI SENSORIALI (INPUT UOMO)</text>
    <text x="40" y="92" fill="#cbd5e1" font-size="11">&bull; Vista: percezione visiva (display, icone, colori, layout)</text>
    <text x="40" y="108" fill="#cbd5e1" font-size="11">&bull; Udito: feedback acustico (notifiche, voce, click sonori)</text>
    <text x="40" y="124" fill="#cbd5e1" font-size="11">&bull; Tatto: sensazione aptica (vibrazioni, texture, resistenza tasti)</text>

    <!-- Mezzi Motori Fisici Umani (Destra) -->
    <rect x="405" y="45" width="350" height="85" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
    <text x="420" y="70" fill="#fbbf24" font-size="13" font-weight="700">ATTUATORI FISICI (OUTPUT UOMO)</text>
    <text x="420" y="92" fill="#cbd5e1" font-size="11">&bull; Dita e Mani: tocco, swipe, pressione, rotazione manopole</text>
    <text x="420" y="108" fill="#cbd5e1" font-size="11">&bull; Voce: comandi vocali, riconoscimento del parlato</text>
    <text x="420" y="124" fill="#cbd5e1" font-size="11">&bull; Occhi e Corpo: tracciamento sguardo (eye-tracking), postura</text>
  </g>

  <!-- FLUSSI INTERATTIVI CENTRALI -->
  <!-- Freccia Azione Uomo -> Macchina (Destra, scende) -->
  <line x1="580" y1="250" x2="580" y2="295" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrMatrixDown)"/>
  <rect x="600" y="258" width="220" height="30" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1"/>
  <text x="710" y="278" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="700">AZIONE / INPUT UTENTE</text>

  <!-- Freccia Risposta Macchina -> Uomo (Sinistra, sale) -->
  <line x1="200" y1="295" x2="200" y2="250" stroke="#10b981" stroke-width="3" marker-end="url(#arrMatrixUp)"/>
  <rect x="220" y="258" width="220" height="30" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
  <text x="330" y="278" text-anchor="middle" fill="#34d399" font-size="11" font-weight="700">FEEDBACK / RISPOSTA MACCHINA</text>

  <!-- POLO INFERIORE: DISPOSITIVO COMPUTERIZZATO -->
  <g transform="translate(60, 310)">
    <rect width="780" height="150" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="780" height="32" rx="8" fill="#059669"/>
    <text x="390" y="22" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">POLO MACCHINA (ARTEFATTO DIGITALE / SISTEMA)</text>

    <!-- Risposte e Display della Macchina (Sinistra) -->
    <rect x="25" y="45" width="350" height="85" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="40" y="70" fill="#34d399" font-size="13" font-weight="700">MEZZI DI RISPOSTA (OUTPUT MACCHINA)</text>
    <text x="40" y="92" fill="#cbd5e1" font-size="11">&bull; Schermi &amp; Display: rendering grafico, animazioni, interfacce GUI</text>
    <text x="40" y="108" fill="#cbd5e1" font-size="11">&bull; Altoparlanti: segnali acustici, suoni di stato, sintesi vocale</text>
    <text x="40" y="124" fill="#cbd5e1" font-size="11">&bull; Motori Aptici: vibrazioni ERM/LRA per feedback di pressione</text>

    <!-- Controlli e Sensori della Macchina (Destra) -->
    <rect x="405" y="45" width="350" height="85" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="420" y="70" fill="#38bdf8" font-size="13" font-weight="700">CONTROLLI E SENSORI (INPUT MACCHINA)</text>
    <text x="420" y="92" fill="#cbd5e1" font-size="11">&bull; Sensori Touch: digitalizzatori capacitivi multitouch</text>
    <text x="420" y="108" fill="#cbd5e1" font-size="11">&bull; Controlli Fisici: pulsanti, encoder rotativi, pedali, leve</text>
    <text x="420" y="124" fill="#cbd5e1" font-size="11">&bull; Sensori Ambientali: microfoni, telecamere, accelerometri, LiDAR</text>
  </g>

  <!-- Note Footer -->
  <text x="450" y="495" text-anchor="middle" fill="#94a3b8" font-size="11">
    Il loop interattivo continuo si completa quando il feedback della macchina modifica il modello mentale dell'utente.
  </text>
</svg>
"""

# 3. Schema User Journey Map & Touchpoints
svg_journey = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="empathyLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="40%" stop-color="#ef4444"/>
      <stop offset="70%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">USER JOURNEY MAP: ANATOMIA DEI TOUCHPOINT ED EMPATIA</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Mappatura cronologica delle fasi, canali di contatto, emozioni e punti di dolore (Pain Points)</text>

  <!-- 5 Colonne delle Fasi della Journey -->
  <!-- 1. Awareness -->
  <g transform="translate(40, 95)">
    <rect width="155" height="40" rx="4" fill="#0284c7"/>
    <text x="77" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">1. AWARENESS</text>
  </g>
  <!-- 2. Consideration -->
  <g transform="translate(205, 95)">
    <rect width="155" height="40" rx="4" fill="#0369a1"/>
    <text x="77" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">2. RICERCA</text>
  </g>
  <!-- 3. Decision / Purchase -->
  <g transform="translate(370, 95)">
    <rect width="155" height="40" rx="4" fill="#6d28d9"/>
    <text x="77" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">3. ACQUISTO / USO</text>
  </g>
  <!-- 4. Retention -->
  <g transform="translate(535, 95)">
    <rect width="155" height="40" rx="4" fill="#b45309"/>
    <text x="77" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">4. ASSISTENZA</text>
  </g>
  <!-- 5. Advocacy -->
  <g transform="translate(700, 95)">
    <rect width="155" height="40" rx="4" fill="#047857"/>
    <text x="77" y="25" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">5. FIDELIZZAZIONE</text>
  </g>

  <!-- Griglia di sfondo delle corsie (Swimlanes) -->
  <rect x="40" y="145" width="815" height="55" fill="#1e293b" opacity="0.6"/>
  <text x="50" y="177" fill="#94a3b8" font-size="11" font-weight="700">AZIONI UTENTE</text>
  <text x="115" y="177" text-anchor="middle" fill="#e2e8f0" font-size="10">Vede post social</text>
  <text x="282" y="177" text-anchor="middle" fill="#e2e8f0" font-size="10">Confronta recensioni</text>
  <text x="447" y="177" text-anchor="middle" fill="#e2e8f0" font-size="10">Compila form checkout</text>
  <text x="612" y="177" text-anchor="middle" fill="#e2e8f0" font-size="10">Chiede supporto bot</text>
  <text x="777" y="177" text-anchor="middle" fill="#e2e8f0" font-size="10">Condivide recensione</text>

  <rect x="40" y="205" width="815" height="55" fill="#1e293b" opacity="0.4"/>
  <text x="50" y="237" fill="#38bdf8" font-size="11" font-weight="700">TOUCHPOINTS</text>
  <text x="115" y="237" text-anchor="middle" fill="#38bdf8" font-size="10">Instagram / Web Ad</text>
  <text x="282" y="237" text-anchor="middle" fill="#38bdf8" font-size="10">Sito web &amp; Forum</text>
  <text x="447" y="237" text-anchor="middle" fill="#38bdf8" font-size="10">App Mobile Gateway</text>
  <text x="612" y="237" text-anchor="middle" fill="#38bdf8" font-size="10">Chat Helpdesk / FAQ</text>
  <text x="777" y="237" text-anchor="middle" fill="#38bdf8" font-size="10">Community / Passaparola</text>

  <!-- Corsia Curva Emotiva (Empathy Curve) -->
  <rect x="40" y="265" width="815" height="110" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="50" y="285" fill="#f8fafc" font-size="11" font-weight="700">CURVA DELL'ESPERIENZA EMOTIVA</text>
  <text x="800" y="285" text-anchor="end" fill="#34d399" font-size="10">Felice (+)</text>
  <text x="800" y="365" text-anchor="end" fill="#ef4444" font-size="10">Frustrato (-)</text>

  <!-- Curva sinusoidale delle emozioni -->
  <path d="M 115 315 Q 200 290 282 300 T 447 360 T 612 320 T 777 285" 
        fill="none" stroke="url(#empathyLine)" stroke-width="3.5" stroke-linecap="round"/>

  <!-- Punti emotivi -->
  <circle cx="115" cy="315" r="5" fill="#38bdf8"/>
  <circle cx="282" cy="300" r="5" fill="#38bdf8"/>
  <circle cx="447" cy="360" r="6" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <circle cx="612" cy="320" r="5" fill="#fbbf24"/>
  <circle cx="777" cy="285" r="7" fill="#10b981" stroke="#ffffff" stroke-width="2"/>

  <!-- Callout Pain Point sul Checkout (447, 360) -->
  <rect x="365" y="385" width="165" height="36" rx="4" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
  <text x="447" y="401" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="700">PAIN POINT CRITICO</text>
  <text x="447" y="414" text-anchor="middle" fill="#ffffff" font-size="9">Checkout troppo lungo</text>

  <!-- Callout Peak-End Rule sulla fidelizzazione (777, 285) -->
  <rect x="690" y="385" width="175" height="36" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
  <text x="777" y="401" text-anchor="middle" fill="#6ee7b7" font-size="10" font-weight="700">PEAK-END SATISFACTION</text>
  <text x="777" y="414" text-anchor="middle" fill="#ffffff" font-size="9">Esperienza gratificante finale</text>

  <!-- OPPORTUNITA PROGETTUALI (Riga Inferiore) -->
  <rect x="40" y="440" width="815" height="55" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="50" y="465" fill="#a78bfa" font-size="11" font-weight="700">OPPORTUNITA</text>
  <text x="50" y="482" fill="#a78bfa" font-size="10">DI DESIGN</text>
  <text x="200" y="465" fill="#cbd5e1" font-size="10">&bull; Semplificare il form di registrazione a un click (Social Login / Apple Pay)</text>
  <text x="200" y="482" fill="#cbd5e1" font-size="10">&bull; Trasformare il punto di frustrazione in un micro-momento di delizia e trasparenza</text>
</svg>
"""

# 4. Schema Spazio Sociale e Habitus di Pierre Bourdieu
svg_bourdieu = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <marker id="arrBourdieu" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <path d="M 1 1 L 6 3.5 L 1 6 Z" fill="#94a3b8" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">SOCIOLOGIA DEI CONSUMI: LO SPAZIO SOCIALE DI PIERRE BOURDIEU</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Capitale Economico vs Capitale Culturale, Stratificazione e Merci di Posizione</text>

  <!-- Assi Cartesiani dello Spazio Sociale -->
  <!-- Asse Verticale: Volume Globale di Capitale (+ in alto, - in basso) -->
  <line x1="450" y1="440" x2="450" y2="105" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrBourdieu)"/>
  <text x="450" y="95" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="800">+ VOLUME COMPLESSIVO DI CAPITALE</text>
  <text x="450" y="465" text-anchor="middle" fill="#ef4444" font-size="12" font-weight="800">- VOLUME COMPLESSIVO DI CAPITALE</text>

  <!-- Asse Orizzontale: Composizione del Capitale (Culturale a SX, Economico a DX) -->
  <line x1="80" y1="270" x2="820" y2="270" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrBourdieu)"/>
  <text x="80" y="255" fill="#a855f7" font-size="12" font-weight="800">+ CAPITALE CULTURALE (Titoli, Arte, Saperi)</text>
  <text x="820" y="255" text-anchor="end" fill="#fbbf24" font-size="12" font-weight="800">+ CAPITALE ECONOMICO (Reddito, Patrimonio)</text>

  <!-- QUADRANTE 1: ALTO CULTURALE / MEDIO-BASSO ECONOMICO (In alto a SX) -->
  <g transform="translate(100, 130)">
    <rect width="280" height="110" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="15" y="25" fill="#c084fc" font-size="13" font-weight="700">Intellettuali, Docenti, Artisti</text>
    <text x="15" y="48" fill="#e2e8f0" font-size="11">&bull; Consumi: teatro d'avanguardia, cinema d'autore</text>
    <text x="15" y="66" fill="#e2e8f0" font-size="11">&bull; Gusto ascetico, rifiuto dell'ostentazione volgare</text>
    <text x="15" y="86" fill="#94a3b8" font-size="10">Valore simbolico &gt; Valore monetario</text>
  </g>

  <!-- QUADRANTE 2: ALTO ECONOMICO / ALTO CAPITALE GLOBALE (In alto a DX) -->
  <g transform="translate(520, 130)">
    <rect width="280" height="110" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="15" y="25" fill="#fbbf24" font-size="13" font-weight="700">Imprenditori, Ceo, Liberi Professionisti</text>
    <text x="15" y="48" fill="#e2e8f0" font-size="11">&bull; Consumi: beni di lusso, yacht, club esclusivi</text>
    <text x="15" y="66" fill="#e2e8f0" font-size="11">&bull; 'Merci di Posizione' e consumo vistoso vebleniano</text>
    <text x="15" y="86" fill="#94a3b8" font-size="10">Affermazione di status e potere economico</text>
  </g>

  <!-- QUADRANTE 3: CLASSI MEDIE E PICCOLA BORGHESIA (Centro) -->
  <g transform="translate(320, 290)">
    <rect width="260" height="70" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="130" y="23" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="700">Piccola Borghesia / Ceto Medio</text>
    <text x="130" y="43" text-anchor="middle" fill="#e2e8f0" font-size="10">Buona volonta culturale, iper-correttezza</text>
    <text x="130" y="58" text-anchor="middle" fill="#94a3b8" font-size="10">Emulazione aspirazionale delle classi alte</text>
  </g>

  <!-- QUADRANTE 4: CLASSI POPOLARI E SUBALTERNE (In basso) -->
  <g transform="translate(180, 380)">
    <rect width="540" height="60" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="270" y="23" text-anchor="middle" fill="#f87171" font-size="12" font-weight="700">Classi Popolari / Basso Capitale Economico e Culturale</text>
    <text x="270" y="43" text-anchor="middle" fill="#cbd5e1" font-size="10">Gusto della necessita: primato della quantita sulla qualita, della sostanza sull'apparenza formale</text>
  </g>

  <!-- Box Concetto di Habitus (Basso DX) -->
  <text x="450" y="495" text-anchor="middle" fill="#94a3b8" font-size="11">
    L'HABITUS e il sistema inconscio interiorizzato di disposizioni che struttura gusti, postura del corpo e scelte di design.
  </text>
</svg>
"""

# 5. Schema Economia dell'Esperienza e Trasformazione (Pine & Gilmore)
svg_esperienza = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="pyrGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="25%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#6d28d9"/>
      <stop offset="75%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">L'ECONOMIA DELL'ESPERIENZA: DALLA MATERIA ALLA TRASFORMAZIONE</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">La progressione del valore economico secondo B. Joseph Pine II e James H. Gilmore</text>

  <!-- Piramide del Valore Economico -->
  <!-- Livello 1: Commodities / Materie Prime -->
  <polygon points="120,440 780,440 730,370 170,370" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
  <text x="450" y="400" text-anchor="middle" fill="#cbd5e1" font-size="13" font-weight="700">1. COMMODITIES (Materie Prime Non Lavorate)</text>
  <text x="450" y="422" text-anchor="middle" fill="#94a3b8" font-size="11">Caffe grezzo in chicchi al chilo &bull; Valore fungibile: pochi centesimi a tazza</text>

  <!-- Livello 2: Goods / Beni Tangibili di Fabbrica -->
  <polygon points="170,370 730,370 670,300 230,300" fill="#0369a1" opacity="0.3" stroke="#0284c7" stroke-width="1.5"/>
  <text x="450" y="330" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="700">2. GOODS (Beni di Consumo / Prodotti Confezionati)</text>
  <text x="450" y="352" text-anchor="middle" fill="#cbd5e1" font-size="11">Caffe macinato in barattolo al supermercato &bull; Standardizzato e tangibile</text>

  <!-- Livello 3: Services / Servizi -->
  <polygon points="230,300 670,300 600,230 300,230" fill="#6d28d9" opacity="0.3" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="450" y="260" text-anchor="middle" fill="#c084fc" font-size="13" font-weight="700">3. SERVICES (Servizi Intangibili su Richiesta)</text>
  <text x="450" y="282" text-anchor="middle" fill="#cbd5e1" font-size="11">Caffe espresso servito al bancone del bar &bull; Si paga la comodita e il tempo</text>

  <!-- Livello 4: Experiences / Esperienze Memorabili -->
  <polygon points="300,230 600,230 530,160 370,160" fill="#d97706" opacity="0.35" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="450" y="190" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="700">4. EXPERIENCES (Esperienze Immersive e Memorabili)</text>
  <text x="450" y="212" text-anchor="middle" fill="#cbd5e1" font-size="11">Starbucks / Cafe Florian a Venezia a 12 euro &bull; Si paga l'atmosfera, il rito e il ricordo</text>

  <!-- Livello 5: Transformations / Trasformazioni dell'Individuo -->
  <polygon points="370,160 530,160 450,90" fill="#e11d48" opacity="0.45" stroke="#f43f5e" stroke-width="2"/>
  <text x="450" y="128" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">5. TRASFORMAZIONE</text>
  <text x="450" y="145" text-anchor="middle" fill="#fca5a5" font-size="10">Cambiamento duraturo di se</text>

  <!-- Frecce laterali di salita del valore -->
  <!-- Sinistra: Prezzo / Valore aggiunto -->
  <line x1="70" y1="440" x2="70" y2="100" stroke="#38bdf8" stroke-width="2" marker-end="url(#pyrGrad)"/>
  <text x="60" y="270" text-anchor="middle" transform="rotate(-90 60,270)" fill="#38bdf8" font-size="12" font-weight="700">VALORE ECONOMICO AGGIUNTO &amp; PREZZO</text>

  <!-- Destra: Rilevanza per l'Utente / Personalizzazione -->
  <line x1="830" y1="440" x2="830" y2="100" stroke="#f43f5e" stroke-width="2"/>
  <text x="840" y="270" text-anchor="middle" transform="rotate(90 840,270)" fill="#f43f5e" font-size="12" font-weight="700">PERSONALIZZAZIONE &amp; IMPATTO SULLA VITA</text>

  <!-- Footer sintetico -->
  <rect x="120" y="465" width="660" height="35" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="450" y="487" text-anchor="middle" fill="#cbd5e1" font-size="11">
    Oggi il consumatore non cerca piu solo l'intrattenimento temporaneo, ma prodotti e servizi che trasformino la propria identita.
  </text>
</svg>
"""

# 6. Schema Affordance: James Gibson vs Donald Norman
svg_affordance = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="affGibson" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="affNorman" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">TEORIA DELL'AFFORDANCE: DA JAMES GIBSON A DONALD NORMAN</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Dalla Proprieta Fisica Ecologica all'Invito all'Uso Percepito e ai Segnalatori (Signifiers)</text>

  <!-- COLONNA SINISTRA: JAMES GIBSON (1979) -->
  <g transform="translate(40, 95)">
    <rect width="390" height="360" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="390" height="42" rx="10" fill="url(#affGibson)"/>
    <text x="195" y="27" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="700">JAMES J. GIBSON (1979) — Ecologia della Percezione</text>

    <text x="25" y="70" fill="#38bdf8" font-size="13" font-weight="700">CONCETTO:</text>
    <text x="25" y="92" fill="#cbd5e1" font-size="12">L'affordance e una proprieta FISICA e OGGETTIVA.</text>
    <text x="25" y="110" fill="#cbd5e1" font-size="12">Esiste indipendentemente dalla capacita del soggetto</text>
    <text x="25" y="128" fill="#cbd5e1" font-size="12">di riconoscerla o percepirla.</text>

    <rect x="20" y="145" width="350" height="85" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="170" fill="#f8fafc" font-size="12" font-weight="600">Relazione Attore - Ambiente:</text>
    <text x="35" y="192" fill="#94a3b8" font-size="11">• Una superficie orizzontale solida e "sedibile" (chair-affordance).</text>
    <text x="35" y="212" fill="#94a3b8" font-size="11">• Un gradino e "salibile" in base alle proporzioni fisiche del corpo.</text>

    <text x="25" y="255" fill="#38bdf8" font-size="13" font-weight="700">IMPLICAZIONE FILOSOFICA:</text>
    <text x="25" y="277" fill="#cbd5e1" font-size="12">La percezione e DIRETTA, non richiede elaborazione</text>
    <text x="25" y="295" fill="#cbd5e1" font-size="12">cognitiva complessa: l'ambiente comunica possibilita</text>
    <text x="25" y="313" fill="#cbd5e1" font-size="12">di azione all'organismo vivente.</text>

    <rect x="20" y="325" width="350" height="24" rx="4" fill="#0369a1" opacity="0.3"/>
    <text x="195" y="341" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">Reale, Invariante, Legata alla biomeccanica</text>
  </g>

  <!-- COLONNA DESTRA: DONALD NORMAN (1988/2013) -->
  <g transform="translate(470, 95)">
    <rect width="390" height="360" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
    <rect width="390" height="42" rx="10" fill="url(#affNorman)"/>
    <text x="195" y="27" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="700">DONALD A. NORMAN (1988) — Design &amp; Scienze Cognitive</text>

    <text x="25" y="70" fill="#c084fc" font-size="13" font-weight="700">CONCETTO:</text>
    <text x="25" y="92" fill="#cbd5e1" font-size="12">L'affordance e PERCEPITA (Perceived Affordance).</text>
    <text x="25" y="110" fill="#cbd5e1" font-size="12">Cio che conta e come l'utente interpreta l'oggetto</text>
    <text x="25" y="128" fill="#cbd5e1" font-size="12">attraverso il proprio modello mentale.</text>

    <rect x="20" y="145" width="350" height="85" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="35" y="170" fill="#f8fafc" font-size="12" font-weight="600">La Triade di Norman (IxD):</text>
    <text x="35" y="192" fill="#94a3b8" font-size="11">• Affordance Reale: cosa l'oggetto puo fare fisicamente.</text>
    <text x="35" y="212" fill="#94a3b8" font-size="11">• Segnalatore (Signifier): indizio visivo/tattile (freccia, pulsante).</text>

    <text x="25" y="255" fill="#c084fc" font-size="13" font-weight="700">ESEMPIO CLASSICO DELLE PORTE:</text>
    <text x="25" y="277" fill="#cbd5e1" font-size="12">• Piastra piatta = SPINGERE (Affordance evidente)</text>
    <text x="25" y="295" fill="#cbd5e1" font-size="12">• Maniglia a staffa = TIRARE (Invito errato se bisogna spingere!)</text>
    <text x="25" y="313" fill="#f87171" font-size="11">"Porte di Norman": errori di usabilita per indizi fuorvianti.</text>

    <rect x="20" y="325" width="350" height="24" rx="4" fill="#6d28d9" opacity="0.3"/>
    <text x="195" y="341" text-anchor="middle" fill="#c084fc" font-size="11" font-weight="600">Percepita, Culturale, Mediata da Signifiers</text>
  </g>

  <!-- Barra inferiore sintesi -->
  <rect x="40" y="470" width="820" height="34" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="450" y="492" text-anchor="middle" fill="#f1f5f9" font-size="11">
    Regola aurea dell'Interaction Design: Se un utente deve leggere un cartello "Spingere", il design dell'interfaccia ha fallito.
  </text>
</svg>
"""

# 7. Schema Personas di Alan Cooper (Template Strutturale Archetipo Utente)
svg_personas = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="pHead" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <text x="450" y="40" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">LA METODOLOGIA DELLE PERSONAS (ALAN COOPER)</text>
  <text x="450" y="64" text-anchor="middle" fill="#94a3b8" font-size="13">Archetipo Fittizio Basato su Dati Reali di Ricerca Etnografica e Comportamentale</text>

  <!-- COLONNA 1: SCHEDA IDENTITARIA DELL'ARCHETIPO -->
  <g transform="translate(40, 85)">
    <rect width="250" height="410" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <rect width="250" height="40" rx="8" fill="url(#pHead)"/>
    <text x="125" y="25" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="700">PROFILO ARCHETIPO</text>

    <!-- Avatar Placeholder Vettoriale (sagoma geometrica senza emoji) -->
    <rect x="75" y="55" width="100" height="100" rx="50" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="125" cy="90" r="24" fill="#38bdf8" opacity="0.6"/>
    <path d="M 95 145 C 95 120, 155 120, 155 145 Z" fill="#38bdf8" opacity="0.6"/>

    <text x="125" y="175" text-anchor="middle" fill="#f8fafc" font-size="15" font-weight="700">Marco, 28 anni</text>
    <text x="125" y="195" text-anchor="middle" fill="#38bdf8" font-size="12">Junior Creative Technologist</text>
    <text x="125" y="215" text-anchor="middle" fill="#94a3b8" font-size="11">Catania / Lavoro ibrido</text>

    <line x1="20" y1="230" x2="230" y2="230" stroke="#334155" stroke-width="1"/>

    <text x="25" y="250" fill="#cbd5e1" font-size="11" font-weight="700">LIVELLO DIGITALE:</text>
    <rect x="25" y="260" width="200" height="8" rx="4" fill="#0f172a"/>
    <rect x="25" y="260" width="170" height="8" rx="4" fill="#10b981"/>

    <text x="25" y="288" fill="#cbd5e1" font-size="11" font-weight="700">DISPOSITIVI PREVALENTI:</text>
    <text x="25" y="306" fill="#94a3b8" font-size="11">• Laptop MacBook Pro</text>
    <text x="25" y="322" fill="#94a3b8" font-size="11">• Smartphone 5G in mobilita</text>

    <!-- Citazione tipica -->
    <rect x="15" y="345" width="220" height="50" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="125" y="365" text-anchor="middle" fill="#fde047" font-size="10" font-style="italic">"Ho bisogno di strumenti che</text>
    <text x="125" y="380" text-anchor="middle" fill="#fde047" font-size="10" font-style="italic">non interrompano il mio flusso."</text>
  </g>

  <!-- COLONNA 2: OBIETTIVI E MODELLO MENTALE -->
  <g transform="translate(310, 85)">
    <!-- OBIETTIVI (GOALS) -->
    <rect width="270" height="195" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="32" rx="8" fill="#065f46"/>
    <text x="135" y="21" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">OBIETTIVI DELL'UTENTE (GOALS)</text>

    <text x="20" y="58" fill="#34d399" font-size="12" font-weight="700">[Life Goals - Obiettivi di Vita]</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="11">• Sentirsi autonomo, competente e stimato.</text>

    <text x="20" y="105" fill="#34d399" font-size="12" font-weight="700">[End Goals - Obiettivi Finali]</text>
    <text x="20" y="122" fill="#cbd5e1" font-size="11">• Finalizzare un progetto interattivo nei tempi.</text>
    <text x="20" y="139" fill="#cbd5e1" font-size="11">• Condividere prototipi con clienti senza attrito.</text>

    <text x="20" y="165" fill="#34d399" font-size="12" font-weight="700">[Experience Goals - Obiettivi Esperienziali]</text>
    <text x="20" y="182" fill="#cbd5e1" font-size="11">• Non sentirsi sopraffatto dalla complessita tecnica.</text>

    <!-- MODELLO MENTALE & COMPORTAMENTI -->
    <g transform="translate(0, 210)">
      <rect width="270" height="195" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="270" height="32" rx="8" fill="#0369a1"/>
      <text x="135" y="21" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">MODELLO MENTALE &amp; HABITUS</text>

      <text x="20" y="58" fill="#38bdf8" font-size="12" font-weight="700">• Attitudine all'esplorazione:</text>
      <text x="20" y="75" fill="#cbd5e1" font-size="11">Preferisce tentare e cliccare piuttosto che</text>
      <text x="20" y="90" fill="#cbd5e1" font-size="11">consultare manuali d'uso o guide scritte.</text>

      <text x="20" y="118" fill="#38bdf8" font-size="12" font-weight="700">• Capitale Culturale (Bourdieu):</text>
      <text x="20" y="135" fill="#cbd5e1" font-size="11">Sensibilita visiva elevata, rigore estetico,</text>
      <text x="20" y="150" fill="#cbd5e1" font-size="11">attento a dettagli tipografici e micro-animazioni.</text>

      <text x="20" y="175" fill="#38bdf8" font-size="12" font-weight="700">• Stile di Vita (VALS):</text>
      <text x="20" y="190" fill="#cbd5e1" font-size="11">"Experiential / Innovatore"</text>
    </g>
  </g>

  <!-- COLONNA 3: FRUSTRAZIONI (PAIN POINTS) E IMPLICAZIONI PROGETTUALI -->
  <g transform="translate(600, 85)">
    <!-- FRUSTRAZIONI -->
    <rect width="260" height="195" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="260" height="32" rx="8" fill="#9f1239"/>
    <text x="130" y="21" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">PAIN POINTS &amp; FRUSTRAZIONI</text>

    <text x="18" y="58" fill="#fda4af" font-size="11" font-weight="700">• Lentezza e Caricamenti Invisibili:</text>
    <text x="18" y="75" fill="#cbd5e1" font-size="11">Interfacce prive di feedback immediato o</text>
    <text x="18" y="90" fill="#cbd5e1" font-size="11">con stati di caricamento opachi.</text>

    <text x="18" y="115" fill="#fda4af" font-size="11" font-weight="700">• Troppi Passaggi Obbligatori:</text>
    <text x="18" y="132" fill="#cbd5e1" font-size="11">Flussi lineari rigidi che impediscono di</text>
    <text x="18" y="147" fill="#cbd5e1" font-size="11">tornare indietro o modificare scelte.</text>

    <text x="18" y="172" fill="#fda4af" font-size="11" font-weight="700">• Notifiche Invasivi e Spam:</text>
    <text x="18" y="187" fill="#cbd5e1" font-size="11">Interruzioni continue che spezzano l'attenzione.</text>

    <!-- DESIGN PRINCIPLES DEDOTTI -->
    <g transform="translate(0, 210)">
      <rect width="260" height="195" rx="8" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
      <rect width="260" height="32" rx="8" fill="#854d0e"/>
      <text x="130" y="21" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">LINEE GUIDA PER IL PROGETTO</text>

      <text x="18" y="58" fill="#fde047" font-size="11" font-weight="700">1. Feedback Istantaneo (&lt; 100ms):</text>
      <text x="18" y="75" fill="#cbd5e1" font-size="11">Micro-interazioni visive su ogni stato d'azione.</text>

      <text x="18" y="105" fill="#fde047" font-size="11" font-weight="700">2. Controllo e Libertà Utente:</text>
      <text x="18" y="122" fill="#cbd5e1" font-size="11">Funzione Undo/Redo sempre accessibile.</text>

      <text x="18" y="152" fill="#fde047" font-size="11" font-weight="700">3. Riduzione del Carico Cognitivo:</text>
      <text x="18" y="170" fill="#cbd5e1" font-size="11">Progressive disclosure delle impostazioni avanzate.</text>
    </g>
  </g>
</svg>
"""

svg_files = {
    "schema_design_thinking_diamond.svg": svg_diamond,
    "schema_interaction_matrix.svg": svg_matrix,
    "schema_user_journey_touchpoints.svg": svg_journey,
    "schema_stili_di_vita_bourdieu.svg": svg_bourdieu,
    "schema_piramide_esperienza_trasformazione.svg": svg_esperienza,
    "schema_affordance_gibson_norman.svg": svg_affordance,
    "schema_personas_cooper_template.svg": svg_personas
}

for fname, content in svg_files.items():
    path = os.path.join(OUTPUT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Creato {fname} in {OUTPUT_DIR}")

print("Tutti i 7 SVG tecnici per Interaction Design creati con successo!")

