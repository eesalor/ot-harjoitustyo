# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on, että käyttäjä voi pitää kirjaa ja hallita tekemättömiä tehtäviään. Tehtäviin on mahdollista merkitä ajankohta, jolloin tehtävä tulee tehdä. Sovellusta on mahdollista käyttää *yksi käyttäjä*. Sovellusta jatkokehitettäessä voidaan lisätä mahdollisuus luoda useita eri käyttäjiä, joilla on omat tehtävänsä. Sovellus toteutetaan työpöytäsovelluksena, joka hyödyntää SQL-tietokantaa.

## Suunnitellut toiminnallisuudet

Sovellukseen suunnitellut toiminnallisuudet:
- *Tehdyt toiminnallisuudet merkitty ruksilla*

- [x] Käyttäjä voi lisätä uuden tehtävän sisältäen seuraavat tiedot:
  - [x] Tehtävän kuvaus
    - [X] Tehtävän kuvaus ei saa olla tyhjä syöte
    - [X] Tehtävän kuvauksen enimmäispituus on 100 merkkiä
  - [x] Tehtävän määräaika
    - [X] Syötettävän päivämäärän oltava muotoa pp.kk.vvvv
    - [X] Syötettävä päivämäärä ei voi olla mennyt päivämäärä
  - [X] Aihekategoria
    - [X] Kategoria ei ole pakollinen.
    - [X] Käyttäjä voi lisätä kategorian vain tehtävän luomisen yhteydessä.
    - [X] Käyttäjä voi lisätä korkeintaan yhden kategorian per tehtävä.
    - [X] Käyttäjä voi lisätä kokonaan uuden kategorian tehtävän luomisen yhteydessä tai valita kategorian aiemmin lisättyjen kategorioiden joukosta.
  - [X] Onko tehtävä tehty / tekemättä
- [x] Käyttäjä näkee sovellukseen lisätyt tehtävät
    - [X] Tekemättömät ja tehdyt tehtävät näkyvät käyttäjälle erillisissä luetteloruuduissa
- [X] Käyttäjä voi merkitä tekemättömiä tehtäviä tehdyksi
- [X] Käyttäjä voi merkitä tehtyjä tehtäviä tekemättömäksi 
- [x] Käyttäjä voi poistaa tehtäviä
- [X] Käyttäjä voi poistaa lisäämiään kategorioita
    - [X] Kategorian poistaminen poistaa kategorian niistä tehtävistä, joihin kyseinen kategoria on liitetty  
- [ ] Käyttäjä voi muokata lisäämiään tehtäviä

## Jatkokehitysideoita

Sovelluksen mahdollisia jatkokehityssuuntia:

- [ ] Käyttäjä voi tarkastella tekemiään tehtäviä
- [ ] Käyttäjä voi lisätä muita tehtäviin liittyviä tietoja
  - Esim. käyttäjä voi määritellä tehtäviin toistumistiheyden, jolloin sovellus näyttää seuraavan ajankohdan tehtävän tekemiselle
- [ ] Käyttäjä voi järjestää tehtäviä esimerkiksi päivänmäärän tai kategorian mukaan
- [ ] Käyttäjä voi suodattaa tehtävänäkymää tehtäviin liittyvien kategorioiden perusteella
- [ ] Käyttäjä voi lisätä uusia kategorioita valmiiseen valikkoon
- [ ] Mahdollisuus luoda käyttäjätunnuksia ja kirjatua sovellukseen eri käyttäjillä
