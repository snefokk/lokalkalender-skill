---
name: lokalkalender-skill
description: >
  Bygger en skreddersydd "kalenderrunde"-skill for et hvilket som helst sted
  (by, kommune eller region) — en ukentlig rutine som samler lokale
  arrangementer fra Facebook og andre kilder uten API, legger dem fram til
  godkjenning, og (valgfritt) skriver de godkjente inn på stedets nettside.
  Kartlegger automatisk lokale kilder (kino, kulturhus, idrettslag,
  bibliotek, kirke, museum, og Facebook-sider) for stedet, og genererer en
  ferdig SKILL.md tilpasset stedet.
  Bruk når: "lag en kalenderskill for [sted]", "bygg kalenderrunde for
  kommunen vår", "vi trenger noe som vadsoby sin kalenderrunde men for
  [sted]", "generer en arrangementskalender-skill", "lag en lokal versjon av
  kalenderrunde-mønsteret".
---

# lokalkalender-skill

Denne skillen bygger **ikke** en kalender. Den bygger **en ny skill** — en
egen `SKILL.md` som gjør for et annet sted det `vadsoby-kalenderrunde` gjør
for Vadsø: kartlegger lokale arrangementskilder, samler forslag ukentlig,
legger dem fram for godkjenning, og (hvis stedet har en nettside for det)
skriver de godkjente inn.

Tenk på det som en **fabrikk**, ikke selve produktet. Når du er ferdig har
brukeren en ny mappe, f.eks. `roros-kalenderrunde/SKILL.md`, som de selv
kjører hver uke — akkurat som Vadsø-varianten.

All kommunikasjon med brukeren skjer på **norsk**.

## Hva skillen leverer

En ferdig `SKILL.md`-fil (pluss en kort README om brukeren vil ha den som
eget repo) for det oppgitte stedet, med:

- Riktig frontmatter (`name`, `description` med triggerord) for stedet
- En kildetabell delt i «hentes automatisk» og «må samles manuelt»
- Steg-for-steg instruksjoner tilpasset de faktiske kildene som ble funnet
- Et skrive-steg tilpasset stedets nettside — enten en generisk
  forslagsliste, eller et skreddersydd format hvis brukeren oppga sin
  nettsides datastruktur
- En feller-seksjon med generaliserte fallgruver, klar til å bygges videre på

## Når skillen passer

✅ **Bruk for**:
- En kommune, næringsforening eller reiselivsorganisasjon som vil ha samme
  type ukentlige kalenderrunde som Vadsø, for sitt eget sted
- Et sted som allerede har en nettside med kalender, men mangler en rutine
  for å fylle den med det som ikke ligger i noe API
- Et sted som ikke har noen nettside ennå, men vil ha en ryddig, ukentlig
  forslagsliste over lokale arrangementer

❌ **Ikke bruk for**:
- Selve den ukentlige kjøringen — det gjør skillen denne genererer, ikke
  denne selv
- Nasjonale eller store, sammensatte kalendere (denne skillen er bygget for
  ett sted eller én sammenhengende region av gangen)
- Sanntids/øyeblikkelig varsling om nye arrangementer — dette er en ukentlig
  batch-rutine, ikke en live-feed

## Forutsetninger

- **Internett** — for websøk og oppslag mot lokale nettsider
- **Chrome MCP / `mcp__claude-in-chrome__*`** (anbefalt) — for å søke
  Facebooks arrangementssøk og lese plakater/bilder aktørene poster
- **Brukerens samarbeid** — særlig i Steg 1 og 4, der bare brukeren kan svare
  på geografisk avgrensning og hvordan nettsiden deres er bygget opp
- *Valgfritt:* tilgang til brukerens nettside-repo, hvis skillen skal skrive
  et tilpasset (ikke generisk) skrive-steg

## Overordnet flyt

```
1. Intervju om stedet        → navn, geografisk avgrensning, finnes nettside/kalender allerede?
2. Kartlegg strukturerte kilder → kino, kulturhus, idrettslag, bibliotek, kirke, museum, golf …
3. Kartlegg Facebook-only     → søk arrangementssøk + bedriftssider for stedet
4. Avklar skrive-format       → generisk forslagsliste, ELLER tilpasset brukerens nettside-struktur
5. Generer SKILL.md           → fyll malen i templates/kalenderrunde-mal.md
6. Lever + neste steg         → hvor fila skal ligge, hvordan brukeren tar den i bruk
```

## Steg 1 — Intervju om stedet

Spør brukeren (bruk `AskUserQuestion` der det passer):

1. **Hva heter stedet, og hva slags sted er det?** By/tettsted, kommune,
   eller region (flere kommuner)? Se `references/kildekategorier.md` under
   «Geografisk avgrensning» — dette styrer hvor bredt du skal søke og hvor
   nøye du må sjekke treff mot faktisk sted.
2. **Er det naboområder som skal regnes med?** (Som Vestre Jakobselv og
   Ekkerøy for Vadsø.) List dem — de brukes som ekstra søkeord i Steg 3.
3. **Finnes det allerede en nettside med kalender for stedet?**
   - Ja → be om URL og (hvis mulig) tilgang til repoet/CMS-et, til bruk i
     Steg 4.
   - Nei → skillen leverer en generisk forslagsliste (se Steg 4).
4. **Hvem skal godkjenne forslagene hver uke?** (Navn/rolle — brukes i
   den genererte skillens tekst om at den aldri publiserer på egen hånd.)

Ikke gå videre før du har svar på minst 1 og 3 — resten kan avklares
underveis.

## Steg 2 — Kartlegg strukturerte kilder

Gå gjennom **kategori A** i `references/kildekategorier.md` (kino,
kulturhus, idrettslag med seriekamper, bibliotek, museum, kirke, golf,
svømmehall) og søk etter hver for stedet. Bruk `WebSearch`/`WebFetch`.

For hver kategori du finner noe i, noter:
- Domene/URL
- Hva slags data den gir (arrangementer med dato+tid? bare beskrivelse uten
  dato? JS-rendret og krever nettleser for å lese?)
- Om den er egnet til automatisk henting (ekte API/feed) eller om den likevel
  må sjekkes manuelt hver uke (strukturert nok til å lese, men ikke skrapbar)

**Sjekk navnefella for hvert treff** — se `references/vanlige-feller.md`.
Et treff som `[aktørnavn].no` er ikke automatisk riktig aktør.

Presenter funnene som en tabell for brukeren før du går videre, med en kort
anbefaling per rad: «automatisk-kandidat», «manuell, men pålitelig kilde»,
eller «fant ikke noe — dekk manuelt via Facebook om de har det».

## Steg 3 — Kartlegg Facebook-only-aktører

Gå gjennom **kategori B og C** i `references/kildekategorier.md` (barer,
restauranter, foreninger, ungdomsklubb, frivilligsentral, turistkontor).

Bruk `mcp__claude-in-chrome__*`. Brukeren må selv være logget inn i sin egen
Chrome. Hold deg til arrangementssøk og bedriftssider — ikke gå inn i feed,
meldinger eller annet personlig.

Søk på hvert stedsnavn/naboområde fra Steg 1:

```
https://www.facebook.com/search/events/?q=<stedsnavn>
https://www.facebook.com/search/events/?q=<naboområde 1>
https://www.facebook.com/search/events/?q=<naboområde 2>
```

**Hent lenkene med JavaScript, ikke bare tekst.** `get_page_text` gir titler
og datoer, men ikke URL-ene — og hver oppføring må ha lenke til selve
arrangementet:

```js
[...document.querySelectorAll('a[href*="/events/"]')]
  .map(a => ({ t: (a.innerText||'').trim().split('\n')[0], h: a.href.split('?')[0] }))
  .filter(x => x.t && !x.h.includes('birthdays') && !x.h.endsWith('/events/'))
```

**Ikke bruk Graph API.** Arrangementssøk er stengt der siden 2018 og svarer
`code 3` uansett innlogging. Grensesnittet virker, API-et gjør det ikke.

For aktørene du finner konkrete sider til: sjekk **Arrangementer**-fanen
først, deretter innleggene — noen aktører (som Baja i Vadsø-originalen)
poster hele månedsprogrammet som én plakat. Noter det som en egen merknad i
kildetabellen («bruker plakat, må zoomes og leses manuelt»).

## Steg 4 — Avklar skrive-format

Spør brukeren:

> Har nettsiden deres en fast måte arrangementer legges inn på (en egen
> datafil, et CMS, en database) — eller vil dere heller ha en enkel liste å
> jobbe videre med selv?

**Generisk modus (standard, og alltid det du leverer minst denne):**
Skriv-steget i den genererte skillen beskriver en enkel, selvstendig
forslagsfil — én rad per arrangement med tittel, dato/tid, sted, arrangør(er),
pris (kun når kjent), kilde-lenke — som markdown-tabell eller flat JSON.
Ingen antakelser om mottakersystem.

**Tilpasset modus (i tillegg, hvis brukeren har en nettside):**
Be om:
- Filstien til der arrangementer lagres (som `src/data/innsendt.json` i
  Vadsø-varianten), eller navnet på CMS-et/databasen
- Et eksempel på strukturen — helst et faktisk utdrag, ikke en beskrivelse
- Feltreglene: hvilke felt er obligatoriske, hvordan håndteres flere
  arrangører, hvordan skiller de sted fra arrangør, hvordan markeres pris
  når den er ukjent

Bruk svarene til å skrive et presist, stedstilpasset Steg 6 i den genererte
skillen — med samme type strenge regler som Vadsø-originalen har («ikke
gjett», «sted er ikke arrangør», «lenke er obligatorisk»). Ta også med et
bygge-/publiseringssteg (Steg 7) **bare** hvis brukeren har en byggeprosess å
kjøre.

## Steg 5 — Generer SKILL.md

Fyll ut `templates/kalenderrunde-mal.md` med det du har samlet i Steg 1–4.
Skriv den ferdige fila til en ny mappe brukeren oppgir (typisk
`<sted-slug>-kalenderrunde/SKILL.md`), ikke inn i denne skillens egne
templates-mappe.

Sjekkliste før du leverer:
- [ ] Frontmatter har konkrete triggerord for stedet, ikke bare Vadsø-teksten
      omskrevet
- [ ] Kildetabellene reflekterer faktiske funn fra Steg 2–3, ikke plassholdere
- [ ] Skriv-steget matcher det brukeren faktisk svarte i Steg 4
- [ ] Feller-seksjonen er skrevet om til stedets kontekst (se
      `references/vanlige-feller.md`), ikke kopiert med Vadsø-eksemplene
      stående igjen
- [ ] «Ikke publiser uten godkjenning» og «ikke kjør ubemannet» står med i
      «Hva skillen ikke skal gjøre» — dette er ikke valgfritt

## Steg 6 — Lever

Fortell brukeren:
- Hvor fila ble lagret
- Hvordan de tar den i bruk (legg mappa i sin egen skill-katalog, eller be om
  at Claude leser `SKILL.md` direkte ved kjøring)
- At **første kjøring bør kjøres sammen med et menneske** — kildetabellen er
  et utgangspunkt, ikke fasit, og den blir bedre etter en runde eller to i
  praksis (slik Vadsø-versjonens «Feller som har rammet oss»-seksjon har
  vokst fram)

## Filer i denne skillen

```
lokalkalender-skill/
├── SKILL.md                          (denne fila)
├── templates/
│   └── kalenderrunde-mal.md          (skjelett for den genererte skillen)
└── references/
    ├── kildekategorier.md            (hvor du leter, kategori for kategori)
    └── vanlige-feller.md             (generaliserte fallgruver fra Vadsø-originalen)
```

## Snefokk-defaults

- Skriv alltid triggerordene i `description` på norsk og konkret til stedet
  — vage triggerord ("kjør runden") gjør at skillen ikke plukkes opp av
  Claude senere.
- Hold den genererte skillen i samme struktur som denne (frontmatter → kort
  intro → kildetabell → nummererte steg → feller → «hva skillen ikke skal
  gjøre») — konsistens på tvers av stedene gjør det lettere for Snefokk å
  vedlikeholde flere av dem samtidig.
- Behold alltid menneske-i-loopen-prinsippet uendret: ingen generert skill
  skal kunne publisere uten godkjenning, uansett hvor lite risikabelt stedet
  virker.
