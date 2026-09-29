#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def update_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for target, repl in replacements.items():
        if target in content:
            content = content.replace(target, repl)
            print(f"Aggiornato {target[:30]} in {path}")
        else:
            print(f"NON TROVATO {target[:30]} in {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 1. Mod 2
update_file(
    "/Users/diego/Altro/Studio/scripts/build_ixd_modules/mod2_user_research.py",
    {
        "### 3. Anatomia Strutturale di una Journey Map": "![Schema Tecnico User Journey e Touchpoints](assets/corsi/dapl08/anno-1/interaction-design/images/schema_user_journey_touchpoints.svg)\n\n---\n\n### 3. Anatomia Strutturale di una Journey Map",
        "### 3. La Dimensione Attitudinale vs Comportamentale": "![Framework di Ricerca nel Design](assets/corsi/dapl08/anno-1/interaction-design/images/framework_ricerca_design.png)\n\n---\n\n### 3. La Dimensione Attitudinale vs Comportamentale"
    }
)

# 2. Mod 3
update_file(
    "/Users/diego/Altro/Studio/scripts/build_ixd_modules/mod3_teoria_sociologia.py",
    {
        "### 3. La Risoluzione dell'Equivoco: Affordance vs Signifier (Segnalatore)": "![Schema Teoria dell'Affordance Gibson vs Norman](assets/corsi/dapl08/anno-1/interaction-design/images/schema_affordance_gibson_norman.svg)\n\n---\n\n### 3. La Risoluzione dell'Equivoco: Affordance vs Signifier (Segnalatore)",
        "### 4. La Convergenza tra Prodotto, Servizio ed Esperienza Trasformativa": "![Piramide dell'Esperienza e della Trasformazione](assets/corsi/dapl08/anno-1/interaction-design/images/schema_piramide_esperienza_trasformazione.svg)\n\n---\n\n### 4. La Convergenza tra Prodotto, Servizio ed Esperienza Trasformativa",
        "### 4. Lo Spazio Sociale e la Mappatura delle Pratiche": "![Spazio Sociale e Stili di Vita secondo Pierre Bourdieu](assets/corsi/dapl08/anno-1/interaction-design/images/schema_stili_di_vita_bourdieu.svg)\n\n---\n\n### 4. Lo Spazio Sociale e la Mappatura delle Pratiche"
    }
)

# 3. Mod 4
update_file(
    "/Users/diego/Altro/Studio/scripts/build_ixd_modules/mod4_strumenti_prototipazione.py",
    {
        "### 3. La Tassonomia degli Obiettivi della Persona (Goals)": "![Template Strutturale delle Personas di Alan Cooper](assets/corsi/dapl08/anno-1/interaction-design/images/schema_personas_cooper_template.svg)\n\n---\n\n### 3. La Tassonomia degli Obiettivi della Persona (Goals)"
    }
)

print("Aggiornamenti immagini markdown completati.")
