import json, re

with open("data/stull-data.js", "r", encoding="utf-8") as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
stull = json.loads(text[start:end])

for c in stull:
    num = c.get("number")
    s = c.get("summary", "")

    # Cap 32: Tiratore Texano
    if num == 32:
        clean_texan = (
            "> **La Fallacia del Tiratore Texano**:\n"
            "> Un tiratore spara a caso sulla parete di un fienile e poi disegna il bersaglio attorno al gruppo di fori più fitto.\n"
            "> *Nel web analytics accade lo stesso*: si scandagliano milioni di log di navigazione a posteriori finché non si trova una correlazione casuale, spacciandola erroneamente per un comportamento utente intenzionale."
        )
        s = re.sub(r'```[\s\S]*?Fallacia del Tiratore Texano[\s\S]*?```', clean_texan, s)

    # Cap 34: Pantera Rosa
    if num == 34:
        clean_pink = (
            "> **L'aneddoto della Pantera Rosa**:\n"
            "> - **Ispettore Clouseau**: *«Il suo cane morde?»*\n"
            "> - **Portiere**: *«No.»*\n"
            "> *(Il cane azzanna la mano di Clouseau)*\n"
            "> - **Clouseau**: *«Aveva detto che il suo cane non mordeva!»*\n"
            "> - **Portiere**: *«Quello non è il mio cane.»*\n"
            ">\n"
            "> **Morale metodologica**: Se nelle interviste poni domande chiuse e imprecise, otterrai risposte letterali ma del tutto fuorvianti per la progettazione."
        )
        s = re.sub(r'```[\s\S]*?La battuta della Pantera Rosa[\s\S]*?```', clean_pink, s)

    # Cap 36: Continuum di Fedeltà
    if num == 36:
        clean_fidelity = (
            "> **Continuum di Fedeltà Progettuale**:\n"
            "> **1. Mappe Concettuali** *(Astratto / Bassa Fedeltà — definiscono il concetto)* →\n"
            "> **2. Mock-up Visivi** *(Media Fedeltà — definiscono l'estetica e la gerarchia)* →\n"
            "> **3. Prototipi Interattivi** *(Concreto / Alta Fedeltà — definiscono l'interazione reale)*"
        )
        s = re.sub(r'```[\s\S]*?ASTRATTO[\s\S]*?PROTOTIPI[\s\S]*?```', clean_fidelity, s)

    c["summary"] = s

output_stull = "// Dati di studio approfonditi estratti da 'UX_Design_Stull_Riassunto_esame.pdf'\n"
output_stull += "// 43 Capitoli completi con sintesi accademiche, storie-ancora, flashcard, quiz di studio e banco d'esame bilanciati.\n"
output_stull += "window.STULL_DATA = " + json.dumps(stull, indent=2, ensure_ascii=False) + ";\n"

with open("data/stull-data.js", "w", encoding="utf-8") as f:
    f.write(output_stull)

print("Capitoli 32, 34, 36 ripuliti con successo!")
