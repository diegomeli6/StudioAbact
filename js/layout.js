/**
 * Layout condiviso delle pagine di studio.
 * Genera tutto il markup della pagina (header, sidebar, subtab, lettore vocale,
 * simulatore d'esame, navigazione mobile) a partire da window.SUBJECTS.
 *
 * La pagina deve avere <body data-subject="{id}" data-course="{CODICE}"> e caricare,
 * in quest'ordine: auth.js, file dati, subjects.js, layout.js, core.js, subject-app.js.
 * Lo script gira in modo sincrono a fine <body>, prima di DOMContentLoaded.
 *
 * Gli ID e le classi qui sotto sono il contratto con core.js e auth.js (vedi AGENTS.md).
 */
(function (window, document) {
  'use strict';

  const subjectId = document.body.dataset.subject;
  const subject = (window.SUBJECTS || {})[subjectId];
  if (!subject) {
    document.body.innerHTML = '<p style="padding:24px">Materia non configurata: ' + subjectId + '</p>';
    return;
  }

  const esc = s => String(s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  const hubHref = `../corsi.html?view=materie&course=${encodeURIComponent(subject.course)}&anno=${subject.anno}`;

  // Icone SVG (stroke = currentColor)
  const svg = (w, body, sw = 2, fill = 'none') =>
    `<svg width="${w}" height="${w}" viewBox="0 0 24 24" fill="${fill}" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
  const I = {
    back: svg(20, '<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>', 2.2),
    study: svg(14, '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'),
    exam: svg(14, '<circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/>'),
    examLg: svg(20, '<circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/>'),
    moon: svg(16, '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>'),
    sun: svg(16, '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>'),
    collapse: svg(18, '<line x1="19" y1="5" x2="19" y2="19"/><polyline points="9 7 4 12 9 17"/><line x1="4" y1="12" x2="19" y2="12"/>', 2.2),
    expand: svg(18, '<line x1="5" y1="5" x2="5" y2="19"/><polyline points="15 7 20 12 15 17"/><line x1="5" y1="12" x2="20" y2="12"/>', 2.2),
    close16: svg(16, '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>', 2.2),
    close18: svg(18, '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>'),
    prev: svg(14, '<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>', 2.5),
    next: svg(14, '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 2.5),
    circle: svg(14, '<circle cx="12" cy="12" r="10"/>'),
    doc: svg(14, '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>'),
    card: svg(14, '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M12 4v16"/>'),
    quiz: svg(14, '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
    play: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>',
    pause: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>',
    stop: '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><rect x="4" y="4" width="16" height="16" rx="2"/></svg>',
    anchor: svg(15, '<circle cx="12" cy="5" r="3"/><line x1="12" y1="22" x2="12" y2="8"/><path d="M5 12H2a10 10 0 0 0 20 0h-3"/>', 2.2),
    pin: svg(16, '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'),
    mic: svg(16, '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/>'),
    chevron: svg(15, '<polyline points="6 9 12 15 18 9"/>', 2.2),
    list: svg(20, '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>'),
    book20: svg(20, '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>'),
    cards: svg(16, '<rect x="3" y="6" width="14" height="14" rx="2"/><path d="M7 2h12a2 2 0 0 1 2 2v12"/>'),
    stats: svg(16, '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>'),
    target: svg(16, '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'),
    book18: svg(18, '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>')
  };

  // Logo di Studio ABA Catania (fonte: assets/logo.svg; inchiostro = currentColor, si adatta al tema)
  const SITE_LOGO = '<svg class="site-logo" viewBox="36 22 340 348" role="img" aria-label="Studio ABA Catania" xmlns="http://www.w3.org/2000/svg"><g transform="translate(0 12)"><path d="M70,250 Q140,232 210,246 T340,238" stroke="#FEB940" stroke-width="58" fill="none" stroke-linecap="round" opacity="0.9"/><path d="M199.1,49.4Q202.2,66.7 200.9,74.9Q199.6,83.1 199.0,92.2Q198.3,101.3 199.7,109.7Q201.0,118.1 201.2,119.1L201.3,120.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M236.9,111.2Q218.2,113.0 209.4,115.8Q200.6,118.6 199.6,118.9L198.6,119.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M162.6,112.8Q181.6,113.8 191.1,114.9Q200.6,116.0 201.7,116.2L202.7,116.3" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M304.5,92.7Q293.3,104.3 287.2,110.6Q281.2,116.9 276.8,124.4Q272.4,131.9 265.1,135.9Q257.7,140.0 256.8,140.5L255.9,141.0" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M287.8,163.8Q272.3,153.6 265.3,147.6Q258.2,141.5 257.4,140.8L256.7,140.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M236.9,111.0Q247.8,127.3 253.2,134.2Q258.6,141.1 259.2,141.9L259.9,142.7" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M350.3,199.1Q333.5,198.2 324.7,197.7Q315.8,197.3 307.9,197.4Q300.0,197.6 291.2,199.0Q282.5,200.5 281.4,200.7L280.4,200.9" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M290.1,236.2Q286.5,218.3 283.9,209.6Q281.4,200.8 281.1,199.8L280.8,198.8" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M288.2,162.7Q284.9,182.0 283.8,191.1Q282.6,200.1 282.4,201.2L282.3,202.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M305.8,305.9Q293.7,295.5 288.5,288.1Q283.3,280.8 276.1,275.9Q268.9,271.1 263.5,265.1Q258.1,259.1 257.4,258.4L256.7,257.6" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M238.1,289.0Q246.6,272.6 252.3,265.1Q258.0,257.7 258.7,256.9L259.3,256.0" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M288.6,235.5Q273.0,248.6 266.3,253.8Q259.6,258.9 258.8,259.6L258.0,260.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M198.1,349.9Q202.8,333.6 201.6,325.2Q200.4,316.8 199.4,308.3Q198.4,299.9 198.9,290.9Q199.3,281.9 199.4,280.9L199.4,279.8" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M162.9,287.3Q182.0,283.2 191.0,283.1Q199.9,283.0 201.0,283.0L202.0,283.0" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M236.2,287.5Q218.3,282.6 209.2,282.8Q200.2,283.0 199.2,283.0L198.1,283.1" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M93.5,305.9Q106.0,293.4 111.7,287.8Q117.5,282.2 123.5,276.7Q129.5,271.2 135.5,265.2Q141.4,259.2 142.2,258.5L142.9,257.7" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M110.8,236.3Q127.3,247.1 134.7,252.8Q142.0,258.5 142.8,259.2L143.7,259.8" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M164.3,287.9Q150.9,274.1 146.3,266.2Q141.7,258.3 141.1,257.4L140.6,256.5" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M50.4,198.5Q66.5,198.9 74.9,200.6Q83.3,202.3 92.2,201.6Q101.0,201.0 109.5,200.6Q117.9,200.2 119.0,200.2L120.0,200.1" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M110.7,162.8Q114.2,181.4 115.9,190.7Q117.5,199.9 117.7,200.9L117.9,202.0" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M111.9,236.7Q113.2,218.4 114.6,208.8Q116.1,199.2 116.2,198.2L116.4,197.1" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M92.9,94.5Q105.0,106.6 111.4,111.8Q117.7,116.9 123.5,122.9Q129.3,129.0 134.7,135.8Q140.2,142.6 140.9,143.5L141.5,144.3" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M164.5,111.1Q155.1,127.4 147.6,134.3Q140.0,141.2 139.3,141.9L138.5,142.6" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M111.0,162.3Q126.3,153.9 134.1,148.3Q141.8,142.7 142.7,142.1L143.5,141.5" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M198.6,200.5Q199.9,183.1 200.0,175.1Q200.1,167.1 199.3,158.9Q198.4,150.7 200.3,142.1Q202.2,133.5 200.9,125.3Q199.6,117.1 199.4,116.1L199.3,115.1" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M201.8,201.0Q212.5,189.0 218.4,183.3Q224.4,177.7 230.1,171.9Q235.8,166.1 242.0,160.3Q248.3,154.5 253.9,148.5Q259.5,142.6 260.2,141.8L260.9,141.1" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M199.3,198.8Q216.9,201.1 225.2,201.2Q233.4,201.2 241.3,199.0Q249.2,196.8 257.7,197.7Q266.2,198.6 274.0,199.5Q281.8,200.5 282.8,200.6L283.9,200.7" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M199.6,200.0Q209.6,212.7 216.8,218.2Q224.0,223.7 229.1,229.4Q234.2,235.1 240.8,240.6Q247.5,246.1 253.2,252.3Q258.8,258.5 259.5,259.3L260.2,260.1" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M199.2,199.4Q198.7,216.5 198.6,224.7Q198.6,232.9 199.8,241.1Q201.1,249.2 201.6,258.0Q202.2,266.8 201.6,274.7Q201.0,282.7 201.0,283.7L200.9,284.7" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.5,200.7Q188.3,211.8 183.1,218.1Q177.8,224.4 171.5,230.3Q165.2,236.2 159.2,241.6Q153.3,247.0 147.6,252.9Q142.0,258.8 141.3,259.5L140.6,260.3" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.0,201.4Q184.0,199.2 175.1,199.8Q166.2,200.5 158.2,201.2Q150.2,202.0 142.3,199.9Q134.4,197.9 126.2,199.5Q118.0,201.2 117.0,201.4L116.0,201.6" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M199.2,200.9Q189.6,186.4 183.1,181.9Q176.6,177.3 170.6,171.3Q164.5,165.3 159.6,158.5Q154.8,151.8 148.1,146.1Q141.3,140.5 140.5,139.8L139.7,139.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M201.1,199.9Q208.0,184.2 210.2,176.1Q212.5,167.9 216.5,159.6Q220.6,151.2 221.0,150.3L221.5,149.3" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.1,198.6Q217.7,195.8 225.8,192.3Q233.9,188.7 241.1,183.7Q248.3,178.6 249.2,178.0L250.0,177.4" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.1,200.6Q215.9,207.3 224.9,209.4Q233.9,211.5 241.2,215.9Q248.6,220.4 249.5,220.9L250.4,221.5" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.3,200.4Q208.2,216.0 211.1,224.0Q214.0,232.1 217.1,240.5Q220.2,248.9 220.6,249.9L221.0,250.9" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M199.2,199.6Q194.2,216.6 191.1,224.7Q188.0,232.7 184.5,240.9Q180.9,249.1 180.5,250.1L180.0,251.0" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M199.3,199.4Q183.2,206.4 175.3,209.7Q167.3,213.1 158.8,216.7Q150.3,220.4 149.3,220.8L148.4,221.2" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.3,198.3Q182.2,195.5 174.6,191.7Q166.9,187.8 158.8,184.6Q150.6,181.3 149.7,180.9L148.7,180.5" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.4,200.8Q191.4,185.2 189.3,176.1Q187.1,167.1 183.6,159.1Q180.0,151.2 179.6,150.2L179.2,149.3" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linecap="round"/><path d="M200.7,116.5Q208.5,136.4 214.0,143.1Q219.6,149.8 228.8,147.5Q238.1,145.2 248.7,143.7Q259.2,142.2 256.5,151.4Q253.8,160.7 251.8,169.4Q249.8,178.1 258.5,183.1Q267.2,188.2 274.9,193.6Q282.5,199.1 274.1,204.9Q265.8,210.8 256.9,215.4Q248.1,220.1 251.9,229.3Q255.8,238.5 256.7,248.9Q257.6,259.3 248.4,256.7Q239.2,254.1 229.1,250.8Q219.0,247.6 214.7,256.9Q210.5,266.3 205.1,274.1Q199.7,281.9 195.4,273.5Q191.2,265.2 185.7,256.3Q180.2,247.4 170.6,251.4Q161.1,255.4 151.4,256.7Q141.7,258.0 143.7,248.9Q145.7,239.7 148.5,229.7Q151.2,219.6 142.7,214.7Q134.2,209.8 125.6,204.9Q117.1,200.0 125.5,194.4Q133.9,188.8 142.8,184.3Q151.7,179.8 150.2,169.9Q148.6,160.1 145.1,151.2Q141.6,142.4 150.9,143.8Q160.2,145.3 169.2,148.0Q178.2,150.7 184.8,142.9Q191.4,135.1 195.6,126.3L199.9,117.6Z" fill="none" stroke="currentColor" stroke-width="7.2" stroke-linejoin="round"/><path d="M199.9,50.1Q208.6,61.3 212.0,67.9Q215.5,74.6 217.5,81.2Q219.5,87.8 224.6,92.7Q229.7,97.6 233.1,104.6Q236.4,111.5 244.3,111.3Q252.2,111.1 258.1,107.6Q264.0,104.1 271.3,101.4Q278.5,98.8 285.4,98.4Q292.2,98.0 299.0,95.7Q305.9,93.4 305.0,100.8Q304.2,108.2 300.6,114.4Q297.0,120.5 296.4,127.9Q295.7,135.2 293.4,141.8Q291.0,148.4 290.0,154.9Q288.9,161.4 294.4,167.0Q300.0,172.7 307.4,173.7Q314.8,174.7 319.5,180.7Q324.1,186.7 331.2,189.4Q338.2,192.2 344.7,196.5Q351.3,200.7 345.6,205.5Q339.8,210.3 332.5,212.3Q325.1,214.2 319.0,217.7Q312.9,221.2 306.5,224.6Q300.1,228.0 294.5,232.4Q289.0,236.8 290.4,244.0Q291.9,251.2 292.2,258.6Q292.5,266.0 294.7,272.2Q297.0,278.3 299.3,285.5Q301.6,292.7 304.5,298.7Q307.4,304.7 299.5,303.2Q291.6,301.7 285.0,299.6Q278.4,297.5 271.0,297.3Q263.6,297.2 256.5,296.1Q249.3,295.1 243.1,292.3Q236.8,289.4 234.1,295.4Q231.5,301.4 226.4,306.6Q221.3,311.8 218.6,318.8Q216.0,325.8 211.4,331.6Q206.9,337.3 204.6,343.2Q202.3,349.2 197.6,343.6Q192.8,338.0 189.6,331.9Q186.4,325.7 181.7,319.9Q176.9,314.0 172.9,308.0Q168.9,302.0 165.9,295.8Q162.9,289.6 156.2,290.8Q149.4,292.1 141.7,292.7Q134.1,293.3 127.6,295.3Q121.2,297.2 114.5,298.6Q107.7,300.0 101.7,302.9Q95.6,305.8 97.7,299.0Q99.9,292.2 102.0,285.6Q104.1,279.0 104.4,271.8Q104.7,264.6 105.1,257.1Q105.6,249.7 108.0,243.7Q110.4,237.6 103.8,234.5Q97.2,231.4 91.4,227.3Q85.5,223.1 79.9,218.7Q74.2,214.4 68.6,210.1Q63.0,205.8 56.3,202.2Q49.6,198.5 55.2,194.5Q60.8,190.4 66.8,187.0Q72.8,183.6 79.9,181.3Q87.0,179.1 92.5,173.7Q98.0,168.4 105.3,165.9Q112.5,163.4 110.5,156.8Q108.4,150.3 105.2,143.6Q101.9,136.8 101.8,129.3Q101.6,121.8 99.2,114.6Q96.7,107.4 95.8,99.9Q94.8,92.4 101.5,96.0Q108.1,99.6 114.6,100.7Q121.0,101.8 128.8,102.7Q136.5,103.7 143.4,104.7Q150.2,105.6 157.4,108.9Q164.6,112.1 166.6,105.0Q168.7,97.9 174.9,93.5Q181.0,89.2 183.0,82.0Q185.0,74.7 189.9,69.4Q194.8,64.1 196.5,56.5L198.1,48.9Z" fill="none" stroke="currentColor" stroke-width="11.9" stroke-linejoin="round" stroke-linecap="round"/><g transform="translate(0 0) rotate(-16 200 52)"><path d="M167.7,51.9Q169.0,62.4 168.5,67.0Q168.0,71.5 171.7,73.8Q175.5,76.0 179.9,77.2Q184.3,78.4 188.1,79.7Q191.9,81.0 196.1,81.3Q200.4,81.6 204.2,81.3Q207.9,81.0 212.2,80.3Q216.4,79.7 220.5,78.0Q224.6,76.4 228.3,74.1Q231.9,71.8 232.4,66.7Q233.0,61.6 232.6,57.0Q232.2,52.3 224.2,52.1Q216.3,52.0 208.2,52.0Q200.1,52.1 192.2,52.4Q184.3,52.8 176.0,52.3L167.7,51.8Z" style="fill:var(--logo-paper,#fff)"/><path d="M200.0,16.1Q214.6,21.3 221.7,24.6Q228.8,28.0 235.8,30.7Q242.9,33.3 250.4,35.4Q257.9,37.5 265.0,41.0Q272.2,44.5 264.9,47.3Q257.6,50.2 250.4,52.5Q243.2,54.9 236.1,57.7Q229.0,60.6 221.8,63.8Q214.6,67.0 207.4,69.2Q200.1,71.4 192.8,69.0Q185.4,66.6 178.3,64.2Q171.2,61.7 163.7,59.1Q156.3,56.4 149.4,52.5Q142.5,48.6 135.3,45.9Q128.0,43.1 135.1,40.3Q142.1,37.5 149.4,35.2Q156.8,32.9 164.1,30.6Q171.5,28.3 178.6,25.2Q185.7,22.1 192.6,18.8L199.6,15.5Z" style="fill:var(--logo-paper,#fff)"/><path d="M166.7,51.5Q166.3,62.2 167.5,67.2Q168.8,72.2 172.6,74.2Q176.4,76.3 180.4,78.4Q184.4,80.6 188.2,80.5Q192.0,80.4 196.3,80.9Q200.6,81.5 204.6,81.5Q208.6,81.5 212.3,80.4Q216.0,79.4 220.3,77.7Q224.7,76.1 228.8,74.2Q233.0,72.4 232.6,67.3Q232.2,62.3 231.7,57.3Q231.3,52.3 223.3,53.4Q215.4,54.4 208.1,53.4Q200.8,52.3 192.5,52.6Q184.3,53.0 175.8,53.3L167.3,53.7Z" fill="none" stroke="currentColor" stroke-width="8.92" stroke-linejoin="round" stroke-linecap="round"/><path d="M200.0,15.7Q215.8,19.1 222.9,22.1Q229.9,25.0 235.9,29.6Q241.9,34.3 249.3,37.5Q256.7,40.8 264.3,42.1Q271.9,43.4 264.4,45.8Q257.0,48.2 249.5,51.3Q242.0,54.4 234.9,57.0Q227.7,59.6 220.8,62.4Q213.9,65.2 206.8,69.6Q199.8,74.1 193.0,69.8Q186.3,65.5 179.1,62.4Q172.0,59.3 164.6,56.5Q157.1,53.7 149.3,52.3Q141.5,50.9 135.3,47.7Q129.0,44.5 136.4,42.7Q143.9,40.9 150.4,37.5Q156.9,34.0 163.8,29.8Q170.7,25.6 178.4,24.3Q186.0,22.9 193.0,19.2L200.1,15.4Z" fill="none" stroke="currentColor" stroke-width="8.92" stroke-linejoin="round" stroke-linecap="round"/><path d="M200.0,44.5Q216.0,44.1 223.4,45.0Q230.7,45.8 238.8,46.1Q246.8,46.3 254.2,47.4Q261.6,48.5 261.8,57.4Q262.0,66.4 262.8,75.0L263.6,83.6" fill="none" stroke="currentColor" stroke-width="8.46" stroke-linecap="round" stroke-linejoin="round"/><path d="M255.7,82.3Q263.7,83.6 267.8,82.7Q271.8,81.8 271.9,87.8Q272.0,93.8 272.9,100.1Q273.8,106.4 268.8,106.1Q263.7,105.7 258.6,106.0Q253.4,106.3 254.0,100.2Q254.6,94.1 255.7,88.1L256.8,82.0Z" fill="currentColor" stroke="currentColor" stroke-width="5.58" stroke-linejoin="round"/><circle cx="200" cy="44" r="5" fill="currentColor" stroke="currentColor" stroke-width="4.68"/></g></g></svg>';

  const tabsHtml = subject.modules.map((m, i) => `
            <button class="pdf-tab${i === 0 ? ' active' : ''}" data-pdf="${esc(m.key)}" id="tab-${esc(m.key)}">
              <span class="tab-indicator"></span>
              <span class="tab-title">${esc(m.tab)}</span>
              <span class="tab-progress-mini" id="prog-mini-${esc(m.key)}">0/0</span>
            </button>`).join('');

  const scopeOptions = [
    '<option value="current">Solo il modulo attivo</option>',
    ...(subject.extraScopes || []).map(s => `<option value="${esc(s.value)}">${esc(s.label)}</option>`),
    '<option value="all">Misto completo (tutti i moduli)</option>'
  ].join('');

  const navBar = (extraClass, withIds) => `
          <div class="chapter-nav-bar ${extraClass}">
            <button ${withIds ? 'id="btn-prev-chap" ' : ''}class="nav-btn btn-prev-chap" type="button" aria-label="Capitolo precedente" title="Capitolo precedente">
              ${I.prev}
              <span class="nav-btn-label-full">Precedente</span>
              <span class="nav-btn-label-short">Prec</span>
            </button>
            <div class="complete-action">
              <button ${withIds ? 'id="btn-toggle-complete" ' : ''}class="btn-complete btn-toggle-complete" type="button" aria-label="Segna capitolo come completato" title="Segna come completato">
                <span class="complete-icon">${I.circle}</span>
                <span class="complete-text">Segna come completato</span>
              </button>
            </div>
            <button ${withIds ? 'id="btn-next-chap" ' : ''}class="nav-btn btn-next-chap" type="button" aria-label="Capitolo successivo" title="Capitolo successivo">
              <span class="nav-btn-label-full">Successivo</span>
              <span class="nav-btn-label-short">Succ</span>
              ${I.next}
            </button>
          </div>`;

  const html = `
  <div id="app" class="app-container">
    <div class="study-sticky-header">
      <header class="top-header">
        <div class="header-brand">
          <button id="btn-hub-nav" class="btn-back-nav" title="Torna alle materie" aria-label="Torna alle materie" data-href="${esc(hubHref)}">
            ${I.back}
          </button>
          <div class="brand-titles-group">
            <h1 class="brand-title" id="brand-main-title">${esc(subject.title)}</h1>
            <span class="brand-docente-badge">Docente: ${esc(subject.docente)}</span>
          </div>
        </div>

        <nav class="pdf-selector" id="pdf-selector-nav" aria-label="Selezione modulo di studio">
          <div class="subject-tabs-group">${tabsHtml}
          </div>
        </nav>

        <div class="header-actions">
          <div class="view-mode-pills" id="header-view-pills" role="tablist">
            <button class="pill-btn active" data-view="study" id="pill-study" title="Studio guidato">${I.study} Studio</button>
            <button class="pill-btn" data-view="exam" id="pill-exam" title="Test, ripasso, orale e progressi">${I.target} Allenati</button>
          </div>
          <div class="utility-btns">
            <button id="btn-theme-toggle" class="icon-btn" title="Cambia tema chiaro/scuro" aria-label="Cambia tema"><span class="theme-icon-moon">${I.moon}</span><span class="theme-icon-sun">${I.sun}</span></button>
          </div>
        </div>
      </header>

      <div class="session-bar" id="session-bar">
        <div class="session-info">
          <span id="active-pdf-name">${esc(subject.modules[0].label)}</span>
        </div>
        <div class="session-progress">
          <span id="active-pdf-progress-text">Progresso: 0%</span>
          <span class="session-progress-track"><span class="session-progress-fill" id="session-progress-fill"></span></span>
        </div>
      </div>
    </div>

    <div class="main-layout" id="main-layout">
      <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
          <div class="sidebar-header-left">
            <h2 class="sidebar-title">Indice dei Capitoli</h2>
            <span class="sidebar-stats" id="sidebar-stats-count">0/0</span>
          </div>
          <div class="sidebar-header-right">
            <button class="sidebar-toggle-twitch" id="btn-sidebar-collapse" type="button" title="Comprimi barra laterale" aria-label="Comprimi barra laterale">${I.collapse}</button>
            <button class="sidebar-mobile-close" id="btn-sidebar-close" type="button" aria-label="Chiudi indice">${I.close16}</button>
          </div>
        </div>
        <div class="progress-track" title="Progresso complessivo">
          <div class="progress-fill" id="sidebar-progress-fill" style="width: 0%;"></div>
        </div>
        <div class="chapter-list-container" id="chapter-list"></div>
      </aside>

      <button class="sidebar-expand-twitch" id="btn-sidebar-expand" type="button" title="Espandi barra laterale" aria-label="Espandi barra laterale">${I.expand}</button>

      <main class="content-area" id="content-area">
        <section id="view-study" class="view-panel active">
          <div class="chapter-hero">
            <div class="hero-meta">
              <span class="hero-part-badge" id="chap-part-badge" style="display: none;"></span>
              <span class="hero-number" id="chap-number">Capitolo 1</span>
              <span class="hero-time" id="chap-read-time"></span>
            </div>
            <h2 class="hero-title" id="chap-title">Caricamento...</h2>
            <p class="hero-subtitle" id="chap-subtitle"></p>
          </div>
${navBar('chapter-nav-top', false)}

          <div class="chapter-subtabs">
            <button class="subtab-btn active" data-subtab="summary">
              ${I.doc}
              <span class="subtab-label-full">Sintesi &amp; Concetti</span>
              <span class="subtab-label-short">Sintesi</span>
            </button>
            <button class="subtab-btn" data-subtab="flashcards">
              ${I.card}
              Flashcard (<span id="count-fc">0</span>)
            </button>
            <button class="subtab-btn" data-subtab="quiz">
              ${I.quiz}
              <span class="subtab-label-full">Quiz con Spiegazione</span>
              <span class="subtab-label-short">Quiz</span>
            </button>
          </div>

          <div id="subtab-panel-summary" class="subtab-panel active">
            <div class="summary-audio-bar" id="summary-audio-bar">
              <div class="audio-controls-left">
                <button id="btn-audio-listen" class="btn-audio-player" type="button" aria-label="Ascolta la sintesi del capitolo" title="Ascolta sintesi vocale">
                  <span class="audio-icon" id="audio-icon-play">${I.play}</span>
                  <span class="audio-icon" id="audio-icon-pause" style="display: none;">${I.pause}</span>
                  <span id="audio-btn-label">Ascolta Sintesi</span>
                </button>
                <button id="btn-audio-stop" class="btn-audio-stop" type="button" style="display: none;" title="Ferma la lettura vocale">
                  ${I.stop}
                  <span>Stop</span>
                </button>
                <div class="audio-speed-pills" id="audio-speed-pills" role="radiogroup" aria-label="Velocità di riproduzione">
                  <button type="button" class="speed-pill active" data-speed="1" title="Velocità normale (1x)">1x</button>
                  <button type="button" class="speed-pill" data-speed="1.25" title="Velocità accelerata (1.25x)">1.25x</button>
                </div>
              </div>
              <div class="audio-status-wrap">
                <div class="audio-visualizer" id="audio-visualizer" style="display: none;">
                  <span class="visualizer-bar bar-1"></span>
                  <span class="visualizer-bar bar-2"></span>
                  <span class="visualizer-bar bar-3"></span>
                </div>
                <span class="audio-status-label" id="audio-status-label">Lettore vocale pronto</span>
              </div>
            </div>

            <div id="anchor-story-box" class="story-anchor-box" style="display: none;">
              <div class="story-anchor-header">
                <div class="story-anchor-badge-row">
                  <span class="story-icon">${I.anchor}</span>
                  <span class="story-anchor-badge-text">STORIA-ANCORA MNEMONICA</span>
                </div>
                <span id="story-anchor-title" class="story-anchor-title"></span>
              </div>
              <p id="story-anchor-text" class="story-anchor-text"></p>
            </div>
            <div class="study-text-body" id="chap-summary-body"></div>
            <div class="key-points-section">
              <h3 class="key-points-heading">${I.pin} Punti Chiave da Sapere all'Esame</h3>
              <ul class="key-points-list" id="chap-key-points"></ul>
            </div>
            <div class="open-questions-section" id="open-questions-section" style="display: none;">
              <div class="open-questions-head">
                <h3 class="key-points-heading">${I.mic} Domande da orale</h3>
                <button type="button" class="btn-secondary-action" id="btn-oral-chapter">${I.mic} Simula l'orale</button>
              </div>
              <p class="open-questions-hint">Prova a rispondere ad alta voce prima di aprire la traccia di risposta.</p>
              <div class="open-questions-list" id="chap-open-questions"></div>
            </div>
          </div>

          <div id="subtab-panel-flashcards" class="subtab-panel">
            <div class="flashcards-container">
              <div class="flashcards-intro">
                <p>Tocca la scheda per girarla, poi indica quanto la ricordavi: le schede che non sapevi tornano prima nel ripasso, quelle che sapevi si allontanano nel tempo.</p>
              </div>
              <div class="flashcards-list" id="chap-flashcards-list"></div>
            </div>
          </div>

          <div id="subtab-panel-quiz" class="subtab-panel">
            <div class="quiz-container">
              <div class="quiz-intro">
                <p>Rispondi alle domande per consolidare i concetti. Riceverai subito la spiegazione didattica.</p>
              </div>
              <div class="quiz-list" id="chap-quiz-list"></div>
            </div>
          </div>

${navBar('chapter-footer chapter-nav-bottom', true)}
        </section>

        <section id="view-exam" class="view-panel">
          <div class="practice-tabs" role="tablist" aria-label="Modalità di allenamento">
            <button type="button" class="practice-tab active" data-practice="test">${I.exam}<span>Test a quiz</span></button>
            <button type="button" class="practice-tab" data-practice="review">${I.cards}<span>Ripasso</span><span class="practice-badge" id="review-due-badge" hidden></span></button>
            <button type="button" class="practice-tab" data-practice="oral">${I.mic}<span>Orale</span></button>
            <button type="button" class="practice-tab" data-practice="stats">${I.stats}<span>Progressi</span></button>
          </div>

          <div class="practice-panel active" id="practice-panel-test">
            <div class="panel-header">
              <h2 class="panel-title">${I.examLg} Simulatore d'Esame</h2>
              <p class="panel-description">Domande casuali a scelta multipla, con voto stimato in trentesimi e correzione finale.</p>
            </div>

            <div class="exam-setup-card" id="exam-setup-box">
              <div class="setup-group">
                <label for="exam-scope-select">Scegli l'ambito delle domande:</label>
                <div class="select-wrapper">
                  <select id="exam-scope-select" class="form-select">${scopeOptions}</select>
                  <span class="select-chevron" aria-hidden="true">${I.chevron}</span>
                </div>
              </div>
              <div class="setup-group">
                <label>Numero di domande:</label>
                <div class="num-pills">
                  <button class="num-btn active" data-count="10">10 domande</button>
                  <button class="num-btn" data-count="20">20 domande</button>
                  <button class="num-btn" data-count="30">30 domande</button>
                </div>
              </div>
              <button id="btn-start-exam" class="btn-primary-action">Inizia il Test d'Esame</button>
            </div>

            <div id="exam-active-box" style="display: none;">
              <div class="exam-header-bar">
                <span id="exam-question-counter">Domanda 1 di 10</span>
                <button id="btn-abort-exam" class="btn-secondary-link">Annulla test</button>
              </div>
              <div class="exam-progress-track"><div class="exam-progress-fill" id="exam-progress-fill"></div></div>
              <div id="exam-card-container"></div>
            </div>

            <div id="exam-result-box" style="display: none;" class="exam-result-card">
              <h3 class="result-title" id="exam-score-title"></h3>
              <p class="result-feedback" id="exam-score-feedback"></p>
              <div class="result-actions">
                <button id="btn-retry-exam" class="btn-primary-action">Ripeti Nuovo Test</button>
              </div>
              <div class="result-review-list" id="exam-review-list"></div>
            </div>
          </div>

          <div class="practice-panel" id="practice-panel-review">
            <div class="panel-header">
              <h2 class="panel-title">${I.cards} Ripasso a intervalli</h2>
              <p class="panel-description">Le flashcard tornano quando stai per dimenticarle: dopo 1, 3, 7, 14 e 30 giorni se le ricordi, subito se le sbagli.</p>
            </div>
            <div id="review-root"></div>
          </div>

          <div class="practice-panel" id="practice-panel-oral">
            <div class="panel-header">
              <h2 class="panel-title">${I.mic} Simulazione dell'orale</h2>
              <p class="panel-description">Una domanda alla volta, come all'esame: rispondi ad alta voce, poi confronta con la traccia e valuta la tua risposta.</p>
            </div>
            <div id="oral-root"></div>
          </div>

          <div class="practice-panel" id="practice-panel-stats">
            <div class="panel-header">
              <h2 class="panel-title">${I.stats} I tuoi progressi</h2>
              <p class="panel-description">Calcolati sui dati salvati in questo browser; con l'accesso sono gli stessi su tutti i tuoi dispositivi.</p>
            </div>
            <div id="stats-root"></div>
          </div>
        </section>

        <footer class="study-site-footer">
          <div class="study-site-footer-inner">
            <a class="footer-aba-logo" href="../index.html" title="Studio ABA Catania, home">${SITE_LOGO}</a>
            <div class="footer-aba-info">
              <p class="footer-inst-title">Studio ABA Catania</p>
              <p class="footer-inst-meta">Piattaforma di studio per gli studenti dell'Accademia di Belle Arti di Catania</p>
            </div>
          </div>
        </footer>
      </main>
    </div>

    <div class="sidebar-backdrop" id="sidebar-backdrop"></div>

    <div class="mobile-sheet-overlay" id="mobile-dispense-overlay">
      <div class="mobile-sheet-card">
        <div class="mobile-sheet-header">
          <div class="mobile-sheet-title">${I.book18}<span>Moduli della materia</span></div>
          <button class="mobile-sheet-close" id="btn-close-dispense-sheet" type="button" aria-label="Chiudi">${I.close18}</button>
        </div>
        <div class="mobile-dispense-list" id="mobile-dispense-list"></div>
      </div>
    </div>

    <nav class="mobile-bottom-bar" id="mobile-bottom-bar" aria-label="Navigazione rapida">
      <button id="btn-bottom-materie" class="bottom-nav-item" type="button" title="Scelta materie">${I.back}<span>Materie</span></button>
      <button id="btn-bottom-chapters" class="bottom-nav-item" type="button" title="Indice capitoli">${I.list}<span>Capitoli</span></button>
      <button id="btn-bottom-dispense" class="bottom-nav-item" type="button" title="Moduli della materia">${I.book20}<span>Moduli</span></button>
    </nav>
  </div>`;

  document.body.insertAdjacentHTML('afterbegin', html);
})(window, document);
