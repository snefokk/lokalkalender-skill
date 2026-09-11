# Vanlige feller — generalisert fra vadsoby-kalenderrunde

Disse fellene er ikke Vadsø-spesifikke. De dukker opp for ethvert sted, og bør
skrives inn i **hver eneste** genererte skill (i seksjonen «Feller som har
rammet oss»), tilpasset det aktuelle stedets faktiske aktører og treff.

## Navnefella

Et likelydende domene eller en likelydende Facebook-side finnes ofte et helt
annet sted i landet. Sjekk alltid at nettstedet/siden faktisk tilhører
den lokale aktøren — adresse, telefonnummer eller «om oss»-tekst må stemme
med stedet du bygger for. Dette har slått feil flere ganger i Vadsø-versjonen
(tre bom på rad), og er den vanligste enkeltfeilen.

## Søketreff utenfor området

Både filmtitler og arrangementsnavn kan gi treff langt unna. Et Facebook-søk
på stedsnavnet finner arrangementer der stedsnavnet bare forekommer i en
filmtittel eller et vennskapsarrangement et annet sted i landet. **Sjekk
stedet i treffet, ikke bare selve søketreffet.** Dette blir viktigere jo bredere
det geografiske området er (region > kommune > by, se `kildekategorier.md`).

## Duplikater er ikke alltid duplikater

To oppføringer med samme tittel samme dag kan være to forskjellige ting —
f.eks. en utstillingsåpning og selve utstillingsperioden. Sjekk arrangørens
egen side før du slår sammen to treff til ett.

## Strukturerte data er ikke nødvendigvis riktige data

Selv API-er og feeds kan ha feil:
- Tidssoner kan være stemplet feil (lokal tid merket med `Z` som om den var UTC).
- Norske tegn (æ, ø, å) kan komme HTML-kodet fra enkelte kilder og falle ut av
  søk/filtrering hvis de ikke normaliseres.
- Stikkprøv alltid minst ett eksempel fra hver strukturert kilde mot
  arrangørens egen tekst før du stoler på resten.

## Arrangør er ikke sted

Spør alltid to spørsmål, ikke ett: *hvem står bak arrangementet* og *hvor
skjer det*. En forening kan arrangere noe et helt annet sted enn der
foreningen selv holder til.

## Ikke gjett

Mangler pris, sted eller klokkeslett — la feltet stå tomt/uklart og marker det
som usikkert i forslagslista, i stedet for å anta et sannsynlig svar. Mangel
på billettlenke betyr for eksempel ikke automatisk «gratis».

## Sider uten årstall

Enkelte lokale kilder (typisk museum og eldre foreningssider) skriver bare
dag og måned, ikke år, og fjerner ikke passerte arrangementer fra lista. Se
etter en teknisk vei rundt dette (f.eks. stigende ID-er i URL-en, som i
Vadsø-varianten), eller flagg oppføringene som «usikker dato» og la mennesket
avgjøre.
