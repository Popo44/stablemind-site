"""Check SEO metadata, structured data, canonical URLs and local resources.

Run with Python 3; no third-party dependencies are required.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'site'
BASE = 'https://www.stablemind.fr'


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.json_blocks = []
        self.in_json = False
        self.block = ''
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True
            self.block = ''

    def handle_data(self, value):
        if self.in_json:
            self.block += value

    def handle_endtag(self, tag):
        if tag == 'script' and self.in_json:
            self.json_blocks.append(json.loads(self.block))
            self.in_json = False


def local_path(page, url):
    pathname = unquote(urlsplit(url).path)
    target = ROOT / pathname.lstrip('/') if pathname.startswith('/') else page.parent / pathname
    target = target.resolve()
    assert target.is_relative_to(ROOT), f'Path outside site: {url}'
    if target.is_dir():
        target /= 'index.html'
    assert target.is_file(), f'{page.relative_to(ROOT)}: missing resource {url}'
    # Windows accepts case mismatches that GitHub Pages does not.
    relative = target.relative_to(ROOT)
    current = ROOT
    for part in relative.parts:
        assert part in {p.name for p in current.iterdir()}, f'Incorrect case: {url}'
        current /= part
    return target


def image_width(path):
    """Read widths of our responsive WebP/PNG assets without extra packages."""
    data = path.read_bytes()
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return int.from_bytes(data[16:20], 'big')
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        offset = 12
        while offset + 8 <= len(data):
            kind = data[offset:offset + 4]
            size = int.from_bytes(data[offset + 4:offset + 8], 'little')
            payload = data[offset + 8:offset + 8 + size]
            if kind == b'VP8X':
                return int.from_bytes(payload[4:7], 'little') + 1
            if kind == b'VP8 ':
                return int.from_bytes(payload[6:8], 'little') & 0x3fff
            if kind == b'VP8L':
                return (int.from_bytes(payload[1:5], 'little') & 0x3fff) + 1
            offset += 8 + size + (size % 2)
    raise AssertionError(f'Unsupported responsive image format: {path.name}')


pages = {p: Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
canonicals = set()
refs = 0
for path, page in pages.items():
    label = path.relative_to(ROOT)
    tags = page.tags
    assert len([a for t, a in tags if t == 'h1']) == 1, f'{label}: expected one H1'
    assert len([a for t, a in tags if t == 'main']) == 1, f'{label}: expected one main landmark'
    metas = [a for t, a in tags if t == 'meta']
    for name in ['description', 'robots', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']:
        matches = [a for a in metas if a.get('name') == name]
        assert len(matches) == 1 and matches[0].get('content'), f'{label}: metadata {name}'
    for prop in ['og:title', 'og:description', 'og:image', 'og:type', 'og:locale']:
        assert len([a for a in metas if a.get('property') == prop and a.get('content')]) == 1, f'{label}: {prop}'
    links = [a for t, a in tags if t == 'link' and a.get('rel') == 'canonical']
    redirects = [a for a in metas if a.get('http-equiv', '').lower() == 'refresh']
    if redirects:
        assert len(redirects) == 1 and redirects[0].get('content') == f'0; url={BASE}/', f'{label}: unexpected migration target'
        assert path.relative_to(ROOT).as_posix() in ['old-home-2.html', 'old-home-2/index.html'], f'{label}: undeclared redirect'
        assert len(links) == 1 and links[0]['href'] == BASE + '/'
        assert any(a.get('name') == 'robots' and 'noindex' in a.get('content', '') for a in metas)
        assert not page.json_blocks
    elif path.name == '404.html':
        assert not links and any(a.get('name') == 'robots' and 'noindex' in a.get('content', '') for a in metas)
        assert not page.json_blocks
    else:
        assert len(links) == 1 and links[0]['href'].startswith(BASE + '/')
        canonical = links[0]['href']
        canonicals.add(canonical)
        target = local_path(path, urlsplit(canonical).path)
        assert target in pages
        assert len(page.json_blocks) == 1
        graph = page.json_blocks[0]['@graph']
        assert next(n for n in graph if n['@type'] == 'WebPage')['url'] == canonical
    ids = [a['id'] for t, a in tags if a.get('id')]
    assert len(ids) == len(set(ids)), f'{label}: duplicate IDs'
    for tag, attrs in tags:
        if tag == 'img':
            assert 'alt' in attrs, f'{label}: missing alt'
        urls = []
        if attrs.get('src'):
            urls.append(attrs['src'])
        if tag in ['link', 'a'] and attrs.get('href'):
            urls.append(attrs['href'])
        if attrs.get('srcset'):
            widths = set()
            for part in attrs['srcset'].split(','):
                candidate = part.strip().split()
                urls.append(candidate[0])
                if len(candidate) == 2 and candidate[1].endswith('w'):
                    width = int(candidate[1][:-1])
                    assert width not in widths, f'{label}: duplicate width in srcset'
                    widths.add(width)
                    image = local_path(path, candidate[0])
                    assert width == image_width(image), f'{label}: wrong width for {candidate[0]}'
        for url in urls:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            target = local_path(path, url) if parsed.path else path
            refs += 1
            if parsed.fragment and target.suffix == '.html':
                assert target in pages and any(a.get('id') == unquote(parsed.fragment) for _, a in pages[target].tags), f'{label}: broken anchor {url}'
for css in (ROOT / 'css').glob('*.css'):
    for url in re.findall(r'url\([\'\"]?([^\)\'\"]+)', css.read_text(encoding='utf-8')):
        if not urlsplit(url).scheme and not url.startswith('#'):
            local_path(css, url)
            refs += 1
sitemap = ET.parse(ROOT / 'sitemap.xml')
listed = {node.text for node in sitemap.findall('.//{*}loc')}
assert listed == canonicals, 'Sitemap must contain exactly the canonical indexable pages'
assert (ROOT / 'CNAME').read_text().strip() == 'www.stablemind.fr'
assert BASE + '/sitemap.xml' in (ROOT / 'robots.txt').read_text()
print(f'OK: {len(pages)} HTML files, {len(canonicals)} canonical URLs, {refs} local references, JSON-LD and sitemap.')
