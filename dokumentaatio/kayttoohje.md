# Käyttöohje

## Sovelluksen käynnistäminen

Sovelluksen riippuvuudet asennetaan komennolla
```
poetry install
```
Sovelluksen tietokanta alustetaan ennen käynnistämistä komennolla
```
poetry run invoke init-database
```
Sovelluksen voi käynnistää komennolla
```
poetry run invoke start
```

## Käynnistyminen / aloitusnäkymä

Sovellus käynnistämisen jälkeen ilmestyy ensin aloitusnäkymä.

Sovelluksen päänäkymään eli tehtävänäkymään pääsee painamalla nappia ”Start”.

## Tehtävänäkymä

Tehtävänäkymässä voi

- luoda uusia tehtäviä
- luoda uusia kategorioita
- merkitä tehtäviä tehdyksi / tekemättömäksi
- poistaa tehtäviä
- poistaa kategorioita

Alla on kuvattu näitä toiminnallisuuksia tarkemmin.

### Uuden tehtävän luominen

Sovelluksessa on mahdollista lisätä uusia tehtäviä ja niihin liittyviä määräaikoja. Molemmat ovat pakollisia tietoja. Lisäksi tehtävään voi halutessaan lisätä kategorian.

Kenttään ”Task” kirjoitetaan tehtävän nimi, jonka enimmäispituus on 100 merkkiä. Kenttään ”Date” kirjoitetaan määräaika muodossa ”pp.kk.vvvv”. Lisättävä päivämäärä ei voi olla mennyt päivämäärä.
Kategoriakenttään ”Enter or select category” voi kirjoittaa kategorian tai valita valikosta aiemmin lisätyn kategorian.

Tehtävä luodaan painamalla nappia ”Create”.

Mikäli tehtävän luominen onnistuu, lisätty tehtävä siirtyy luetteloruutuun ”Uncompleted tasks”.

### Uuden kategorian luominen

Uuden kategorian lisääminen valikkoon on mahdollista vain tehtävän lisäämisen yhteydessä. Erillistä toimintoa pelkän kategorian lisäämiselle ei ole.

### Tehtävien merkitseminen tehdyksi / tekemättömäksi

Oletuksena uuden tehtävän tila on tekemätön (uncompleted). Sovelluksessa on mahdollista merkitä tekemätön tehtävä tehdyksi valitsemalla kyseinen tehtävä luettelosta ja painamalla nappia ”Set completed”.
Tämän jälkeen tehtävä siirtyy viereiseen luetteloon, jossa näkyy tehdyiksi merkityt tehtävät (”Completed tasks”).

Sovelluksessa voi myös myös muuttaa tehtyjen tehtävien tilan takaisin tekemättömäksi valitsemalla kyseinen valmiiksi merkitty tehtävä ja painamalla nappia ”Set uncompleted”. Tämän jälkeen tehtävä siirtyy takaisin viereiseen luetteloon, jossa näkyy tekemättömät tehtävät (”Uncompleted tasks”).

### Tehtävien poistaminen

Sovelluksessa on mahdollista poistaa sekä tekemättömiä että tehtyjä tehtäviä.
Tekemättömien tehtävien poistaminen tapahtuu valitsemalla luettelosta tehtävän ja painamalla kyseisen luettelon alla olevaa nappia ”Delete selected task”.

Vastaavasti tehtyjen tehtävien poistaminen tapahtuu valitsemalla luettolosta tehtävän ja painamalla kyseisen luettelon alla olevaa nappia ”Delete selected task”.

### Kategorian poistaminen

Sovellukseen lisättyjä kategorioita voi poistaa valitsemalla pudotusvalikosta poistettavan kategorian ja painamalla nappia ”Delete selected category”.
Kategorian poistaminen poistaa kategorian myös niistä tehtävistä, joihin kyseinen kategoria on lisätty.
