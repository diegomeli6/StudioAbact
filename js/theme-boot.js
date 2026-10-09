/**
 * Applica subito il tema salvato, prima del caricamento dei dati, per evitare il lampo
 * di tema chiaro. Va incluso come primo elemento dentro <body> (home e pagine di studio).
 */
(function () {
  try {
    var theme = localStorage.getItem('aba_studio_theme');
    if (theme === 'dark') {
      document.body.classList.remove('theme-light');
      document.body.classList.add('theme-dark');
    }
  } catch (e) {}
})();
