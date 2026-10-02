// VText service worker: the app is cached and only changes when the user taps Settings > App update.
const CACHE = 'vtext-shell';
const FILES = ['./', 'index.html', 'offline.html', 'logo.svg', 'manifest.json'];
const reqOf = u => new Request(new URL(u, self.registration.scope).href);

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    if (!(await c.keys()).length) {
      for (const u of FILES) { try { await c.add(reqOf(u)); } catch (x) {} }
    }
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));

self.addEventListener('fetch', e => {
  const r = e.request, u = new URL(r.url);
  if (r.method !== 'GET' || u.origin !== location.origin || u.pathname.endsWith('/version.json')) return;
  e.respondWith((async () => {
    const hit = await caches.match(r, { ignoreSearch: true });
    return hit || fetch(r);
  })());
});

self.addEventListener('message', e => {
  if (e.data !== 'update') return;
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    let ok = 0;
    for (const u of FILES) {
      try {
        const base = reqOf(u).url;
        const res = await fetch(base + (base.includes('?') ? '&' : '?') + 't=' + Date.now(), { cache: 'reload' });
        if (res.ok) { await c.put(reqOf(u), res); ok++; }
      } catch (x) {}
    }
    const target = e.source || (await self.clients.matchAll())[0];
    if (target) target.postMessage(ok ? 'updated' : 'failed');
  })());
});
