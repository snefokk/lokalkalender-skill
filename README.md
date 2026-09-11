# lokalkalender-skill

Bygger en skreddersydd **kalenderrunde-skill** for et hvilket som helst sted
— by, kommune eller region. En ukentlig rutine som samler lokale
arrangementer fra Facebook og andre kilder uten API, legger dem fram til
godkjenning, og (hvis stedet har en nettside for det) skriver de godkjente
inn. En åpen skill for Claude (Cowork / Claude Code).

> **Vil du heller at vi bygger kalenderrunden for deg?**
> Bestill en ferdig kalenderrunde på **[snefokk.com/kalender](https://snefokk.com/kalender)**
> — så bygger Snefokk rutinen, tilpasser den kildene og nettsiden deres har,
> og leverer klar til bruk. Dette repoet er for deg som vil gjøre jobben
> selv, gratis.

## Hva skillen lager

Ikke selve kalenderen — en **ny skill** som gjør jobben ukentlig for stedet
ditt, etter samme mønster som ble bygget for [vadsoby.com](https://vadsoby.com):

- Kartlegger automatisk hvilke lokale kilder som har strukturerte data (kino,
  kulturhus, idrettslag med seriekamper, bibliotek, museum, kirke, golf …)
  og hvilke som bare finnes på Facebook
- Genererer en ferdig `SKILL.md` for stedet, med kildetabell, steg-for-steg
  instruksjoner og kjente fallgruver
- Skriv-steget i den genererte skillen leverer enten en enkel forslagsliste,
  eller (hvis dere oppgir nettsidens datastruktur) et format tilpasset
  akkurat deres system
- **Mennesket godkjenner alltid før noe publiseres** — det gjelder både denne
  skillen og hver eneste skill den genererer

## Hvem det er for

- Kommuner, næringsforeninger og reiselivsorganisasjoner som vil ha samme
  type ukentlige kalenderrutine som Vadsø, for sitt eget sted
- Nettsteder som allerede har en kalenderfunksjon, men mangler en rutine for
  arrangementer som ikke ligger i noe API
- Steder uten egen nettside ennå, som vil ha en ryddig ukentlig oversikt over
  lokale arrangementer å jobbe videre med

## To måter å få kalenderrunden

| Gjør det selv (dette repoet) | La Snefokk gjøre jobben |
| --- | --- |
| Gratis — krever et Claude-abonnement | Bestill på **[snefokk.com/kalender](https://snefokk.com/kalender)** |
| Du kjører skillen selv i Claude — genererer en skill for stedet ditt, som du deretter kjører ukentlig | Snefokk bygger, tilpasser kildene og leverer, med én tilbakemeldingsrunde |
| Krever at du selv kjører kartleggingen og finjusterer kildetabellen | Snefokk kjenner fallgruvene fra Vadsø-varianten og sparer deg for de første feilrundene |

## Hva du trenger (for å gjøre det selv)

- Et aktivt **Claude Pro**-abonnement (eller høyere) — skillen kjører i
  Claude Cowork / Claude Code
- **Chrome-tilkobling** (Claude i Chrome) — for å søke Facebooks
  arrangementssøk og lese plakater/bilder aktørene poster
- **Internett-tilgang** — for websøk mot lokale nettsider, kino, bibliotek,
  kirke osv.
- *Valgfritt:* tilgang til nettsidens repo/CMS, hvis dere vil ha et
  skreddersydd skriv-steg i stedet for en generisk forslagsliste

Skillen i seg selv er gratis og åpen kildekode.

## Kom i gang (gjør det selv)

1. **Last ned skillen** — klon eller last ned dette repoet.
2. **Installer i Claude** — pek Cowork/Claude Code mot skill-mappa
   (`~/.claude/skills/`).
3. **Følg `SKILL.md`** — den tar deg steg for steg: fortell om stedet, la
   Claude kartlegge kildene, avklar skriv-format, og få en ferdig
   `SKILL.md` for stedet ditt.
4. **Ta den nye skillen i bruk** — legg den genererte mappa i din egen
   skill-katalog og kjør den ukentlig, med et menneske som godkjenner før
   noe publiseres.

## Eksempler

- **vadsoby.com** — den opprinnelige, håndbygde kalenderrunden dette
  mønsteret er hentet fra, med kino, kulturscene, idrettslag, bibliotek,
  kirke, golf og en håndfull Facebook-only-aktører

## Lisens

Se [LICENSE](LICENSE). MIT — åpen kildekode, bruk, modifiser og del fritt.
