// static/js/toast.js
(function () {
  const box   = document.getElementById('toast-component');
  const title = document.getElementById('toast-title');
  const msg   = document.getElementById('toast-message');
  const icon  = document.getElementById('toast-icon');

  let hideTimer;

  function setStyleByType(type) {
    // warna/ikon sederhana
    if (!icon) return;
    const map = {
      success: '✅',
      error:   '⛔',
      info:    'ℹ️',
      warning: '⚠️',
    };
    icon.textContent = map[type] || '🔔';
  }

  function show(titleText, messageText, type = 'info', duration = 4000) {
    if (!box || !title || !msg) return;
    title.textContent = titleText || '';
    msg.textContent   = messageText || '';
    setStyleByType(type);

    // tampilkan
    box.style.opacity   = '1';
    box.style.transform = 'translateY(0)';

    // auto hide
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, duration);
  }

  function hide() {
    if (!box) return;
    box.style.opacity   = '0';
    box.style.transform = 'translateY(32px)';
  }

  // Biar bisa dipanggil dari mana saja
  window.showToast = show;

  // Konsumsi “pending toast” setelah pindah halaman (mis. register → login, login → home)
  window.consumePendingToast = function () {
    try {
      const raw = sessionStorage.getItem('pendingToast');
      if (!raw) return;
      sessionStorage.removeItem('pendingToast');
      const t = JSON.parse(raw);
      show(t.title || 'Info', t.message || '', t.type || 'info', t.duration || 4000);
    } catch (_) {}
  };

  // Kalau kamu mau tutup manual:
  window.hideToast = hide;
})();
