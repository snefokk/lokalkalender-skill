---
name: lokalkalender-skill
description: >
  Bygger en selvstendig HTML-aktivitetskalender for et hvilket som helst sted
  (by, kommune eller region). Kartlegger lokale arrangementskilder (kino,
  kulturhus, idrettslag, bibliotek, kirke, museum, golf, og Facebook-sider
  uten API), samler kommende arrangementer, legger dem fram til godkjenning,
  og bygger en ferdig, dagsgruppert HTML-side — ingen server, ingen
  database, bare åpne fila. Første kjøring lager en kildeliste
  (kalenderkilder.md) som brukeren kan redigere selv, og en fast ukedag for
  oppdatering; senere kjøringer leser lista og samler bare nye arrangementer.
  Bruk når: "lag en aktivitetskalender for [sted]", "bygg en hva skjer-side
  for kommunen vår", "vi trenger noe som vadsoby sin kalender men for
  [sted]", "oppdater kalenderen for [sted]", "generer en HTML-kalender over
  lokale arrangementer".
---

# lokalkalender-skill

Bygger en **selvstendig HTML-side** — «Hva skjer i [sted]» — med kommende
lokale arrangementer, dagsgruppert og klar til å legges ut hvor som helst.
Ingen database, ingen server, ingen CMS å drifte: én fil, som kan åpnes
direkte i nettleseren eller legges på hvilken som helst webhotell/statisk
hosting.

Kalenderen er ferskvare. **Første gang** kartlegger skillen kildene og lager
en kildeliste, `kalenderkilder.md`, som stedet selv kan holde ved like — og man
avtaler en **fast ukedag** for oppdatering. **Senere ganger** leses lista, og
bare selve innsamlingen av arrangementer gjøres på nytt.

All kommunikasjon med brukeren skjer på **norsk**.

## Hva skillen leverer

- **Én HTML-fil** — dagsgruppert agenda (dato → arrangementer sortert på
  klokkeslett), med ikon per kategori, kategori-filter, billett-lenker der de
  finnes, og Snefokks visuelle stil (Newsreader/Inter, krem/lilla)
- **En kildeliste** (`kalenderkilder.md`) for stedet — lesbar og redigerbar
  for hånd, med fast oppdateringsdag øverst. Neste kjøring leser den i stedet
  for å kartlegge kino/bibliotek/kirke/Facebook-sider på nytt, og nye tips
  legges rett inn i den
- **En bygge-config** (`config.json`) med de godkjente arrangementene — kan
  redigeres for hånd mellom kjøringer om noen vil justere et enkelt punkt

## Når skillen passer

✅ **Bruk for**:
- Et sted som vil ha en samlet «hva skjer»-oversikt, uten å bygge eller
  drifte et eget nettsted for det
- En kommune, næringsforening eller reiselivsorganisasjon som vil legge en
  ferdig kalender inn på en eksisterende nettside (iframe, undermappe, eller
  lenke)
- Noen som vil ha samme type oversikt som vadsoby.com sin «Hva skjer»-side,
  uten Vadsøs egne database- og innsendingsløsning

❌ **Ikke bruk for**:
- Et sted som trenger at *publikum selv* skal kunne sende inn arrangementer
  gjennom et skjema — det krever en database og et innsendingsflow, som er
  utenfor det en statisk HTML-fil kan gjøre. Da trengs en løsning som
  vadsoby.com sin egen (Astro + database), ikke denne skillen.
- Sanntidsvarsling om nye arrangementer — dette er en periodisk batch-rutine
  (kjør på nytt for å oppdatere), ikke en live-feed

## Forutsetninger

- **Python 3** — for å bygge selve HTML-en (kun standardbibliotek, ingen
  `pip install`)
- **Chrome MCP / `mcp__claude-in-chrome__*`** (anbefalt) — for å søke
  Facebooks arrangementssøk og lese plakater/bilder aktørene poster
- **Internett** — for websøk mot lokale nettsider
- **Brukerens samarbeid** — særlig i steg 1 (avgrensning) og steg 4
  (godkjenning av forslag)

## Mappestruktur per sted

Hvert sted får sin egen arbeidsmappe, f.eks. `roros-kalender/`:

```
roros-kalender/
├── kalenderkilder.md               (kildeliste + oppdateringsdag — lages første gang, redigeres fritt)
├── config.json                     (tittel, farger, colophon + godkjente arrangementer)
└── hva-skjer-i-roros.html          (levert fil — bygges fra config.json)
```

Arbeidsmappene (`<sted>-kalender/`) inneholder kundedata og er ikke ment å
ligge i det offentlige skill-repoet — `.gitignore` i repoet ekskluderer dem.

## Overordnet flyt

```
0. Sjekk tidligere kjøring   → finnes kalenderkilder.md? Ja: les den, gå til steg 3. Nei: første kjøring
1. Intervju om stedet        → navn, geografisk avgrensning, naboområder, ønsket design (valgfritt)
2. Kartlegg kilder            → strukturerte (kino, bibliotek, kirke, museum …) + Facebook-only
2b. Lag kildelista            → skriv kalenderkilder.md, få den godkjent, velg fast oppdateringsdag
3. Samle arrangementer        → hent fra hver kilde i kalenderkilder.md, strukturer som utkast
4. Legg fram forslag          → tabell til godkjenning — MENNESKET avgjør hvilke som skal med
5. Bygg HTML                  → skriv godkjente til config.json, kjør build_html.py
6. Lever                      → vis fila, forklar hvordan man oppdaterer den neste gang
```

## Steg 0 — Sjekk tidligere kjøring

Spør brukeren hvilken mappe stedet skal bruke (opprett en ny hvis første
gang).

**Finnes `kalenderkilder.md`** → les den (den kan være redigert for hånd siden
sist — den er fasit). Si kort hva du fant, og spør om noe er nytt:

> Kildelista for [sted] har [N] kilder og oppdateres hver [ukedag]. Har dere
> fått tips om nye aktører siden sist, eller er noen lagt ned?

Legg inn det brukeren sier i lista, og gå til **steg 3**. Er «Kildene sist
gjennomgått» mer enn tre måneder gammel, foreslå en ny kartlegging (steg 2) —
nye aktører dukker opp.

Kjøres skillen en annen dag enn den avtalte, er det helt greit — bare nevn
neste faste oppdateringsdag i leveransen.

**Finnes en gammel `kilder.json`** (fra før kildelista ble en egen fil) → lag
`kalenderkilder.md` fra den (steg 2b), og spør om oppdateringsdag.

**Finnes ingen av dem** → første kjøring: start på **steg 1**.

## Steg 1 — Intervju om stedet

Spør brukeren (bruk `AskUserQuestion` der det passer):

1. **Hva heter stedet, og hva slags sted er det?** By/tettsted, kommune,
   eller region (flere kommuner)? Se `references/kildekategorier.md` under
   «Geografisk avgrensning» — dette styrer hvor bredt du skal søke.
2. **Er det naboområder som skal regnes med?** List dem — de brukes som
   ekstra søkeord i steg 2.
3. **Ønsket tittel/undertittel**, hvis noe annet enn «Hva skjer i [sted]».
4. **Profil: farger og fonter** — bruk Snefokk-standarden (se
   «Snefokk-defaults» under) med mindre bruker oppgir stedets egen profil.
   Spør i så fall etter: aksentfarge, evt. egen overskriftsfarge, og
   fontnavn for overskrift og brødtekst (Google Fonts). Lag aldri en kopi av
   malen for dette — alt styres fra `config.json` (se steg 5).
5. **Hvor skal fila og arbeidsmappa ligge?**

## Steg 2 — Kartlegg kilder (strukturerte + Facebook)

Gå gjennom **alle kategoriene** i `references/kildekategorier.md` — både de
som ofte har strukturerte data (kino, kulturhus, idrettslag, bibliotek,
museum, kirke, golf) og de som nesten alltid bare finnes på Facebook (barer,
foreninger, ungdomsklubb, frivilligsentral).

**For strukturerte kilder:** bruk `WebSearch`/`WebFetch`. Noter domene,
hva slags data kilden gir, og eventuelle kjente svakheter (mangler årstall,
JS-rendret, osv.) — se referansen for detaljer.

**For Facebook-only aktører:** bruk `mcp__claude-in-chrome__*`. Brukeren må
selv være logget inn i sin egen Chrome. Hold deg til arrangementssøk og
bedriftssider — ikke gå inn i feed, meldinger eller annet personlig.

Søk på hvert stedsnavn/naboområde fra steg 1:

```
https://www.facebook.com/search/events/?q=<stedsnavn>
https://www.facebook.com/search/events/?q=<naboområde 1>
```

**Hent lenkene med JavaScript, ikke bare tekst** — `get_page_text` gir titler
og datoer, men ikke URL-ene:

```js
[...document.querySelectorAll('a[href*="/events/"]')]
  .map(a => ({ t: (a.innerText||'').trim().split('\n')[0], h: a.href.split('?')[0] }))
  .filter(x => x.t && !x.h.includes('birthdays') && !x.h.endsWith('/events/'))
```

**Ikke bruk Graph API** — arrangementssøk er stengt der siden 2018.
Grensesnittet virker, API-et gjør det ikke.

For aktørene du finner konkrete sider til: sjekk **Arrangementer**-fanen
først, deretter innleggene — noen poster hele månedsprogrammet som én
plakat (zoom inn og les nøye, ikke gjett klokkeslett).

**Sjekk navnefella for hvert treff** — se `references/vanlige-feller.md`.

Hold rede på alt du finner — navn, kategori, lenke og hva som er spesielt med
kilden. Det blir kildelista i neste steg.

## Steg 2b — Lag kildelista og velg oppdateringsdag (bare første gang)

Skriv `kalenderkilder.md` i arbeidsmappa, med
`references/kalenderkilder-mal.md` som mal. Fire deler:

1. **Søkeord** for Facebooks arrangementssøk (stedet + naboområdene fra steg 1)
2. **Aktører som sjekkes for hånd** — Facebook-sider og nettsider uten
   hentbare data, med «Merk» om hva som er spesielt (plakat som bilde,
   månedsprogram, mangler årstall …)
3. **Faste ukentlige tilbud** — det som skjer samme tid hver uke
4. **Kilder med strukturerte data** — kino, billettsystem, seriekamper

Lista skal kunne leses og endres av noen som ikke kan kode: vanlige ord,
klikkbare lenker, ingen JSON.

**Legg lista fram før du går videre:**

> Her er kildene jeg fant for [sted] — [N] Facebook-sider, [N] nettsider og
> [N] faste ukentlige tilbud. Mangler det noen dere vet om, eller er noen
> feil?

Rett lista etter svaret.

**Velg så en fast oppdateringsdag** (bruk `AskUserQuestion`). Foreslå
**torsdag** som standard — da rekker kalenderen å bli oppdatert før helga og
kan deles i sosiale medier samme dag. Andre vanlige valg: mandag (planlegge
uka) eller søndag. Spør også hvor langt fram kalenderen skal dekke (standard
14 dager).

Skriv valgene inn øverst i `kalenderkilder.md` («Oppdateres hver»,
«Kalenderen dekker», «Laget», «Kildene sist gjennomgått»).

**Påminnelse (valgfritt):** Har plattformen planlagte oppgaver (f.eks.
scheduled tasks i Claude Code/Cowork), tilby en ukentlig påminnelse den valgte
dagen. Påminnelsen skal **bare spørre** om kalenderen skal oppdateres nå — den
skal aldri kjøre innsamlingen selv (se «Hva skillen ikke skal gjøre»). Lag den
bare hvis brukeren sier ja.

## Steg 3 — Samle arrangementer

Gå gjennom hver kilde i `kalenderkilder.md` — søkeordene i del 1, aktørene i
del 2, de faste tilbudene i del 3 (kontroller at tidene stemmer) og kildene i
del 4 — og hent kommende arrangementer innenfor perioden lista oppgir. For
hver oppføring, strukturer et utkast:

```json
{
  "dato": "2026-09-20",
  "tid": "19:00",
  "tittel": "Kveldsquiz",
  "sted": "Vertshuset Røros",
  "info": "Maks 5 per lag",
  "kategori": "uteliv",
  "pris": "gratis",
  "billett_url": null,
  "kilde_url": "https://facebook.com/events/..."
}
```

**Kategorier** (styrer ikon og filter i den ferdige HTML-en): `mat`,
`kultur`, `sport`, `bibliotek`, `kirke`, `uteliv`, `barn`, `annet`.

**Feller — les `references/vanlige-feller.md` før du går videre.** De
viktigste i korte trekk:
- Søketreff kan ligge langt utenfor det avgrensede området — sjekk stedet,
  ikke bare selve treffet.
- To like titler er ikke nødvendigvis duplikat — sjekk arrangørens egen side.
- Strukturerte kilder kan ha feil tidssone eller feilkodede norske tegn.
- **Ikke gjett** pris, sted eller klokkeslett — la feltet stå tomt/uklart og
  marker det som usikkert i steg 4, i stedet for å anta et sannsynlig svar.

## Steg 4 — Legg fram forslag til godkjenning

Tabell sortert på dato. Marker tydelig:
- **Duplikat** — samme arrangement funnet i to kilder
- **Usikker dato/pris/tid** — kilden var utydelig
- **Utenfor [området]** — treff som falt utenfor avgrensningen

Spør: *«Hvilke skal inn?»* — **og gå ikke videre før brukeren har svart.**
Dette steget er ikke valgfritt, uansett hvor «åpenbart riktig» forslagene
ser ut.

## Steg 5 — Bygg HTML

Skriv de godkjente arrangementene inn i `config.json` sitt
`arrangementer`-felt (se `examples/config-eksempel.json` for full struktur —
`tittel`, `eyebrow`, `h1`, `undertittel`, `generert`, `kilde_note`,
`colophon`, `arrangementer`, og valgfritt `farger`, `fonter` og
`skjul_passerte`).

Valgfrie felt for stedets profil og oppførsel:

```json
"farger": { "accent": "#eb6f0a", "heading": "#1a484f", "bg": "#ffffff" },
"fonter": { "overskrift": "Poppins", "brodtekst": "Open Sans", "overskrift_vekt": 700 },
"skjul_passerte": true
```

- `farger` — `bg`, `ink`, `ink_soft`, `accent`, `rule` og `heading`
  (overskriftsfarge; standard er `ink`). Det som utelates, får Snefokk-standard.
- `fonter` — Google Fonts-navn (bare bokstaver, tall, mellomrom, bindestrek).
  Lenken til Google Fonts bygges automatisk; `google_fonts_url` kan settes for
  å overstyre. `overskrift_vekt` er 500 som standard.
- `skjul_passerte` — standard `true`: dager før dagens dato (i leserens
  nettleser) skjules, så en fil som ikke er oppdatert ikke ser gammel ut.
  Sett `false` for demoer med faste datoer.

Kjør deretter:

```bash
python3 scripts/build_html.py \
  --config roros-kalender/config.json \
  --template templates/kalender-mal.html \
  --output roros-kalender/hva-skjer-i-roros.html
```

Scriptet er kun standardbibliotek — ingen `pip install`. Det setter inn
Snefokks fargetokens som standard (se «Snefokk-defaults») med mindre
`config.json` overstyrer dem under `"farger"`.

**Sjekk resultatet i nettleseren** før du leverer — åpne fila direkte
(`file://…`) og se at dagene grupperes riktig, at ikonene stemmer med
kategoriene, og at billett-lenker/priser vises som forventet.

## Steg 6 — Lever

- Gi brukeren HTML-fila (og forklar at den er selvstendig — ingen andre
  filer trengs, med mindre de vil endre den senere).
- Forklar hvordan den legges ut: åpnes direkte, legges i en undermappe på
  eksisterende nettsted, eller hostes av Snefokk.
- Forklar oppdatering: kalenderen oppdateres hver **[ukedag fra
  kalenderkilder.md]** ved å kjøre skillen på nytt for samme sted. **Steg 0**
  leser kildelista og går rett til innsamlingen.
- Forklar kildelista: `kalenderkilder.md` kan redigeres i hvilken som helst
  teksteditor — legg til en rad når dere får tips om en ny aktør, eller stryk
  en som er lagt ned. Den brukes neste gang.
- Har kildelista blitt endret i denne runden (nye tips, døde kilder), oppdater
  «Kildene sist gjennomgått» hvis du gikk gjennom hele lista.

## Feller som har rammet oss

Se `references/vanlige-feller.md` for full liste (navnefella, søketreff
utenfor området, strukturerte data som likevel har feil, arrangør ≠ sted,
sider uten årstall). Legg til stedsspesifikke feller etter hvert som de
oppdages — dette er en levende seksjon.

## Snefokk-defaults

- **Farger:** krem `#faf8f4` / lilla `#3d1f4d` (Snefokks husstil) med mindre
  brukeren ber om noe annet — se `DEFAULT_FARGER` i `scripts/build_html.py`.
- **Fonter:** Newsreader (overskrifter, serif) + Inter (brødtekst, sans) —
  lastet fra Google Fonts, samme oppsett som snefokk.com. Overstyres med
  `fonter` i `config.json` når stedet har egen profil.
- **Footer:** *«Laget med hjerte i nord av Snefokk»*, lenket til
  snefokk.com — står fast i malen, ikke noe brukeren skal fjerne eller
  omformulere.
- **Ikoner:** åtte kategori-ikoner (mat, kultur, sport, bibliotek, kirke,
  uteliv, barn, annet) som tynne linje-SVG-er i aksentfargen — definert i
  `templates/kalender-mal.html`.

## Hva skillen ikke skal gjøre

- **Ikke bygg HTML uten godkjenning.** Alltid steg 4 før steg 5.
- **Ikke kjør ubemannet.** Startes av et menneske hver gang. En planlagt
  påminnelse på oppdateringsdagen skal bare spørre, aldri starte innsamlingen.
- **Ikke legg nye kilder bare i hodet eller i en annen fil.** Alt som skal
  sjekkes, står i `kalenderkilder.md`.
- **Ikke gjett** pris, sted eller klokkeslett.
- **Ikke ta med arrangementer utenfor det avgrensede området.**

## Filer i denne skillen

```
lokalkalender-skill/
├── SKILL.md                          (denne fila)
├── templates/
│   └── kalender-mal.html             (HTML-mal med placeholders + inline JS-rendering)
├── scripts/
│   └── build_html.py                 (templating — kun standardbibliotek)
├── examples/
│   ├── config-eksempel.json          (eksempel på full config-struktur)
│   └── hva-skjer-i-vadso.html        (bygget demo, til referanse)
└── references/
    ├── kalenderkilder-mal.md         (mal for kildelista som lages første gang)
    ├── kildekategorier.md            (hvor du leter, kategori for kategori)
    └── vanlige-feller.md             (generaliserte fallgruver)
```
