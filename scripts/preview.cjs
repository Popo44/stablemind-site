const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(process.argv[2] || path.join(__dirname, '..', 'site'));
const port = Number(process.env.STABLEMIND_PREVIEW_PORT || 4190);
if (!fs.existsSync(path.join(root, 'index.html'))) {
  console.error('Aucun index.html dans : ' + root);
  process.exit(1);
}
const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'application/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.woff':'font/woff','.woff2':'font/woff2','.ttf':'font/ttf','.otf':'font/otf','.xml':'application/xml','.txt':'text/plain; charset=utf-8'};
http.createServer((req, res) => {
  let file;
  try { file = path.resolve(root, '.' + decodeURIComponent(new URL(req.url, 'http://localhost').pathname)); }
  catch { res.writeHead(400); res.end(); return; }
  if (file !== root && !file.startsWith(root + path.sep)) { res.writeHead(403); res.end(); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); res.end('Page introuvable'); return; }
  res.setHeader('Content-Type', mime[path.extname(file).toLowerCase()] || 'application/octet-stream');
  res.setHeader('Cache-Control', 'no-store');
  const stream = fs.createReadStream(file);
  stream.on('error', () => { res.destroy(); });
  stream.pipe(res);
}).listen(port, '127.0.0.1', () => {
  console.log('Version locale : http://127.0.0.1:' + port);
  console.log('Dossier affiche : ' + root);
  console.log('Laissez cette fenetre ouverte. Ctrl+C pour arreter.');
}).on('error', err => {
  console.error(err.code === 'EADDRINUSE' ? 'Le port est deja utilise. Fermez le precedent apercu local puis relancez.' : err.message);
  process.exitCode = 1;
});
