// Portal Syndex — guarda o portal para abrir rápido e funcionar com internet fraca.
// Sempre tenta a versão nova primeiro; usa a guardada só se estiver sem conexão.
const CACHE = 'portal-syndex-v1';
const ARQUIVOS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './assets/syndex-logo.png',
  './assets/syndex-simbolo.png',
  './assets/syndex-fundo.jpg',
  './icon-192.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ARQUIVOS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((nomes) => Promise.all(nomes.filter((n) => n !== CACHE).map((n) => caches.delete(n))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  e.respondWith(
    fetch(req)
      .then((res) => {
        const copia = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copia));
        return res;
      })
      .catch(() => caches.match(req).then((r) => r || caches.match('./')))
  );
});
