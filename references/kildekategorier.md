# Kildekategorier — hva du leter etter, og hvor

Bruk denne lista i Steg 2 og 3 av `SKILL.md`. For hvert sted finnes ikke alle
kategoriene — noen steder har verken kino eller golfklubb. Gå gjennom lista,
søk, og noter «finnes ikke her» der det stemmer i stedet for å hoppe over
kategorien stille.

For hver aktør du finner: sjekk **navnefella** før du går videre — stemmer
domenet/siden faktisk med den lokale aktøren, ikke en likelydende aktør et
annet sted? (Se `vanlige-feller.md`.)

## A — Ofte strukturerte data (sjekk om et API/feed finnes)

| Kategori | Typisk plattform | Hvordan sjekke |
| --- | --- | --- |
| Kino | Filmweb, Nordisk Film Kino, kommunal kino | Søk «[sted] kino». Filmweb har åpent API for de fleste kinoene i Norge. |
| Kulturhus / konsertscene | TicketCo, Checkin.no, Ticketmaster, Hoopla | Søk «[sted] kulturhus billetter». Se om det er en ekstern billettleverandør — de har ofte feed/API. |
| Idrettslag, seriekamper | fotball.no (NFF), handball.no, volleyball.no | Søk «[idrettslag] fotball.no». Seriekamper er strukturerte og oppdateres automatisk. |
| Bibliotek | Lokalt CMS med «Arrangementer»-side | Søk «[sted] bibliotek arrangementer». Sjekk om URL-en har dato i seg (mønster som kan skrapes). |
| Museum | DigitaltMuseum, lokalt museumslag, kommunalt museum | Søk «[sted] museum arrangementer». Sjekk om siden mangler årstall i lista (vanlig — se `vanlige-feller.md`). |
| Kirke | «Skjer i kirken»-plattformen (skjerikirken.no), eller kirken.no-menighetsside | Søk «[sted] kirke gudstjenester». Skjer i kirken-plattformen er strukturert og pålitelig; kirken.no-arkivsider er ofte foreldet. |
| Golf | GolfBox | Søk «[sted] golfklubb». GolfBox brukes av de fleste norske golfklubber for turneringer. |
| Svømmehall / idrettshall | Kommunens sesongprogram | Ofte et fast ukentlig mønster (åpningstider, svømmekurs) — ikke enkeltarrangementer. Sjekk om det i det hele tatt gir mening som kalenderdata, eller om det heller er info-tekst. |

## B — Nesten alltid kun Facebook

| Kategori | Merknad |
| --- | --- |
| Barer, puber, utesteder | Kveldsarrangementer, quiz, konserter. Sjekk «Arrangementer»-fanen, ikke bare innlegg. |
| Restauranter med arrangementer | Temakvelder, livemusikk. |
| Kunstforeninger, historielag, husflidslag | Ofte medlemsdrevne sider med lav postefrekvens — sjekk om noen i organisasjonen kan gi direkte tilgang i stedet for å skrape. |
| Idrettslag uten seriekamper (klubbkvelder, trening) | F.eks. bowling-klubbkvelder, skiklubbens fellesturer. |
| Ungdomsklubb / ungdomshus | Ofte kun Facebook eller Instagram, sjelden egen nettside. |
| Frivilligsentral | Koordinerer ofte andre foreningers arrangementer — god kilde for bredde. |

## C — Lett å glemme, men ofte gullgruver

- **Turistkontor / besøkssenter** har ofte allerede en samlet «hva skjer»-liste
  for hele regionen — sjekk om den kan brukes som kryssjekk eller direkte kilde
  i stedet for å bygge alt fra bunnen.
- **Kommunens egen nettside** har noen ganger en «Kultur og fritid»-kalender
  som allerede samler flere av aktørene over.
- **Regionale/interkommunale aktører** (f.eks. en felles kulturskole eller et
  regionteater) dekker gjerne flere steder på én gang — sjekk om de allerede
  filtrerer per sted, eller om du må filtrere selv.

## Geografisk avgrensning — avklar dette FØR du søker

«Sted» kan bety en by, en kommune eller en hel region. Avklar med brukeren i
Steg 1 hvor grensa går, og bruk det bevisst i hvert søk:

- **By/tettsted** (som Vadsø i den opprinnelige skillen): søk på tettstedsnavn
  + nærmeste nabotettsteder brukeren nevner.
- **Kommune**: søk på kommunenavn, men vær obs på at kommunen kan ha flere
  tettsteder med hvert sitt aktørmiljø — spør brukeren om alle skal dekkes,
  eller bare kommunesenteret.
- **Region** (flere kommuner): søket blir bredere og du får flere treff
  utenfor det egentlige området. Regionale kalendere trenger strengere
  stedsjekk per treff (se `vanlige-feller.md` — «Søketreff utenfor
  området»), og du bør vurdere om regionen er stor nok til at kalenderen
  heller bør bygges kommune for kommune og slås sammen.
