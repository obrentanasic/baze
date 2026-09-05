#!/usr/bin/env python3
"""Generiše PDF iz ispit/primeri-uz-skriptu.md.

    pip install markdown weasyprint
    python3 tools/md2pdf.py

Naslovna strana i sadržaj se grade automatski iz strukture naslova u markdownu.
Fontovi su DejaVu (Serif / Sans / Sans Mono) — jedini komplet na sistemu koji
pokriva i naša slova i znakove za crtanje okvira u dijagramima.
"""
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

KOREN = Path(__file__).resolve().parent.parent
IZVOR = KOREN / "ispit" / "primeri-uz-skriptu.md"
IZLAZ = KOREN / "ispit" / "primeri-uz-skriptu.pdf"

CSS = """
@page {
  size: A4;
  margin: 19mm 18mm 16mm 18mm;
  @top-left {
    content: "Primeri uz skriptu";
    font-family: "DejaVu Sans"; font-size: 7.5pt; color: #8b95a5;
    padding-bottom: 3mm;
  }
  @top-right {
    content: string(celina);
    font-family: "DejaVu Sans"; font-size: 7.5pt; color: #8b95a5;
    padding-bottom: 3mm;
  }
  @bottom-center {
    content: counter(page);
    font-family: "DejaVu Sans"; font-size: 8pt; color: #8b95a5;
    padding-top: 3mm;
  }
}
@page bez-zaglavlja {
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-center { content: none; }
}

:root {
  --ink: #16202e;
  --muted: #5b6779;
  --accent: #2d4f7c;
  --accent-dark: #1e3a5f;
  --accent-soft: #eaf0f7;
  --rule: #d4dce6;
  --code-bg: #f6f8fa;
  --code-border: #dfe6ef;
}

body {
  font-family: "DejaVu Serif", serif;
  font-size: 9.6pt;
  line-height: 1.52;
  color: var(--ink);
  hyphens: none;
}

/* ---------- naslovna ---------- */

.naslovna {
  page: bez-zaglavlja;
  break-after: page;
  padding-top: 38mm;
}
.naslovna a { color: var(--accent); text-decoration: none; }
.naslovna .oznaka {
  font-family: "DejaVu Sans"; font-size: 9pt; letter-spacing: 0.22em;
  text-transform: uppercase; color: var(--accent); margin-bottom: 6mm;
}
.naslovna h1 {
  font-family: "DejaVu Sans"; font-size: 30pt; line-height: 1.15;
  color: var(--accent-dark); margin: 0 0 4mm 0; font-weight: bold;
}
.naslovna .podnaslov {
  font-family: "DejaVu Sans"; font-size: 13pt; color: var(--muted);
  margin: 0 0 9mm 0;
}
.naslovna .traka {
  height: 3.4mm; width: 46mm; background: var(--accent); margin-bottom: 9mm;
}
.naslovna .uvod { font-size: 10pt; max-width: 122mm; color: #33404f; }
.naslovna .uvod p { margin: 0 0 3.4mm 0; }
.naslovna .uvod code {
  font-family: "DejaVu Sans Mono"; font-size: 8.4pt;
  background: var(--accent-soft); padding: 0.4mm 1mm; border-radius: 1mm;
}
.naslovna .brojke {
  margin-top: 11mm; display: flex; gap: 12mm;
  border-top: 0.4mm solid var(--rule); padding-top: 5mm;
}
.naslovna .brojke div { font-family: "DejaVu Sans"; }
.naslovna .brojke .b {
  font-size: 19pt; color: var(--accent); font-weight: bold; display: block;
}
.naslovna .brojke .o {
  font-size: 7.6pt; color: var(--muted); letter-spacing: 0.09em;
  text-transform: uppercase;
}

/* ---------- sadržaj ---------- */

.sadrzaj { page: bez-zaglavlja; }
.sadrzaj h2 {
  font-family: "DejaVu Sans"; font-size: 15pt; color: var(--accent-dark);
  margin: 0 0 7mm 0; padding: 0 0 3mm 0; border-bottom: 0.7mm solid var(--accent);
  border-top: none; background: none;
}
.sadrzaj ol { list-style: none; margin: 0; padding: 0; }
.sadrzaj .celina {
  font-family: "DejaVu Sans"; font-size: 10pt; font-weight: bold;
  color: var(--accent-dark); margin: 5.5mm 0 1.8mm 0;
}
.sadrzaj .celina:first-child { margin-top: 0; }
.sadrzaj .pitanje {
  font-size: 9.2pt; margin: 0 0 0.9mm 0; padding-left: 9mm; color: #33404f;
}
.sadrzaj a { color: inherit; text-decoration: none; }
.sadrzaj .pitanje a::after,
.sadrzaj .celina a::after {
  content: " " leader(". ") " " target-counter(attr(href), page);
  color: #9aa5b4;
}
.sadrzaj .celina a::after { color: var(--accent); }
.sadrzaj .br {
  font-family: "DejaVu Sans Mono"; font-size: 8.4pt; color: var(--accent);
  padding-right: 2mm;
}

/* ---------- naslovi u tekstu ---------- */

h2 {
  break-before: page;
  font-family: "DejaVu Sans"; font-size: 17pt; font-weight: bold;
  color: var(--accent-dark);
  margin: 0 0 7mm 0; padding: 4mm 0 3.5mm 0;
  border-top: 1.2mm solid var(--accent);
  border-bottom: 0.3mm solid var(--rule);
}
h2 .br {
  display: block; font-size: 9pt; letter-spacing: 0.2em; color: var(--accent);
  margin-bottom: 1.5mm;
}
h2 .naslov { string-set: celina content(text); }
h3 {
  font-family: "DejaVu Sans"; font-size: 11.4pt; font-weight: bold;
  color: var(--accent-dark);
  margin: 8mm 0 3mm 0;
  break-after: avoid; break-inside: avoid;
}
h3 .br {
  display: inline-block; min-width: 11mm;
  color: #fff; background: var(--accent);
  font-size: 9pt; text-align: center; border-radius: 1mm;
  padding: 0.6mm 1.4mm; margin-right: 2.6mm;
}
h2 + h3 { margin-top: 0; }

/* ---------- telo ---------- */

p { margin: 0 0 3mm 0; orphans: 2; widows: 2; }
strong { color: var(--accent-dark); }
em { color: var(--muted); }

ul { margin: 0 0 3.4mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.2mm; }
li::marker { color: var(--accent); }

code {
  font-family: "DejaVu Sans Mono"; font-size: 8.3pt;
  background: var(--accent-soft); color: var(--accent-dark);
  padding: 0.3mm 0.9mm; border-radius: 0.8mm;
}

pre {
  font-family: "DejaVu Sans Mono"; font-size: 8.4pt; line-height: 1.34;
  background: var(--code-bg); border: 0.25mm solid var(--code-border);
  border-left: 1mm solid var(--accent);
  border-radius: 1mm;
  padding: 2.8mm 3.2mm; margin: 0 0 3.6mm 0;
  white-space: pre; break-inside: avoid; overflow: visible;
}
pre code { background: none; padding: 0; font-size: inherit; color: var(--ink); }

table {
  width: 100%; border-collapse: collapse;
  font-family: "DejaVu Sans"; font-size: 8.5pt; line-height: 1.35;
  margin: 0 0 4mm 0; break-inside: avoid;
}
th {
  background: var(--accent); color: #fff; font-weight: bold;
  text-align: left; padding: 1.7mm 2.2mm;
  border: 0.25mm solid var(--accent);
}
td {
  padding: 1.5mm 2.2mm; border: 0.25mm solid var(--rule); vertical-align: top;
}
tbody tr:nth-child(even) td { background: #f4f7fa; }
td code, th code { font-size: 7.9pt; background: rgba(45,79,124,0.09); }

hr { display: none; }

.ispravke { break-before: page; }
"""

SABLON = """<!DOCTYPE html>
<html lang="sr-Latn">
<head>
<meta charset="utf-8">
<title>Primeri uz skriptu — Baze podataka</title>
<style>{css}</style>
</head>
<body>
{naslovna}
{sadrzaj}
{telo}
</body>
</html>
"""


def izdvoj_broj(tekst):
    """'04 Gerund' -> ('04', 'Gerund'); '40–45 Create…' -> ('40–45', 'Create…')."""
    m = re.match(r"^([\d]+(?:[–-][\d]+)?)\s+(.*)$", tekst)
    return (m.group(1), m.group(2)) if m else (None, tekst)


def main():
    tekst = IZVOR.read_text(encoding="utf-8")

    # naslov i uvodni pasusi idu na naslovnu, ostalo u telo
    telo_md = tekst.split("\n---\n", 1)[1]
    uvod_md = tekst.split("\n---\n", 1)[0]
    uvod_md = "\n".join(uvod_md.split("\n")[1:]).strip()
    uvod_md = uvod_md.split("\n\n", 1)[1].strip()  # bez linka na PDF skripte

    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])
    telo = md.convert(telo_md)
    uvod = markdown.markdown(uvod_md)

    # broj u naslovu se izdvaja u <span class="br"> radi stilizovanja
    def obradi_naslov(m):
        nivo, atributi, sadrzaj = m.group(1), m.group(2), m.group(3)
        broj, ostatak = izdvoj_broj(sadrzaj)
        if broj is None:
            return m.group(0)
        return (f'<h{nivo}{atributi}><span class="br">{broj}</span>'
                f'<span class="naslov">{ostatak}</span></h{nivo}>')

    telo = re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", obradi_naslov, telo, flags=re.S)
    telo = telo.replace('<h2 id="sitne-ispravke-uz-skriptu">',
                        '<h2 id="sitne-ispravke-uz-skriptu" class="ispravke">')

    # sadržaj iz strukture naslova
    redovi = []
    for celina in md.toc_tokens:
        broj, ime = izdvoj_broj(celina["name"])
        oznaka = f'<span class="br">{broj}</span>' if broj else ""
        redovi.append(
            f'<li class="celina"><a href="#{celina["id"]}">{oznaka}{ime}</a></li>'
        )
        for pitanje in celina.get("children", []):
            broj, ime = izdvoj_broj(pitanje["name"])
            oznaka = f'<span class="br">{broj}</span>' if broj else ""
            redovi.append(
                f'<li class="pitanje"><a href="#{pitanje["id"]}">{oznaka}{ime}</a></li>'
            )
    sadrzaj = ('<section class="sadrzaj"><h2>Sadržaj</h2><ol>'
               + "".join(redovi) + "</ol></section>")

    def koliko_pitanja(oznaka):
        if oznaka is None:
            return 0
        granice = re.split(r"[–-]", oznaka)
        return int(granice[-1]) - int(granice[0]) + 1

    broj_pitanja = sum(
        koliko_pitanja(izdvoj_broj(p["name"])[0])
        for c in md.toc_tokens
        for p in c.get("children", [])
    )
    broj_celina = len([c for c in md.toc_tokens if izdvoj_broj(c["name"])[0]])

    naslovna = f"""<section class="naslovna">
  <div class="oznaka">Baze podataka</div>
  <h1>Primeri uz skriptu</h1>
  <div class="podnaslov">Rešeni primeri uz pitanja i odgovore</div>
  <div class="traka"></div>
  <div class="uvod">{uvod}</div>
  <div class="brojke">
    <div><span class="b">{broj_pitanja}</span><span class="o">pitanja sa primerom</span></div>
    <div><span class="b">{broj_celina}</span><span class="o">celina</span></div>
  </div>
</section>"""

    html = SABLON.format(css=CSS, naslovna=naslovna, sadrzaj=sadrzaj, telo=telo)
    HTML(string=html, base_url=str(KOREN)).write_pdf(IZLAZ)
    print(f"napravljeno: {IZLAZ.relative_to(KOREN)}")


if __name__ == "__main__":
    sys.exit(main())
