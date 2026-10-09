# lokalkalender-skill

Bygger en **selvstendig HTML-aktivitetskalender** — «Hva skjer i [sted]» —
for et hvilket som helst sted i Norge: by, kommune eller region. Kartlegger
lokale arrangementskilder, samler kommende arrangementer, legger dem fram
til godkjenning, og bygger en ferdig, dagsgruppert HTML-side. Ingen server,
ingen database — bare åpne fila. En åpen skill for Claude (Cowork / Claude
Code).

> **Vil du heller at vi bygger kalenderen for deg?**
> Bestill en ferdig aktivitetskalender på
> **[snefokk.com/kalender](https://snefokk.com/kalender)** — så bygger
> Snefokk den, tilpasser kildene og designet, og leverer klar til bruk.
> Dette repoet er for deg som vil gjøre jobben selv, gratis.

## Hva skillen lager

- **Én selvstendig HTML-fil** — dagsgruppert agenda (dato → arrangementer
  sortert på klokkeslett), med ikon per kategori, kategori-filter og
  billett-lenker der de finnes
- **Snefokks visuelle stil** — Newsreader/Inter, krem/lilla, samme
  typografiske system som snefokk.com
- **Kartlegger kildene automatisk** — kino, kulturhus, idrettslag,
  bibliotek, kirke, museum, golf, og Facebook-sider uten API
- **Rask å oppdatere** — kjør skillen på nytt (f.eks. ukentlig), så
  gjenbrukes kildelista fra forrige kjøring; bare selve arrangementene
  hentes ferskt
- **Mennesket godkjenner alltid** — skillen bygger aldri HTML-en uten at
  forslagene er godkjent først

## Hvem det er for

- Kommuner, næringsforeninger og reiselivsorganisasjoner som vil ha en
  samlet «hva skjer»-oversikt, uten å bygge og drifte et eget nettsted for
  det
- Nettsteder som vil legge en ferdig kalender inn på en eksisterende side
  (undermappe, iframe, eller egen lenke)
- Steder som vil ha noe i samme ånd som vadsoby.com sin «Hva skjer»-side,
  uten Vadsøs egen database- og innsendingsløsning

## To måter å få kalenderen

| Gjør det selv (dette repoet)                                                            | La Snefokk gjøre jobben                                             |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Gratis — krever et Claude-abonnement                                                    | Bestill på **[snefokk.com/kalender](https://snefokk.com/kalender)** |
| Du kjører skillen selv i Claude — kartlegger kilder, godkjenner forslag, bygger HTML-en | Snefokk kartlegger kildene, tilpasser designet og leverer           |
| Kjør på nytt selv så ofte du vil, ingen ekstra kostnad                                  | Snefokk kjenner fallgruvene og sparer deg for de første feilrundene |

## Hva du trenger (for å gjøre det selv)

- Et aktivt **Claude Pro**-abonnement (eller høyere) — skillen kjører i
  Claude Cowork / Claude Code
- **Python 3** — for å bygge selve HTML-en (kun standardbibliotek, ingen
  `pip install`; finnes på de fleste maskiner)
- **Chrome-tilkobling** (Claude i Chrome) — for å søke Facebooks
  arrangementssøk og lese plakater/bilder aktørene poster
- **Internett-tilgang** — for websøk mot lokale nettsider

Skillen i seg selv er gratis og åpen kildekode.

## Kom i gang (gjør det selv)

1. **Last ned skillen** — klon eller last ned dette repoet.
2. **Installer i Claude** — pek Cowork/Claude Code mot skill-mappa
   (`~/.claude/skills/`).
3. **Følg `SKILL.md`** — den tar deg steg for steg: fortell om stedet, la
   Claude kartlegge kildene, godkjenn forslagene, og få en ferdig HTML-fil.
4. **Legg fila ut** — åpne den direkte, legg den på eksisterende
   webhotell/hosting, eller be Snefokk om å hoste den.
5. **Oppdater ved å kjøre skillen på nytt** — kildelista gjenbrukes
   automatisk, så bare nye arrangementer samles inn før HTML-en bygges på
   nytt.

## Bygg fra en config-fil direkte (avansert)

Skillen produserer en `config.json` og bygger HTML-en med et lite
Python-skript (kun standardbibliotek — ingen `pip install`):

```bash
python3 scripts/build_html.py \
  --config <sted>-kalender/config.json \
  --template templates/kalender-mal.html \
  --output <sted>-kalender/hva-skjer-i-<sted>.html
```

Se [`examples/config-eksempel.json`](examples/config-eksempel.json) for full
struktur, og [`examples/hva-skjer-i-vadso.html`](examples/hva-skjer-i-vadso.html)
for hvordan resultatet ser ut.

## Eksempler

- **Vadsø** — se [`examples/hva-skjer-i-vadso.html`](examples/hva-skjer-i-vadso.html)
  for en bygget demo (eksempeldata, ikke live)

## Lisens

Se [LICENSE](LICENSE). MIT — åpen kildekode, bruk, modifiser og del fritt.
