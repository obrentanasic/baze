# Baze podataka

Materijali za predmet Baze podataka — predavanja i pitanja za pripremu ispita.

## Predavanja

### Baze podataka 1 (BP1)

| # | Tema | Fajl |
|---|------|------|
| 01 | Uvod i osnovni pojmovi | [01_BP1_Uvod_Osnovni_pojmovi.pdf](predavanja/01_BP1_Uvod_Osnovni_pojmovi.pdf) |
| 02 | Koncepcija baze podataka | [02_BP1_Koncepcija_baze_podataka.pdf](predavanja/02_BP1_Koncepcija_baze_podataka.pdf) |
| 03 | Modeli podataka | [03_BP1_Modeli_podataka.pdf](predavanja/03_BP1_Modeli_podataka.pdf) |
| 04 | ER model — osnove | [04_BP1_ER_Model_Osnove.pdf](predavanja/04_BP1_ER_Model_Osnove.pdf) |
| 05 | Relacioni model — osnove | [05_BP1_Relacioni_model_osnove.pdf](predavanja/05_BP1_Relacioni_model_osnove.pdf) |

### Baze podataka 2 (BP2)

| # | Tema | Fajl |
|---|------|------|
| 06 | Prevođenje ER modela u relacioni model | [06_BP2_ER_RMP_Prevodjenje.pdf](predavanja/06_BP2_ER_RMP_Prevodjenje.pdf) |

### Organizacija datoteka (OD)

| # | Tema | Fajl |
|---|------|------|
| 07 | Eksterne memorije i fizička organizacija | [07_OD_EkstMemFizickaOrganizacija.pdf](predavanja/07_OD_EkstMemFizickaOrganizacija.pdf) |
| 08 | File sistem operativnog sistema | [08_OD_FileSistemOS.pdf](predavanja/08_OD_FileSistemOS.pdf) |
| 09 | Metode pristupa i organizacije datoteka | [09_OD_MetPristOrgDat.pdf](predavanja/09_OD_MetPristOrgDat.pdf) |
| 10 | Serijska i sekvencijalna datoteka | [10_OD_Serijska_Sekvencijalna_datoteka.pdf](predavanja/10_OD_Serijska_Sekvencijalna_datoteka.pdf) |
| 11 | Rasute datoteke | [11_OD_Rasute_datoteke.pdf](predavanja/11_OD_Rasute_datoteke.pdf) |
| 12 | Indeks-sekvencijalna statička datoteka | [12_OD_Indekssekvencijalna_staticka_datoteka.pdf](predavanja/12_OD_Indekssekvencijalna_staticka_datoteka.pdf) |
| 13 | Indeksna organizacija — B-stablo | [13_OD_Indeksna_B_stablo.pdf](predavanja/13_OD_Indeksna_B_stablo.pdf) |

## Priprema ispita

| Materijal | Fajl |
|-----------|------|
| Pitanja i odgovori, grupisano po temama (45 pitanja, 7 celina) | [Baze_podataka__pitanja_i_odgovori_grupisano_po_temama.pdf](ispit/Baze_podataka__pitanja_i_odgovori_grupisano_po_temama.pdf) |
| Primeri uz skriptu — dopuna za pitanja koja u skripti nemaju primer | [PDF](ispit/primeri-uz-skriptu.pdf) · [izvor u Markdownu](ispit/primeri-uz-skriptu.md) |

## Struktura

```
predavanja/   slajdovi sa predavanja, numerisani redom obrade
ispit/        pitanja i odgovori za pripremu ispita + primeri uz njih
tools/        md2pdf.py — generiše PDF iz markdown izvora
```

PDF se ponovo generiše sa `python3 tools/md2pdf.py` (potrebni `markdown` i `weasyprint`).
