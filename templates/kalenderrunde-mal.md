# Mal for den genererte kalenderrunde-skillen

Dette er **ikke** en skill i seg selv — det er skjelettet du fyller ut når du
skriver den ferdige `SKILL.md`-fila for stedet i Steg 5. Hver `[…]`-blokk
beskriver hva som skal stå der. Skriv om til flytende norsk tekst, ikke la
klammene stå igjen i sluttresultatet.

Følg strukturen fra `vadsoby-kalenderrunde` (referert i README til denne
skillen) — samme oppbygning har vist seg å fungere i praksis. Det som er nytt
her er at innholdet er parametrisert per sted i stedet for hardkodet til
Vadsø.

---

```markdown
---
name: [sted-slug]-kalenderrunde
description: >
  Ukentlig runde for kalenderen på [nettside/prosjekt]. Samler arrangementer
  fra Facebook og fra aktører som ikke har hentbare data, legger dem fram til
  godkjenning, og skriver de godkjente inn på nettsiden.
  Bruk når: "kjør kalenderrunden", "hva skjer i [sted] denne uka", "oppdater
  kalenderen", "ukentlig kalender", "sjekk Facebook for arrangementer".
---

# Kalenderrunde for [sted]

[Én-to setninger: hva slags sted er dette (by/kommune/region), og hvilken
nettside/kalender skal den mate. Nevn evt. hvor mange kilder som allerede
hentes automatisk vs. hvor mange denne skillen dekker manuelt.]

**Den publiserer aldri selv.** Den legger fram forslag, [rolle/navn på den
som godkjenner] godkjenner, og først da skrives noe til nettsiden.

[Hvis relevant: prosjektmappe/repo-sti brukeren oppga i Steg 1.]

## Kildene

**Hentes allerede automatisk — skal IKKE samles inn her:**
[Tabell over kilder med strukturerte data/API-er funnet i Steg 2 — kino,
kulturhus, idrettslag med seriekamper, golf, etc. Tom tabell/avsnitt hvis
ingen slike finnes for stedet.]

**Denne skillens jobb:**
[Tabell: Aktør | Hvor (Facebook/nettside-URL) | Merk. Fyll inn alle aktørene
fra Steg 2 og 3 som IKKE har strukturerte data. Ta med samme type merknader
som i Vadsø-originalen der det er relevant: "Bruker innlegg, ikke
arrangementer", "Månedsplakat som bilde — må leses", "Er medlem" (hvis
brukeren har egen tilgang), "Eneste kilde" (der Facebook gir støy).]

## Instruksjoner for Claude

### Steg 1 — Se hva som allerede er dekket
[Kommando for å sjekke eksisterende data — TILPASSET nettsidens faktiske
oppsett fra Steg 4 i denne skillen (bygg-kommando, datafil å lese, eller
"ingen egen nettside ennå — se an mot forrige ukes forslagsliste i stedet").]

### Steg 2 — Facebooks arrangementssøk
[Samme mønster som originalen: bruk mcp__claude-in-chrome__*, hold seg til
arrangementssøk/bedriftssider, søk på stedsnavn + eventuelle nabotettsteder
brukeren nevnte i Steg 1 av DENNE skillen. Ta med samme advarsel om at
Graph API for events har vært stengt siden 2018 — bruk grensesnittet.]

### Steg 3 — Aktørene som poster bilder/plakater
[Tilpass til aktørene fra Steg 3-kartleggingen som poster program som bilde
eller plakat i stedet for strukturerte "Arrangement"-oppføringer.]

### Steg 4 — De som ikke er på Facebook
[Én kulepunkt-linje per strukturert kilde funnet i Steg 2 av DENNE skillen —
kino, bibliotek, kirke, museum, golf, osv. — med domenet, hva slags data den
gir, og eventuelle kjente svakheter (mangler årstall, mangler klokkeslett,
JS-rendret og krever nettleser, osv.). Kopiér gjerne formuleringene fra
`kildekategorier.md` og gjør dem spesifikke for de faktiske funnene.]

### Steg 5 — Legg fram forslagene
[Behold uendret fra originalen: tabell sortert på dato, marker Duplikat /
Usikker dato / Utenfor [området]. Spør "Hvilke skal inn?" og skriv ingenting
før mennesket har svart.]

### Steg 6 — Skriv til nettsiden
[Denne seksjonen avhenger av svaret i Steg 4 av DENNE skillen:
- **Generisk modus**: beskriv et enkelt, selvstendig format (markdown-tabell
  eller flat JSON-liste) som mennesket kan lime inn i sitt eget system.
- **Tilpasset modus**: gjengi det eksakte skjemaet/feltene/filstien brukeren
  oppga, med samme type feltregler som Vadsø-originalen har (obligatoriske
  felt, hva som ALDRI skal gjettes, hvordan flere arrangører håndteres, at
  sted ≠ arrangør, osv.) — tilpasset stedets faktiske nettside-struktur.]

### Steg 7 — Bygg, kontroller, publiser
[Bare ta med dette steget hvis brukeren har en nettside å bygge/publisere.
Bruk brukerens faktiske bygge-/deploy-kommandoer fra Steg 4. I generisk
modus: dropp steget, eller erstatt med "lever forslagsfila til mennesket".]

## Feller som har rammet oss
[Start med innholdet fra `vanlige-feller.md`, skrevet om til stedets kontekst.
Legg til stedsspesifikke feller etter hvert som de oppdages i praksis — dette
er en levende seksjon, ikke en engangsliste.]

## Hva skillen ikke skal gjøre

- **Ikke publiser uten godkjenning.** Alltid Steg 5 før Steg 6.
- **Ikke kjør ubemannet.** Startes av et menneske, [passende intervall — ofte
  ukentlig]. En robot som maler døgnet rundt på en innlogget Facebook-økt
  risikerer personkontoen.
- **Ikke legg inn [ekskluderte kategorier — f.eks. bortekamper hvis kalenderen
  bare skal dekke hjemmearrangementer, eller arrangementer utenfor det
  avgrensede området].**
```

---

## Notater til deg som fyller ut malen

- **Ikke fyll ut mer enn det du faktisk vet.** En tom rad i kildetabellen med
  «ikke funnet — sjekk manuelt senere» er bedre enn å dikte opp en URL.
- **Prosjektmappe/repo-sti** hentes fra brukerens svar i Steg 1 av
  hovedskillen (`SKILL.md`) — spør konkret om filbane, ikke anta en struktur.
- **«Skjer i kirken»-mønsteret** (én pålitelig strukturert kilde fremfor en
  foreldet arkivside) dukker ofte opp for flere aktørtyper enn kirken — vær
  obs på tilsvarende doble sider (gammel arkivside vs. ny driftet side) for
  andre kategorier også, og skriv inn hvilken som er fasit.
