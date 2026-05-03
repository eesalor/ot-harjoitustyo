# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on, että käyttäjä voi pitää kirjaa ja hallita tekemättömiä tehtäviään. Tehtäviin on mahdollista merkitä ajankohta, jolloin tehtävä tulee tehdä. Sovellusta on mahdollista käyttää *yksi käyttäjä*. Sovellusta jatkokehitettäessä voidaan lisätä mahdollisuus luoda useita eri käyttäjiä, joilla on omat tehtävänsä. Sovellus toteutetaan työpöytäsovelluksena, joka hyödyntää SQL-tietokantaa.

## Sovelluksen toiminnallisuudet

Sovellus sisältää seuraavat toiminnallisuudet:

- [x] Käyttäjä voi lisätä uuden tehtävän sisältäen seuraavat tiedot:
  - Tehtävän kuvaus
    - Tehtävän kuvaus ei saa olla tyhjä syöte ja sen enimmäispituus on 100 merkkiä
  - Tehtävän määräaika
    - Syötettävän päivämäärän oltava muotoa pp.kk.vvvv eikä se saa olla mennyt päivämäärä
  - Aihekategoria
    - Kategoria ei ole pakollinen.
    - Käyttäjä voi lisätä korkeintaan yhden kategorian per tehtävä
    - Käyttäjä voi lisätä tehtävään kategorian vain tehtävän luomisen yhteydessä joko kirjoittamalla sen kenttään tai valitsemalla kategorian valikosta aiemmin lisättyjen kategorioiden joukosta.
    - Käyttäjä voi lisätä sovellukseen kokonaan uuden kategorian vain kirjoittamalla sen lomakkeelle luodessaan uutta tehtävää. Käyttäjä ei voi siis lisätä ja tallentaa sovellukseen suoraan pelkkiä kategorioita.
    - Olemassa olevaa kategoriaa ei lisätä moneen kertaan
  - Oletusarvoisesti uuden tehtävän tila on "tekemättä"

- [x] Käyttäjä näkee sovellukseen lisätyt tehtävät
    -  Tekemättömät ja tehdyt tehtävät näkyvät käyttäjälle erillisissä luetteloruuduissa
- [X] Käyttäjä voi merkitä tekemättömiä tehtäviä tehdyksi
- [X] Käyttäjä voi merkitä tehtyjä tehtäviä tekemättömäksi 
- [x] Käyttäjä voi poistaa tehtäviä
- [X] Käyttäjä voi poistaa lisäämiään kategorioita
    - Kategorian poistaminen poistaa kategorian myös niistä tehtävistä, joihin kyseinen kategoria on liitetty

## Jatkokehitysideoita

Sovelluksen mahdollisia jatkokehityssuuntia:

- [ ] Käyttäjä voi muokata lisäämiään tehtäviä
- [ ] Käyttäjä voi lisätä muita tehtäviin liittyviä tietoja
  - Esim. käyttäjä voi määritellä tehtäviin toistumistiheyden, jolloin sovellus näyttää seuraavan ajankohdan tehtävän tekemiselle
- [ ] Käyttäjä voi järjestää tehtäviä esimerkiksi päivänmäärän tai kategorian mukaan
- [ ] Käyttäjä voi suodattaa tehtävänäkymää tehtäviin liittyvien kategorioiden perusteella
- [ ] Käyttäjä voi lisätä pelkästään uusia kategorioita valmiiseen valikkoon
- [ ] Mahdollisuus luoda käyttäjätunnuksia ja kirjatua sovellukseen eri käyttäjillä
