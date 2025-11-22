const CACHE = 'my-website-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/assets/style.css',
  '/assets/app.js'
];

self.addEventListener('install', evt => {
  evt.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', evt => {
  evt.waitUntil(clients.claim());
});

self.addEventListener('fetch', evt => {
  evt.respondWith(
    caches.match(evt.request).then(r => r || fetch(evt.request))
  );
});
