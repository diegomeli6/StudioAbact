/**
 * Registro centrale delle materie con contenuti di studio.
 * Unica fonte di verità per: titolo, docente, corso/anno, moduli (tab), file dati,
 * prefisso degli ID capitolo (usato dalla home per il calcolo del progresso).
 *
 * Per aggiungere una materia: vedi AGENTS.md, sezione "Aggiungere una materia".
 *
 * Campi di ogni materia:
 *   title        Nome ufficiale mostrato nell'header
 *   docente      Nome del docente (senza il prefisso "Docente: ")
 *   course, anno Codice corso (chiave di ABA_DATA.PIANI_STUDIO) e anno, per il tasto Indietro
 *   examLabel    Etichetta della sorgente nel simulatore d'esame (scope "Misto completo")
 *   idPrefixes   Prefissi degli ID capitolo; servono alla home per contare i completati
 *   modules      Tab del selettore: key (univoca), tab (etichetta breve), label (nome esteso),
 *                source (variabile globale window.X del file dati), module (filtro su chapter.module, opzionale)
 *   extraScopes  Ambiti aggiuntivi del simulatore: { value, label, filter(chapter) }
 */
(function (window) {
  'use strict';

  const SUBJECTS = {
    'storia-arte-1': {
      title: "Storia dell'Arte Contemporanea 1",
      docente: 'Prof.ssa Ambra Stazzone',
      course: 'DAPL08',
      anno: 1,
      examLabel: "Storia dell'Arte Contemporanea 1",
      idPrefixes: ['arte1-'],
      modules: [
        { key: 'arte1-anni50', tab: "1. Anni '50", label: "1. Anni '50 — L'Informale e il Dopoguerra", source: 'ARTE1_DATA', module: 'anni50' },
        { key: 'arte1-anni60', tab: "2. Anni '60", label: "2. Anni '60 — Dalla Pop Art all'Arte Povera", source: 'ARTE1_DATA', module: 'anni60' },
        { key: 'arte1-anni70', tab: "3. Anni '70", label: "3. Anni '70 — Smaterializzazione, Spazio e Corpo", source: 'ARTE1_DATA', module: 'anni70' },
        { key: 'arte1-monografie', tab: '4. Monografie', label: '4. Monografie — Magritte, Man Ray, Warhol', source: 'ARTE1_DATA', module: 'monografie' }
      ]
    },

    'fotografia': {
      title: 'Fotografia Digitale',
      docente: 'Prof. Carmelo Bongiorno',
      course: 'DAPL08',
      anno: 1,
      examLabel: 'Fotografia Digitale',
      idPrefixes: ['foto-'],
      modules: [
        { key: 'foto-tecnica', tab: '1. Tecnica & Grammatica', label: '1. Tecnica & Grammatica', source: 'FOTOGRAFIA_DATA', module: 'foto-tecnica' },
        { key: 'foto-teoria', tab: '2. Teoria & Inconscio', label: '2. Teoria & Inconscio', source: 'FOTOGRAFIA_DATA', module: 'foto-teoria' },
        { key: 'foto-autori', tab: '3. I 15 Autori', label: '3. I 15 Autori Contemporanei', source: 'FOTOGRAFIA_DATA', module: 'foto-autori' },
        { key: 'foto-maestri', tab: '4. I Grandi Maestri', label: '4. I Grandi Maestri Storici', source: 'FOTOGRAFIA_DATA', module: 'foto-maestri' }
      ]
    },

    'taw': {
      title: 'Tecniche Audiovisive per il Web',
      docente: 'Prof. Lorenzo Di Silvestro',
      course: 'DAPL08',
      anno: 1,
      examLabel: 'Tecniche Audiovisive per il Web',
      idPrefixes: ['taw-'],
      modules: [
        { key: 'taw-camera-linguaggio', tab: '1. Fotocamera & Linguaggio', label: '1. Fotocamera & Linguaggio', source: 'TAW_DATA', module: 'taw-camera-linguaggio' },
        { key: 'taw-movimenti-montaggio', tab: '2. Dinamica & Montaggio', label: '2. Dinamica & Montaggio', source: 'TAW_DATA', module: 'taw-movimenti-montaggio' },
        { key: 'taw-drammaturgia-produzione', tab: '3. Sceneggiatura & Produzione', label: '3. Sceneggiatura & Produzione', source: 'TAW_DATA', module: 'taw-drammaturgia-produzione' },
        { key: 'taw-post-web', tab: '4. Post-Produzione & Web', label: '4. Post-Produzione & Web', source: 'TAW_DATA', module: 'taw-post-web' }
      ]
    },

    'interaction': {
      title: 'Interaction Design',
      docente: 'Prof. Giulio Interlandi',
      course: 'DAPL08',
      anno: 1,
      examLabel: 'Interaction Design',
      idPrefixes: ['ixd-'],
      modules: [
        { key: 'ixd-fondamenti-design-thinking', tab: '1. Fondamenti & Design Thinking', label: '1. Fondamenti & Design Thinking', source: 'INTERACTION_DATA', module: 'ixd-fondamenti-design-thinking' },
        { key: 'ixd-user-research', tab: '2. Metodologie & User Research', label: '2. Metodologie & User Research', source: 'INTERACTION_DATA', module: 'ixd-user-research' },
        { key: 'ixd-teoria-sociologia', tab: '3. Esperienza & Sociologia', label: '3. Esperienza & Sociologia', source: 'INTERACTION_DATA', module: 'ixd-teoria-sociologia' },
        { key: 'ixd-strumenti-prototipazione', tab: '4. Prototipazione & Strumenti', label: '4. Prototipazione & Strumenti', source: 'INTERACTION_DATA', module: 'ixd-strumenti-prototipazione' }
      ]
    },

    'storia-arte': {
      title: "Storia dell'Arte Contemporanea 2",
      docente: 'Prof.ssa Ambra Stazzone',
      course: 'DAPL08',
      anno: 2,
      examLabel: "Storia dell'Arte Contemporanea 2",
      idPrefixes: ['arte-'],
      modules: [
        { key: 'arte-anni80', tab: "1. Anni '80", label: "1. Movimenti Anni '80", source: 'ARTE_DATA', module: 'anni80' },
        { key: 'arte-anni90', tab: "2. Anni '90", label: "2. Movimenti Anni '90", source: 'ARTE_DATA', module: 'anni90' },
        { key: 'arte-duemila', tab: '3. Duemila', label: '3. Anni Duemila', source: 'ARTE_DATA', module: 'duemila' },
        { key: 'arte-monografie', tab: '4. Monografie', label: '4. Monografie & Linguaggi Contemporanei', source: 'ARTE_DATA', module: 'monografie' }
      ]
    },

    'archetipi': {
      title: "Archetipi dell'immaginario",
      docente: 'Prof. Stefano Puglisi',
      course: 'DAPL08',
      anno: 2,
      examLabel: "Archetipi dell'immaginario",
      idPrefixes: ['archetipi-'],
      modules: [
        { key: 'archetipi-ecologica', tab: '1. Dimensione Ecologica', label: '1. Verso una Dimensione Ecologica', source: 'ARCHETIPI_DATA', module: 'archetipi-ecologica' },
        { key: 'archetipi-jung', tab: '2. Inconscio Collettivo', label: '2. Inconscio Collettivo & Archetipi', source: 'ARCHETIPI_DATA', module: 'archetipi-jung' },
        { key: 'archetipi-simbologia', tab: '3. Simbologia & Epigenetica', label: '3. Linguaggi Simbolici & Epigenetica', source: 'ARCHETIPI_DATA', module: 'archetipi-simbologia' }
      ]
    },

    'ux-webdesign': {
      title: 'Web Design',
      docente: 'Prof. Ciro Esposito',
      course: 'DAPL08',
      anno: 2,
      examLabel: 'Web Design',
      idPrefixes: ['dispense-', 'krug-', 'stull-', 'maeda-'],
      modules: [
        { key: 'dispense', tab: '1. Dispense', label: '1. Dispense Professore', source: 'DISPENSE_DATA' },
        { key: 'krug', tab: '2. Krug', label: "2. Steve Krug — Don't Make Me Think", source: 'KRUG_DATA' },
        { key: 'stull', tab: '3. Stull (UX)', label: '3. Edward Stull — UX Design', source: 'STULL_DATA' },
        { key: 'maeda', tab: '4. Maeda', label: '4. John Maeda — Le leggi della semplicità', source: 'MAEDA_DATA' }
      ],
      extraScopes: [
        {
          value: 'codice',
          label: 'Solo Codice Progetto Esame (HTML & CSS)',
          modules: ['dispense'],
          filter: c => c.number >= 11 && c.number <= 14
        }
      ]
    }
  };

  // Accetta sia un array di capitoli sia un oggetto { chapters: [...] }
  function toChapters(value) {
    if (Array.isArray(value)) return value;
    if (value && Array.isArray(value.chapters)) return value.chapters;
    return [];
  }

  function getModuleChapters(mod) {
    const all = toChapters(window[mod.source]);
    return mod.module ? all.filter(c => c.module === mod.module) : all;
  }

  window.SUBJECTS = SUBJECTS;
  window.SubjectRegistry = { SUBJECTS, toChapters, getModuleChapters };
})(window);
