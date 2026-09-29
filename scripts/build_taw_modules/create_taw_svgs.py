#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera 5 schemi tecnici vettoriali SVG per Tecniche Audiovisive per il Web (TAW)
Regola assoluta: ZERO EMOJI. Solo grafica vettoriale geometrica, label pulite e stili CSS moderni.
"""

import os

OUTPUT_DIR = "assets/corsi/dapl08/anno-1/tecniche-audiovisive/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Schema Movimenti di Macchina
svg_movimenti = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="panGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <linearGradient id="tiltGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#fb923c"/>
    </linearGradient>
    <linearGradient id="dollyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
    <marker id="arrowHead" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 1 1 L 7 4 L 1 7 Z" fill="#38bdf8" />
    </marker>
    <marker id="arrowHeadRose" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 1 1 L 7 4 L 1 7 Z" fill="#f43f5e" />
    </marker>
    <marker id="arrowHeadGreen" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 1 1 L 7 4 L 1 7 Z" fill="#10b981" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">CINEMATOGRAFIA: MAPPA DEI MOVIMENTI DI CAMERA</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Assi di rotazione (ottica fissa) vs Traslazioni fisiche nello spazio filmico</text>

  <!-- Box 1: ROTAZIONI SU ASSE (Testa/Treppiede) -->
  <g transform="translate(40, 95)">
    <rect width="395" height="185" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="395" height="34" rx="8" fill="#334155" opacity="0.6"/>
    <text x="20" y="23" fill="#38bdf8" font-size="14" font-weight="700" letter-spacing="0.5">ROTAZIONI SU ASSE (Camera Stazionaria)</text>

    <!-- Panoramica PAN -->
    <circle cx="55" cy="80" r="24" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 38 74 Q 55 60 72 74" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowHead)"/>
    <text x="95" y="76" fill="#f8fafc" font-size="14" font-weight="600">PAN (Panoramica Orizzontale)</text>
    <text x="95" y="94" fill="#94a3b8" font-size="12">Rotazione sull'asse pan (Dx/Sx). Variante: Whip Pan (a schiaffo)</text>

    <!-- Tilt -->
    <circle cx="55" cy="140" r="24" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <path d="M 50 155 Q 40 140 50 125" fill="none" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrowHeadRose)"/>
    <text x="95" y="136" fill="#f8fafc" font-size="14" font-weight="600">TILT (Panoramica Verticale)</text>
    <text x="95" y="154" fill="#94a3b8" font-size="12">Rotazione su asse di beccheggio: Tilt Up (in alto) / Tilt Down (in basso)</text>
  </g>

  <!-- Box 2: TRASLAZIONI FISICHE (Carrello, Dolly, Gru) -->
  <g transform="translate(465, 95)">
    <rect width="395" height="185" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="395" height="34" rx="8" fill="#334155" opacity="0.6"/>
    <text x="20" y="23" fill="#10b981" font-size="14" font-weight="700" letter-spacing="0.5">TRASLAZIONI NELLO SPAZIO (Dolly, Track, Crane)</text>

    <!-- Dolly In / Out -->
    <circle cx="55" cy="80" r="24" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <line x1="42" y1="80" x2="68" y2="80" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrowHeadGreen)"/>
    <text x="95" y="76" fill="#f8fafc" font-size="14" font-weight="600">DOLLY (In / Out)</text>
    <text x="95" y="94" fill="#94a3b8" font-size="12">Spostamento su ruote/binario: Push-In (avanti) / Pull-Out (indietro)</text>

    <!-- Truck / Boom -->
    <circle cx="55" cy="140" r="24" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <line x1="45" y1="140" x2="65" y2="140" stroke="#fbbf24" stroke-width="2"/>
    <line x1="55" y1="150" x2="55" y2="130" stroke="#fbbf24" stroke-width="2"/>
    <text x="95" y="136" fill="#f8fafc" font-size="14" font-weight="600">TRUCK (Crab) &amp; BOOM (Pedestal)</text>
    <text x="95" y="154" fill="#94a3b8" font-size="12">Truck: traslazione laterale parallela. Boom/Jib: elevazione verticale</text>
  </g>

  <!-- Box 3: MOVIMENTI COMPLESSI & EFFETTI SPECIALI (Riga inferiore) -->
  <g transform="translate(40, 295)">
    <rect width="820" height="195" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="820" height="34" rx="8" fill="#334155" opacity="0.6"/>
    <text x="20" y="23" fill="#a78bfa" font-size="14" font-weight="700" letter-spacing="0.5">DINAMICHE COMPLESSE: DOLLY ZOOM, PARALLAX, SNORRICAM</text>

    <!-- Item 1: Dolly Zoom / Vertigo -->
    <g transform="translate(25, 50)">
      <rect width="245" height="125" rx="6" fill="#0f172a" stroke="#a78bfa" stroke-width="1"/>
      <text x="15" y="26" fill="#c084fc" font-size="13" font-weight="700">DOLLY ZOOM (Vertigo)</text>
      <text x="15" y="48" fill="#e2e8f0" font-size="12" font-weight="600">Dolly In + Zoom Out</text>
      <text x="15" y="66" fill="#94a3b8" font-size="11">o viceversa (Dolly Out + Zoom In).</text>
      <text x="15" y="86" fill="#94a3b8" font-size="11">Il soggetto resta immutato,</text>
      <text x="15" y="104" fill="#38bdf8" font-size="11">lo sfondo si dilata o comprime.</text>
    </g>

    <!-- Item 2: Parallax Shot -->
    <g transform="translate(288, 50)">
      <rect width="245" height="125" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="15" y="26" fill="#38bdf8" font-size="13" font-weight="700">PARALLAX SHOT</text>
      <text x="15" y="48" fill="#e2e8f0" font-size="12" font-weight="600">PAN + Dolly Opposto</text>
      <text x="15" y="66" fill="#94a3b8" font-size="11">La camera scorre lateralmente</text>
      <text x="15" y="86" fill="#94a3b8" font-size="11">mentre ruota in senso contrario.</text>
      <text x="15" y="104" fill="#fb923c" font-size="11">Profondita prospettica dinamica.</text>
    </g>

    <!-- Item 3: Snorricam -->
    <g transform="translate(550, 50)">
      <rect width="245" height="125" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="1"/>
      <text x="15" y="26" fill="#f43f5e" font-size="13" font-weight="700">SNORRICAM (Bodycam)</text>
      <text x="15" y="48" fill="#e2e8f0" font-size="12" font-weight="600">Rig ancorato al torso</text>
      <text x="15" y="66" fill="#94a3b8" font-size="11">Obiettivo puntato sull'attore.</text>
      <text x="15" y="86" fill="#94a3b8" font-size="11">Il volto resta immobile nel frame</text>
      <text x="15" y="104" fill="#f43f5e" font-size="11">mentre il mondo oscilla frenetico.</text>
    </g>
  </g>
</svg>
"""

# 2. Schema Regola dei 180 Gradi
svg_180 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <marker id="arrow180" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 1 1 L 7 4 L 1 7 Z" fill="#fbbf24" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">GRAMMATICA FILMICA: LA REGOLA DEI 180 GRADI</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Asse dell'Azione, Raccordo di Sguardo e Conservazione dello Spazio Schermo</text>

  <!-- Sfondo semi-cerchio autorizzato (Area Verde) -->
  <path d="M 150 250 A 300 300 0 0 0 750 250 Z" fill="#065f46" opacity="0.15"/>
  <!-- Sfondo semi-cerchio vietato (Area Rossa) -->
  <path d="M 150 250 A 300 300 0 0 1 750 250 Z" fill="#991b1b" opacity="0.12"/>

  <!-- Asse dell'Azione (Linea orizzontale tratteggiata) -->
  <line x1="100" y1="250" x2="800" y2="250" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="8 6"/>
  <text x="450" y="240" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="700" letter-spacing="1">ASSE DELL'AZIONE (LINEA GUIDA DELLO SGUARDO)</text>

  <!-- Personaggio A (Sinistra) -->
  <circle cx="320" cy="250" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="320" y="256" text-anchor="middle" fill="#38bdf8" font-size="15" font-weight="700">A</text>
  <!-- Freccia sguardo A verso B -->
  <line x1="360" y1="245" x2="430" y2="245" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow180)"/>
  <text x="320" y="205" text-anchor="middle" fill="#e2e8f0" font-size="12" font-weight="600">Attore A</text>
  <text x="320" y="222" text-anchor="middle" fill="#94a3b8" font-size="11">Guarda verso Destra</text>

  <!-- Personaggio B (Destra) -->
  <circle cx="580" cy="250" r="30" fill="#1e293b" stroke="#f43f5e" stroke-width="3"/>
  <text x="580" y="256" text-anchor="middle" fill="#f43f5e" font-size="15" font-weight="700">B</text>
  <!-- Freccia sguardo B verso A -->
  <line x1="540" y1="255" x2="470" y2="255" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow180)"/>
  <text x="580" y="205" text-anchor="middle" fill="#e2e8f0" font-size="12" font-weight="600">Attore B</text>
  <text x="580" y="222" text-anchor="middle" fill="#94a3b8" font-size="11">Guarda verso Sinistra</text>

  <!-- Telecamera 1 (Master / Totale) -->
  <g transform="translate(430, 420)">
    <rect x="-35" y="-20" width="70" height="40" rx="6" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
    <polygon points="0,-20 -15,-35 15,-35" fill="#34d399"/>
    <text x="0" y="5" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="800">CAM 1</text>
    <text x="0" y="38" text-anchor="middle" fill="#34d399" font-size="12" font-weight="600">Totale (Master)</text>
  </g>

  <!-- Telecamera 2 (Close-up su B da lato consentito) -->
  <g transform="translate(230, 360)">
    <rect x="-35" y="-20" width="70" height="40" rx="6" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
    <polygon points="15,-18 30,-30 10,-35" fill="#34d399"/>
    <text x="0" y="5" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="800">CAM 2</text>
    <text x="0" y="38" text-anchor="middle" fill="#34d399" font-size="12" font-weight="600">Primo Piano B</text>
    <text x="0" y="52" text-anchor="middle" fill="#94a3b8" font-size="10">B guarda a SX</text>
  </g>

  <!-- Telecamera 3 (Close-up su A da lato consentito) -->
  <g transform="translate(670, 360)">
    <rect x="-35" y="-20" width="70" height="40" rx="6" fill="#10b981" stroke="#34d399" stroke-width="1.5"/>
    <polygon points="-15,-18 -30,-30 -10,-35" fill="#34d399"/>
    <text x="0" y="5" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="800">CAM 3</text>
    <text x="0" y="38" text-anchor="middle" fill="#34d399" font-size="12" font-weight="600">Primo Piano A</text>
    <text x="0" y="52" text-anchor="middle" fill="#94a3b8" font-size="10">A guarda a DX</text>
  </g>

  <!-- Telecamera X (Scavalcamento di campo - Errore) -->
  <g transform="translate(450, 115)">
    <rect x="-40" y="-18" width="80" height="36" rx="6" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
    <polygon points="0,18 -15,32 15,32" fill="#f87171"/>
    <text x="0" y="4" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="800">CAM X (VIETATA)</text>
    <text x="0" y="-26" text-anchor="middle" fill="#f87171" font-size="12" font-weight="700">SCAVALCAMENTO DI CAMPO</text>
    <text x="0" y="-12" text-anchor="middle" fill="#94a3b8" font-size="10">Inverte gli sguardi e disorienta lo spettatore</text>
  </g>

  <!-- Badge Zona Consentita -->
  <rect x="50" y="445" width="220" height="50" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <circle cx="70" cy="470" r="8" fill="#10b981"/>
  <text x="90" y="466" fill="#34d399" font-size="12" font-weight="700">ZONA CONSENTITA (180°)</text>
  <text x="90" y="482" fill="#94a3b8" font-size="10">Le camere mantengono la coerenza</text>

  <!-- Badge Zona Vietata -->
  <rect x="630" y="445" width="220" height="50" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="650" cy="470" r="8" fill="#ef4444"/>
  <text x="670" y="466" fill="#f87171" font-size="12" font-weight="700">ZONA VIETATA</text>
  <text x="670" y="482" fill="#94a3b8" font-size="10">Rottura dell'orientamento spaziale</text>
</svg>
"""

# 3. Schema Struttura Drammaturgica in Tre Atti (Syd Field)
svg_tre_atti = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="climaxGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#f43f5e"/>
    </linearGradient>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">SCENEGGIATURA: STRUTTURA RESTAURATIVA IN TRE ATTI</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Il paradigma narrativo classico di Syd Field, Robert McKee e il dramma ben fatto di Eugène Scribe</text>

  <!-- Griglia proporzioni 3 Atti (30 pag / 60 pag / 30 pag) -->
  <!-- Atto 1: 0 - 240 px (25%) -->
  <rect x="50" y="95" width="200" height="30" fill="#1e293b" stroke="#38bdf8" stroke-width="1" rx="4"/>
  <text x="150" y="115" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="700">ATTO I: SETUP (~25%)</text>

  <!-- Atto 2: 240 - 640 px (50%) -->
  <rect x="260" y="95" width="380" height="30" fill="#1e293b" stroke="#fbbf24" stroke-width="1" rx="4"/>
  <text x="450" y="115" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="700">ATTO II: CONFRONTO E LOTTA (~50%)</text>

  <!-- Atto 3: 640 - 850 px (25%) -->
  <rect x="650" y="95" width="200" height="30" fill="#1e293b" stroke="#f43f5e" stroke-width="1" rx="4"/>
  <text x="750" y="115" text-anchor="middle" fill="#f43f5e" font-size="13" font-weight="700">ATTO III: RISOLUZIONE (~25%)</text>

  <!-- Curva della Tensione Drammatica -->
  <path d="M 60 400 Q 150 380 200 340 T 260 330 T 450 250 T 640 220 T 730 160 Q 770 150 840 370" 
        fill="none" stroke="url(#climaxGrad)" stroke-width="4.5" stroke-linecap="round"/>

  <!-- Punti notevoli sulla curva -->
  <!-- 1. Inciting Incident -->
  <circle cx="140" cy="380" r="7" fill="#38bdf8"/>
  <text x="140" y="420" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="700">INCITING INCIDENT</text>
  <text x="140" y="435" text-anchor="middle" fill="#94a3b8" font-size="10">Rottura dell'equilibrio</text>

  <!-- 2. Plot Point 1 -->
  <circle cx="260" cy="330" r="8" fill="#fbbf24" stroke="#f8fafc" stroke-width="2"/>
  <text x="260" y="300" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="800">PLOT POINT 1</text>
  <text x="260" y="315" text-anchor="middle" fill="#f8fafc" font-size="10">Punto di non ritorno (Falsa soluzione)</text>

  <!-- 3. Midpoint -->
  <circle cx="450" cy="250" r="8" fill="#fbbf24"/>
  <text x="450" y="215" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="800">MIDPOINT</text>
  <text x="450" y="230" text-anchor="middle" fill="#94a3b8" font-size="10">Alzamento della posta in gioco</text>

  <!-- 4. All is Lost / Plot Point 2 -->
  <circle cx="640" cy="220" r="8" fill="#f43f5e" stroke="#f8fafc" stroke-width="2"/>
  <text x="640" y="185" text-anchor="middle" fill="#f43f5e" font-size="12" font-weight="800">PLOT POINT 2</text>
  <text x="640" y="200" text-anchor="middle" fill="#f8fafc" font-size="10">Crisi totale / "Tutto e perduto"</text>

  <!-- 5. Climax -->
  <circle cx="730" cy="160" r="9" fill="#f43f5e" stroke="#ffffff" stroke-width="3"/>
  <text x="730" y="135" text-anchor="middle" fill="#f87171" font-size="13" font-weight="900">CLIMAX</text>
  <text x="730" y="150" text-anchor="middle" fill="#f8fafc" font-size="10">Scontro finale risolutivo</text>

  <!-- 6. Status Quo Restaurato -->
  <circle cx="840" cy="370" r="7" fill="#10b981"/>
  <text x="830" y="415" text-anchor="middle" fill="#34d399" font-size="11" font-weight="700">NUOVO STATUS QUO</text>
  <text x="830" y="430" text-anchor="middle" fill="#94a3b8" font-size="10">Redenzione &amp; Ordine</text>

  <!-- Footer box chiarimenti -->
  <rect x="50" y="460" width="800" height="40" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="450" y="484" text-anchor="middle" fill="#cbd5e1" font-size="12">
    In 120 pagine di sceneggiatura: Atto I = 30 pag, Atto II = 60 pag, Atto III = 30 pag (1 pagina di sceneggiatura = 1 minuto di film)
  </text>
</svg>
"""

# 4. Schema Fasi della Produzione Audiovisiva (Metodo Bruno Munari)
svg_produzione = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <marker id="arrowProd" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <path d="M 1 1 L 6 3.5 L 1 6 Z" fill="#94a3b8" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">ITER PROGETTUALE: DALL'IDEA AL MASTER WEB</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Le 4 macro-fasi della produzione audiovisiva secondo il metodo rigoroso di Bruno Munari</text>

  <!-- FASE 1: SCRITTURA E SVILUPPO -->
  <g transform="translate(40, 95)">
    <rect width="185" height="380" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#0284c7"/>
    <text x="92" y="24" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">1. SVILUPPO &amp; TESTO</text>

    <g transform="translate(15, 55)">
      <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">A. Idea &amp; 5W</text>
      <text x="0" y="32" fill="#94a3b8" font-size="10">Who, What, When, Where, Why</text>

      <text x="0" y="62" fill="#38bdf8" font-size="12" font-weight="700">B. Soggetto</text>
      <text x="0" y="78" fill="#94a3b8" font-size="10">Racconto narrativo continuo</text>

      <text x="0" y="108" fill="#38bdf8" font-size="12" font-weight="700">C. Scaletta</text>
      <text x="0" y="124" fill="#94a3b8" font-size="10">Elenco numerato delle scene</text>

      <text x="0" y="154" fill="#38bdf8" font-size="12" font-weight="700">D. Trattamento</text>
      <text x="0" y="170" fill="#94a3b8" font-size="10">Prosa dettagliata, stile e toni</text>

      <text x="0" y="200" fill="#38bdf8" font-size="12" font-weight="700">E. Sceneggiatura</text>
      <text x="0" y="216" fill="#94a3b8" font-size="10">Formato americano/italiano</text>

      <text x="0" y="246" fill="#38bdf8" font-size="12" font-weight="700">F. Storyboard</text>
      <text x="0" y="262" fill="#94a3b8" font-size="10">Visualizzazione a fumetto</text>
    </g>
  </g>

  <!-- FASE 2: PRE-PRODUZIONE -->
  <g transform="translate(250, 95)">
    <rect width="185" height="380" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#d97706"/>
    <text x="92" y="24" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">2. PRE-PRODUZIONE</text>

    <g transform="translate(15, 55)">
      <text x="0" y="16" fill="#fbbf24" font-size="12" font-weight="700">A. Spoglio Sceneggiatura</text>
      <text x="0" y="32" fill="#94a3b8" font-size="10">Catalogazione fabbisogni</text>

      <text x="0" y="62" fill="#fbbf24" font-size="12" font-weight="700">B. Piano di Lavorazione</text>
      <text x="0" y="78" fill="#94a3b8" font-size="10">Shooting schedule per set</text>

      <text x="0" y="108" fill="#fbbf24" font-size="12" font-weight="700">C. Casting &amp; Location</text>
      <text x="0" y="124" fill="#94a3b8" font-size="10">Attori e sopralluoghi tecnici</text>

      <text x="0" y="154" fill="#fbbf24" font-size="12" font-weight="700">D. Costumi &amp; Scenografia</text>
      <text x="0" y="170" fill="#94a3b8" font-size="10">Allestimento e attrezzeria</text>

      <text x="0" y="200" fill="#fbbf24" font-size="12" font-weight="700">E. Ordine del Giorno</text>
      <text x="0" y="216" fill="#94a3b8" font-size="10">Call Sheet quotidiano troupe</text>
    </g>
  </g>

  <!-- FASE 3: PRODUZIONE (IL SET) -->
  <g transform="translate(460, 95)">
    <rect width="185" height="380" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#e11d48"/>
    <text x="92" y="24" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">3. IL SET (RIPRESE)</text>

    <g transform="translate(15, 55)">
      <text x="0" y="16" fill="#f43f5e" font-size="12" font-weight="700">A. Regia &amp; Aiuto Regista</text>
      <text x="0" y="32" fill="#94a3b8" font-size="10">Guida artistica e timing</text>

      <text x="0" y="62" fill="#f43f5e" font-size="12" font-weight="700">B. DoP &amp; Camera Crew</text>
      <text x="0" y="78" fill="#94a3b8" font-size="10">Direttore foto, operatore, 1st AC</text>

      <text x="0" y="108" fill="#f43f5e" font-size="12" font-weight="700">C. Gaffer &amp; Grip</text>
      <text x="0" y="124" fill="#94a3b8" font-size="10">Luci, stativi, dolly, crane</text>

      <text x="0" y="154" fill="#f43f5e" font-size="12" font-weight="700">D. Presa Diretta Suono</text>
      <text x="0" y="170" fill="#94a3b8" font-size="10">Fonico e microfonista (boom)</text>

      <text x="0" y="200" fill="#f43f5e" font-size="12" font-weight="700">E. Ciak &amp; Sincronia</text>
      <text x="0" y="216" fill="#94a3b8" font-size="10">Script supervisor (segretaria ed.)</text>
    </g>
  </g>

  <!-- FASE 4: POST-PRODUZIONE & WEB -->
  <g transform="translate(670, 95)">
    <rect width="185" height="380" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect width="185" height="36" rx="8" fill="#059669"/>
    <text x="92" y="24" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="700">4. POST &amp; WEB</text>

    <g transform="translate(15, 55)">
      <text x="0" y="16" fill="#10b981" font-size="12" font-weight="700">A. Montaggio Video</text>
      <text x="0" y="32" fill="#94a3b8" font-size="10">Offline cut e picture lock</text>

      <text x="0" y="62" fill="#10b981" font-size="12" font-weight="700">B. Sound Design &amp; Mix</text>
      <text x="0" y="78" fill="#94a3b8" font-size="10">Foley, dialoghi, colonna sonora</text>

      <text x="0" y="108" fill="#10b981" font-size="12" font-weight="700">C. Color Grading</text>
      <text x="0" y="124" fill="#94a3b8" font-size="10">LUT, correzione primaria/secondaria</text>

      <text x="0" y="154" fill="#10b981" font-size="12" font-weight="700">D. Compressione Codec</text>
      <text x="0" y="170" fill="#94a3b8" font-size="10">H.264, HEVC, AV1, ProRes</text>

      <text x="0" y="200" fill="#10b981" font-size="12" font-weight="700">E. Web Delivery HLS/DASH</text>
      <text x="0" y="216" fill="#94a3b8" font-size="10">Streaming adattivo e HTML5 video</text>
    </g>
  </g>
</svg>
"""

# 5. Schema Formati Video, Codec e Distribuzione Web
svg_video_web = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="auto" style="background:#0f172a; border-radius:12px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <marker id="arrowWeb" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <path d="M 1 1 L 6 3.5 L 1 6 Z" fill="#38bdf8" />
    </marker>
  </defs>

  <rect width="900" height="520" fill="#0f172a" rx="12"/>
  <rect x="2" y="2" width="896" height="516" fill="none" stroke="#334155" stroke-width="1.5" rx="10"/>

  <!-- Titolo -->
  <text x="450" y="44" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="1">ARCHITETTURA VIDEO PER IL WEB: CODEC, CONTAINER E STREAMING</text>
  <text x="450" y="68" text-anchor="middle" fill="#94a3b8" font-size="13">Dal flusso Master non compresso al protocollo adattivo per browser e dispositivi mobili</text>

  <!-- Box 1: CONTENITORE vs CODEC -->
  <g transform="translate(40, 95)">
    <rect width="395" height="185" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="395" height="34" rx="8" fill="#334155" opacity="0.6"/>
    <text x="20" y="23" fill="#38bdf8" font-size="14" font-weight="700">CONTENITORE (Wrapper) vs CODEC</text>

    <!-- Container MP4/WebM -->
    <rect x="20" y="50" width="355" height="55" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="35" y="73" fill="#38bdf8" font-size="13" font-weight="700">Contenitori (.mp4, .webm, .mov, .mkv)</text>
    <text x="35" y="93" fill="#94a3b8" font-size="11">Scatole che incapsulano flusso video, tracce audio, metadati e sottotitoli.</text>

    <!-- Codec Video & Audio -->
    <rect x="20" y="115" width="355" height="55" rx="6" fill="#0f172a" stroke="#a78bfa" stroke-width="1"/>
    <text x="35" y="138" fill="#a78bfa" font-size="13" font-weight="700">Codec Video (H.264/AVC, H.265/HEVC, VP9, AV1)</text>
    <text x="35" y="158" fill="#94a3b8" font-size="11">Algoritmi di compressione/decompressione. Codec Audio: AAC, Opus.</text>
  </g>

  <!-- Box 2: PARAMETRI TECNICI CHIAVE -->
  <g transform="translate(465, 95)">
    <rect width="395" height="185" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="395" height="34" rx="8" fill="#334155" opacity="0.6"/>
    <text x="20" y="23" fill="#fbbf24" font-size="14" font-weight="700">PARAMETRI FONDAMENTALI DEL SEGNALE</text>

    <g transform="translate(20, 50)">
      <text x="0" y="18" fill="#f8fafc" font-size="13" font-weight="600">Risoluzione &amp; Aspetto:</text>
      <text x="160" y="18" fill="#94a3b8" font-size="12">1080p (Full HD), 4K UHD | 16:9 o 9:16 (Vertical)</text>

      <text x="0" y="48" fill="#f8fafc" font-size="13" font-weight="600">Frame Rate (fps):</text>
      <text x="160" y="48" fill="#94a3b8" font-size="12">24 fps (Cinema), 25 fps (PAL), 30/60 fps (Web)</text>

      <text x="0" y="78" fill="#f8fafc" font-size="13" font-weight="600">Bitrate &amp; Rate Control:</text>
      <text x="160" y="78" fill="#94a3b8" font-size="12">CBR (Costante) vs VBR (Variabile 2-Pass)</text>

      <text x="0" y="108" fill="#f8fafc" font-size="13" font-weight="600">GOP &amp; Keyframe:</text>
      <text x="160" y="108" fill="#94a3b8" font-size="12">I-Frame (intra), P-Frame (pred.), B-Frame (bi-dir.)</text>
    </g>
  </g>

  <!-- Box 3: STREAMING ADATTIVO (HLS / MPEG-DASH) -->
  <g transform="translate(40, 295)">
    <rect width="820" height="195" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="0" y="0" width="820" height="34" rx="8" fill="#334155" opacity="0.6"/>
    <text x="20" y="23" fill="#10b981" font-size="14" font-weight="700">DISTRIBUZIONE WEB: ADAPTIVE BITRATE STREAMING (ABR)</text>

    <!-- Pipeline diagramma orizzontale -->
    <g transform="translate(25, 60)">
      <!-- Master File -->
      <rect width="135" height="105" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
      <text x="67" y="32" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="700">VIDEO MASTER</text>
      <text x="67" y="52" text-anchor="middle" fill="#94a3b8" font-size="10">ProRes 422 HQ</text>
      <text x="67" y="70" text-anchor="middle" fill="#94a3b8" font-size="10">o DNxHR</text>
      <text x="67" y="90" text-anchor="middle" fill="#38bdf8" font-size="10">High Bitrate</text>

      <!-- Arrow 1 -->
      <line x1="145" y1="52" x2="175" y2="52" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowWeb)"/>

      <!-- Transcoder Multi-Bitrate -->
      <rect x="185" y="0" width="165" height="105" rx="6" fill="#0f172a" stroke="#a78bfa" stroke-width="1.5"/>
      <text x="267" y="28" text-anchor="middle" fill="#c084fc" font-size="12" font-weight="700">TRANSCODIFICA</text>
      <text x="267" y="48" text-anchor="middle" fill="#38bdf8" font-size="10">Risoluzioni Multiple:</text>
      <text x="267" y="66" text-anchor="middle" fill="#94a3b8" font-size="10">1080p @ 6 Mbps</text>
      <text x="267" y="80" text-anchor="middle" fill="#94a3b8" font-size="10">720p @ 3 Mbps</text>
      <text x="267" y="94" text-anchor="middle" fill="#94a3b8" font-size="10">480p @ 1.2 Mbps</text>

      <!-- Arrow 2 -->
      <line x1="360" y1="52" x2="390" y2="52" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowWeb)"/>

      <!-- Segmenter / Chunks -->
      <rect x="400" y="0" width="165" height="105" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="482" y="28" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="700">SEGMENTAZIONE</text>
      <text x="482" y="50" text-anchor="middle" fill="#94a3b8" font-size="10">Segmenti .ts o .m4s</text>
      <text x="482" y="68" text-anchor="middle" fill="#94a3b8" font-size="10">Durata: 2-6 secondi</text>
      <text x="482" y="88" text-anchor="middle" fill="#f8fafc" font-size="10">Playlist .m3u8 / .mpd</text>

      <!-- Arrow 3 -->
      <line x1="575" y1="52" x2="605" y2="52" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowWeb)"/>

      <!-- Player Web / CDN -->
      <rect x="615" y="0" width="150" height="105" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="690" y="28" text-anchor="middle" fill="#34d399" font-size="12" font-weight="700">WEB CLIENT</text>
      <text x="690" y="50" text-anchor="middle" fill="#94a3b8" font-size="10">HLS.js / Video.js</text>
      <text x="690" y="68" text-anchor="middle" fill="#94a3b8" font-size="10">Switch dinamico</text>
      <text x="690" y="88" text-anchor="middle" fill="#34d399" font-size="10">Zero Buffering</text>
    </g>
  </g>
</svg>
"""

svg_files = {
    "schema_movimenti_camera.svg": svg_movimenti,
    "schema_regola_180.svg": svg_180,
    "schema_struttura_3_atti.svg": svg_tre_atti,
    "schema_fasi_produzione.svg": svg_produzione,
    "schema_video_web_streaming.svg": svg_video_web
}

for fname, content in svg_files.items():
    path = os.path.join(OUTPUT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Creato {fname} in {OUTPUT_DIR}")

print("Tutti i 5 SVG tecnici per TAW creati con successo!")
